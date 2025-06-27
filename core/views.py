from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from core.utils import execute_query, create_jwt_token
import json
import datetime

def api_response(data, status=200):
    """Helper to return a JSON response."""
    return JsonResponse(data, status=status, safe=False)


@csrf_exempt
def register_user(request):
    """
    Handles user registration.
    Method: POST
    Endpoint: /api/auth/register/
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not all([username, email, password]):
                return api_response({'detail': 'Username, email, and password are required.'}, status=400)

            hashed_password = make_password(password)

            existing_user = execute_query(
                "SELECT id FROM users WHERE username = %s OR email = %s",
                (username, email),
                fetch_type='one'
            )
            if existing_user:
                return api_response({'detail': 'Username or email already exists.'}, status=409)

            user_id = execute_query(
                "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s) RETURNING id",
                (username, email, hashed_password),
                fetch_type='one'
            )['id']

            return api_response({'message': 'User registered successfully.', 'user_id': user_id}, status=201)
        except json.JSONDecodeError:
            return api_response({'detail': 'Invalid JSON in request body.'}, status=400)
        except Exception as e:
            print(f"Error registering user: {e}")
            return api_response({'detail': 'An internal server error occurred.'}, status=500)
    return api_response({'detail': 'Method not allowed.'}, status=405)


@csrf_exempt
def login_user(request):
    """
    Handles user login and JWT token generation.
    Method: POST
    Endpoint: /api/auth/login/
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not all([username, password]):
                return api_response({'detail': 'Username and password are required.'}, status=400)

            user = execute_query(
                "SELECT id, username, password_hash FROM users WHERE username = %s",
                (username,),
                fetch_type='one'
            )

            if not user:
                return api_response({'detail': 'Invalid credentials.'}, status=401)


            if not check_password(password, user['password_hash']):
                return api_response({'detail': 'Invalid credentials.'}, status=401)


            access_token = create_jwt_token(user['id'], user['username'])

            return api_response({
                'message': 'Login successful.',
                'access_token': access_token,
                'user_id': user['id'],
                'username': user['username']
            })
        except json.JSONDecodeError:
            return api_response({'detail': 'Invalid JSON in request body.'}, status=400)
        except Exception as e:
            print(f"Error logging in user: {e}")
            return api_response({'detail': 'An internal server error occurred.'}, status=500)
    return api_response({'detail': 'Method not allowed.'}, status=405)



@csrf_exempt
def upload_pin(request):
    """
    Handles uploading a new pin.
    Method: POST
    Endpoint: /api/pins/
    Permissions: Authenticated
    """
    if request.method == 'POST':
        if not hasattr(request, 'user_id') or not request.user_id:
            return api_response({'detail': 'Authentication required.'}, status=401)

        try:
            data = json.loads(request.body)
            image_url = data.get('image_url')
            title = data.get('title')
            description = data.get('description', '')
            tags = data.get('tags', '')

            if not all([image_url, title]):
                return api_response({'detail': 'Image URL and title are required.'}, status=400)

            user_id = request.user_id

            pin_id = execute_query(
                "INSERT INTO pins (user_id, image_url, title, description, tags) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (user_id, image_url, title, description, tags),
                fetch_type='one'
            )['id']

            return api_response({'message': 'Pin uploaded successfully.', 'pin_id': pin_id}, status=201)
        except json.JSONDecodeError:
            return api_response({'detail': 'Invalid JSON in request body.'}, status=400)
        except Exception as e:
            print(f"Error uploading pin: {e}")
            return api_response({'detail': 'An internal server error occurred.'}, status=500)
    return api_response({'detail': 'Method not allowed.'}, status=405)

def list_pins(request):
    """
    Lists all pins (feed).
    Method: GET
    Endpoint: /api/pins/
    Permissions: Public
    """
    if request.method == 'GET':
        try:
            pins = execute_query(
                "SELECT p.id, p.image_url, p.title, p.description, p.tags, p.created_at, u.username "
                "FROM pins p JOIN users u ON p.user_id = u.id ORDER BY p.created_at DESC",
                fetch_type='all'
            )

            for pin in pins:
                if 'created_at' in pin and isinstance(pin['created_at'], datetime.datetime):
                    pin['created_at'] = pin['created_at'].isoformat()
                if 'updated_at' in pin and isinstance(pin['updated_at'], datetime.datetime):
                    pin['updated_at'] = pin['updated_at'].isoformat()

            return api_response(pins)
        except Exception as e:
            print(f"Error listing pins: {e}")
            return api_response({'detail': 'An internal server error occurred.'}, status=500)
    return api_response({'detail': 'Method not allowed.'}, status=405)

@csrf_exempt
def pin_detail(request, pin_id):
    """
    Handles GET, PUT, DELETE for a specific pin.
    Method: GET, PUT, DELETE
    Endpoint: /api/pins/<id>/
    Permissions: Owner-only for PUT/DELETE
    """
    try:
        pin = execute_query(
            "SELECT p.id, p.user_id, p.image_url, p.title, p.description, p.tags, p.created_at, p.updated_at, u.username "
            "FROM pins p JOIN users u ON p.user_id = u.id WHERE p.id = %s",
            (pin_id,),
            fetch_type='one'
        )

        if not pin:
            return api_response({'detail': 'Pin not found.'}, status=404)


        if 'created_at' in pin and isinstance(pin['created_at'], datetime.datetime):
            pin['created_at'] = pin['created_at'].isoformat()
        if 'updated_at' in pin and isinstance(pin['updated_at'], datetime.datetime):
            pin['updated_at'] = pin['updated_at'].isoformat()

        if request.method == 'GET':
            return api_response(pin)

        if not hasattr(request, 'user_id') or not request.user_id:
            return api_response({'detail': 'Authentication required.'}, status=401)

        if pin['user_id'] != request.user_id:
            return api_response({'detail': 'You do not have permission to perform this action.'}, status=403)

        if request.method == 'PUT':
            try:
                data = json.loads(request.body)
                title = data.get('title', pin['title'])
                description = data.get('description', pin['description'])
                tags = data.get('tags', pin['tags'])
                image_url = data.get('image_url', pin['image_url'])

                execute_query(
                    "UPDATE pins SET title = %s, description = %s, tags = %s, image_url = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                    (title, description, tags, image_url, pin_id)
                )
                return api_response({'message': 'Pin updated successfully.'})
            except json.JSONDecodeError:
                return api_response({'detail': 'Invalid JSON in request body.'}, status=400)
            except Exception as e:
                print(f"Error updating pin: {e}")
                return api_response({'detail': 'An internal server error occurred.'}, status=500)

        elif request.method == 'DELETE':
            try:
                execute_query("DELETE FROM pins WHERE id = %s", (pin_id,))
                return api_response({'message': 'Pin deleted successfully.'}, status=204)
            except Exception as e:
                print(f"Error deleting pin: {e}")
                return api_response({'detail': 'An internal server error occurred.'}, status=500)

    except Exception as e:
        print(f"Error in pin_detail view: {e}")
        return api_response({'detail': 'An internal server error occurred.'}, status=500)

    return api_response({'detail': 'Method not allowed.'}, status=405)

