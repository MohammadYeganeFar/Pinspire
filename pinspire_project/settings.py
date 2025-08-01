import os
import decouple
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-your-secret-key-for-django-please-change-this!')

DEBUG = True 

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # 'django.contrib.admin', # Not using Django Admin with raw SQL
    'django.contrib.auth', # Not using Django's Auth system directly, but hashers are used
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'core',
    'account.apps.AccountConfig',
    'user_interactions.apps.UserInteractionsConfig',
    'shop_manage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # Keep for POST requests, but views are @csrf_exempt
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Not using Django's Auth system
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'core.middlewares.JWTAuthenticationMiddleware', # Our custom JWT middleware
]

ROOT_URLCONF = 'pinspire_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pinspire_project.wsgi.application'

# Database configuration (NOT USED BY DJANGO ORM, but for reference)
# Our raw SQL utilities will use environment variables directly.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Just for Django's internal checks, not used by our raw SQL
        'NAME': decouple.config('DB_NAME', 'pinspire_db'),
        'USER': decouple.config('DB_USER', 'pinspire_user'),
        'PASSWORD': decouple.config('DB_PASSWORD', 'pinspire_password'),
        'HOST': decouple.config('DB_HOST', 'localhost'),
        'PORT': decouple.config('DB_PORT', '5432'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': 
        ('rest_framework_simplejwt.authentication.JWTAuthentication', ),

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 1,
    
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
