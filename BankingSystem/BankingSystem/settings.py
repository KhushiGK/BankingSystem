"""
Django settings for BankingSystem project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""



from pathlib import Path
import os
from django.contrib.messages import constants as messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your-secret-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
    'rest_framework',
    'corsheaders',
    'django_celery_beat',
    'Custom_admin',
    'django_prometheus',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

LOGIN_URL = '/login/'  # Set your custom login URL


ROOT_URLCONF = "BankingSystem.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # BankingSystem/BankingSystem/templates
            os.path.join(BASE_DIR, 'Custom_admin', 'templates'),  # BankingSystem/Custom_admin/templates
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "BankingSystem.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Detect environment
 # Local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",  # In-memory cache
        "LOCATION": "unique-snowflake",
        "TIMEOUT": 30,  # Default timeout (can be overridden)
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',

    
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Celery Beat Settings
CELERY_BEAT_SCHEDULE = {
    # 'test-task-30-seconds': {
    #     'task': 'app.tasks.test_task',
    #     'schedule': 30.0,  # Run every 30 seconds
    # },
    'calculate-interest-daily': {
        'task': 'app.tasks.calculate_interest',
        'schedule': 86400.0,  # 86400 24 hours
    },
    'calculate-monthly-interest-summary': {
        'task': 'app.tasks.calculate_monthly_interest_summary',
        'schedule': 2592000.0,  # 2592000 30 days
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server for Gmail
EMAIL_PORT = 587  # Use 587 for TLS, 465 for SSL
EMAIL_USE_TLS = True  # Enable TLS security
EMAIL_USE_SSL = False  # Make sure this is False if using TLS
EMAIL_HOST_USER = 'mthreebanking@gmail.com'  # Your email
EMAIL_HOST_PASSWORD = 'tfsqbnufvupatngl'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
# SESSION_CACHE_ALIAS = "default"  # cache alias
# SESSION_COOKIE_AGE = 120  # 2 minutes timeout
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # expire session when browser is closed
# SESSION_SAVE_EVERY_REQUEST = True  # save session every request
# LOGIN_URL = "/login/"  # login url
# LOGOUT_REDIRECT_URL = "/login/"  # logout redirect url to login page
SESSION_COOKIE_SECURE = False  # True in production with HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'  # Or 'None' if using cross-site
CORS_ALLOW_CREDENTIALS = True  # If using CORS

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://web:8000",
    "http://localhost:3000",
    "https://3661-2405-201-c047-c859-8ece-d760-52a7-1787.ngrok-free.app",r"^https:\/\/[a-z0-9\-]+\.ngrok-free\.app$",
]
# Allow all origins (for development purposes only)
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", 
     "https://3661-2405-201-c047-c859-8ece-d760-52a7-1787.ngrok-free.app"# Your React app
]
