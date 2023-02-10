"""
Django settings for app project.
"""
from pathlib import Path

from passlib.context import CryptContext
from dotenv import dotenv_values


BASE_DIR = Path(__file__).resolve().parents[1]
CONF_DICT = dotenv_values(BASE_DIR / '.secret')

# Load
SECRET_KEY = CONF_DICT.get('DJANGO_SECRET')
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

# Crypto definitions
PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Token definitions
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
TOKEN_TYPE = 'JWT'
JWT_SECRET_KEY = CONF_DICT.get('JWT_SECRET_KEY')
JWT_REFRESH_SECRET_KEY = CONF_DICT.get('JWT_REFRESH_SECRET_KEY')

# Application definition
WSGI_APPLICATION = 'app.wsgi.application'
ROOT_URLCONF = 'app.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'app.authentication'
]

AUTH_USER_MODEL = 'authentication.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': CONF_DICT.get('POSTGRESQL_DB_NAME'),
        'USER': CONF_DICT.get('POSTGRESQL_DB_USER'),
        'PASSWORD': CONF_DICT.get('POSTGRESQL_DB_PASSWORD'),
        'HOST': CONF_DICT.get('POSTGRESQL_DB_HOST'),
        'PORT': CONF_DICT.get('POSTGRESQL_DB_PORT')
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK SETTINGS

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'app.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'errors',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'app.authentication.backends.JWTAuthentication',
    ),
}
