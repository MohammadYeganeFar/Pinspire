from django.http import JsonResponse
from core.utils import decode_jwt_token, execute_query

class JWTAuthenticationMiddleware:
    """
    Custom middleware to authenticate users via JWT token.
    Attaches 'user_id' and 'username' to request.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'OPTIONS':
            return self.get_response(request)

        public_urls = [
            '/api/auth/register/',
            '/api/auth/login/',
            '/api/pins/',
            '/api/pins/search/',
        ]
        if any(request.path.startswith(url) for url in public_urls):
            request.user_id = None 
            request.username = None
            return self.get_response(request)

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=401)

        try:
            token_type, token = auth_header.split(' ')
            if token_type.lower() != 'bearer':
                return JsonResponse({'detail': 'Invalid token type. Must be Bearer.'}, status=401)

            decoded_token = decode_jwt_token(token)

            if "error" in decoded_token:
                return JsonResponse({'detail': decoded_token['error']}, status=401)

            user_id = decoded_token.get('user_id')
            username = decoded_token.get('username')

            if not user_id or not username:
                return JsonResponse({'detail': 'Invalid token payload.'}, status=401)

            user = execute_query("SELECT id, username FROM users WHERE id = %s", (user_id,), fetch_type='one')
            if not user:
                return JsonResponse({'detail': 'User not found.'}, status=401)

            request.user_id = user_id
            request.username = username
        except ValueError:
            return JsonResponse({'detail': 'Invalid Authorization header format.'}, status=401)
        except Exception as e:
            print(f"Authentication error: {e}")
            return JsonResponse({'detail': 'An error occurred during authentication.'}, status=500)

        response = self.get_response(request)
        return response

