import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-hc^-dz#z2=ilnsh&v^(2^ddt3oc@@!#v8b5(9!)!f5ml9@(+fo'

DEBUG = True

ALLOWED_HOSTS = []

BASE_URL = 'http://127.0.0.1:8000'

INSTALLED_APPS = [
    'user_images.apps.UserImagesConfig',
    'user_accounts.apps.UserAccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ImageTierApi.urls'

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

WSGI_APPLICATION = 'ImageTierApi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# UserAccount model settings.
USER_ACCOUNT_NAME_MAX_LENGTH = 100
USER_ACCOUNT_SURNAME_MAX_LENGTH = 100
USER_ACCOUNT_USERNAME_MAX_LENGTH = 50
USER_ACCOUNT_USERNAME_UNIQUE = True
USER_ACCOUNT_TIER_MAX_LENGTH = 20


# UserImage model settings.
USER_IMAGE_USER_RELATED_NAME = 'images'
USER_IMAGE_IMAGE_UPLOAD_TO = 'images/'
USER_IMAGE_FORMAT_MAX_LENGTH = 10
USER_IMAGE_FORMAT_BLANK = True
USER_IMAGE_WIDTH_BLANK = True
USER_IMAGE_WIDTH_NULL = True
USER_IMAGE_HEIGHT_BLANK = True
USER_IMAGE_HEIGHT_NULL = True
USER_IMAGE_EXPIRE_LINK_TOKEN_MAX_LENGTH = 255
USER_IMAGE_EXPIRE_LINK_TOKEN_BLANK = True


# ThumbnailImage model settings.
USER_IMAGE_IMAGE_THUMBNAIL_UPLOAD_TO = 'images/thumbnails/'


TIER_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise'),
    ]
