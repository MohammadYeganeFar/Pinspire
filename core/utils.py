import psycopg2
from psycopg2.extras import RealDictCursor
from django.utils import timezone
import datetime
import jwt
import os


DB_NAME = os.environ.get('DB_NAME', 'pinspire_db')
DB_USER = os.environ.get('DB_USER', 'pinspire_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'pinspire_password')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-super-secret-jwt-key-please-change-this-in-production!')
ALGORITHM = 'HS256'
ACCESS_TOKEN_LIFETIME_MINUTES = 60
REFRESH_TOKEN_LIFETIME_DAYS = 7

def get_db_connection():
    """Establishes and returns a database connection."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        raise

def execute_query(query, params=None, fetch_type='none'):
    """
    Executes a raw SQL query.

    Args:
        query (str): The SQL query string.
        params (tuple, optional): Parameters to pass to the query. Defaults to None.
        fetch_type (str): 'one' for single row, 'all' for multiple rows, 'none' for no fetch.

    Returns:
        dict or list of dicts: Fetched data, or None for 'none' fetch_type.
    """
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, params)
        conn.commit()

        if fetch_type == 'one':
            return cursor.fetchone()
        elif fetch_type == 'all':
            return cursor.fetchall()
        else:
            return None
    except psycopg2.Error as e:
        conn.rollback()
        print(f"SQL query error: {e}")
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def create_jwt_token(user_id, username):
    """
    Creates a simplified JWT access token.
    DO NOT USE IN PRODUCTION WITHOUT PROPER SECURITY REVIEW.
    """
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': timezone.now() + datetime.timedelta(minutes=ACCESS_TOKEN_LIFETIME_MINUTES),
        'iat': timezone.now()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_jwt_token(token):
    """
    Decodes a simplified JWT token.
    DO NOT USE IN PRODUCTION WITHOUT PROPER SECURITY REVIEW.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}

