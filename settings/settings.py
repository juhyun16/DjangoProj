"""
Django settings for multichat project.

Generated by 'django-admin startproject' using Django 1.10.dev20151126161447.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=os.environ.get("SECRET_KEY", "vsecretvv")

# SECURITY WARNING: don't run with debug turned on in production!
# prod.py에서 오버라이딩 해준다.
DEBUG = True

# forwarding 허락할 호스트를 적어준다.
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'chat.apps.ChatConfig',
    'accounts.apps.AccountsConfig',
    'friend.apps.FriendConfig',
    'imagekit',
    'bootstrap3',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

]

ROOT_URLCONF = 'multichat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'multichat.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 언어 설정 변경
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

# time zone 변경
# TIME_ZONE = 'UTC'
TIME_ZONE='Asia/Seoul'


USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')


#   미디어 관련 사항 지정(파일 업로드 할 때 쓴다. ex. 이미지 파일)
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')


#   아래의 항목은 1.8 version부터 deprecated되었음.
#   TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)


'''
from django.contrib.messages import constants
MESSAGE_LEVEL=constants.DEBUG           #   지금부터 debug 레벨의 message를 남길 수 있다.
MESSAGE_TAGS={constants.ERROR : "danger"}
'''

LOGIN_URL="/accounts/login/"
LOGIN_REDIRECT_URL="/"
LOGOUT_REDIRECT_URL=None
AUTH_USER_MODEL="auth.User"
