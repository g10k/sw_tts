"""
Django settings for sw_tts project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1^xn16c_l*5+ko)_#nrue-+as1@jowgr1+e%0y4fk@#rd%*j)3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_swagger',
    'rest_framework',
    'django_speach_synthesizer',
    'core',
    'social.apps.django_app.default',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sw_tts.urls'

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
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.request',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'sw_tts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('frontend', os.path.join(BASE_DIR, 'frontend')),
)
LANGUAGE_CODE = 'ru-Ru'


OUTPUT_DIR = os.path.join(BASE_DIR, 'generated')
MAX_SOUND_LIFE = 60*60*12   # seconds of sound file storing


SOCIAL_AUTH_VK_OPENAPI_ID = '5596606'
SOCIAL_AUTH_VK_APP_SECRET = 'jBx8nnH7pzevq7UA3hH0'
SOCIAL_AUTH_VK_APP_USER_MODE = 2

VK_APP_ID = '5596606'
VKONTAKTE_APP_ID = VK_APP_ID
VK_API_SECRET = 'jBx8nnH7pzevq7UA3hH0'
VKONTAKTE_APP_SECRET = VK_API_SECRET

SOCIAL_AUTH_VK_OAUTH2_KEY = '5596606'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'jBx8nnH7pzevq7UA3hH0'


AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.vk.VKOAuth2',
    'social.backends.vk.VKontakteOpenAPI',
    'social.backends.yandex.YaruOAuth2',
    'social.backends.yandex.YandexOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_URL_NAMESPACE = 'social'
# SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'

try:
    from sw_tts.local_settings import *
except ImportError:
    print("Warning: no local_settings.py")