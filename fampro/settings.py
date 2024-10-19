"""
Django settings for fampro project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sajiththomas231@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'vuijgsiliugfcqvc'  # Your Gmail app password:             
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2oad=x^$a#h60cl&#-d-gq50r0e0h(eqcb!nnifi&ur_d#83=j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['famouspro.onrender.com','127.0.0.1','3.109.203.247',]
# ALLOWED_HOSTS = ['13.200.235.4', 'famousfoodproducts.in', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}




import os
MEDIA_ROOT= os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
ROOT_URLCONF = 'fampro.urls'
TEMPLATES_DIR=os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'fampro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.',
#         'NAME':'famouspro',
#         'USER':'root',
#         'PASSWORD':'',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }



# DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# #         'NAME':'famous',
# #         'USER':'famous_user',
# #         'PASSWORD':'thainS0kPN5DMfmxaIZiIRhJ1qebauZG',
# #         'HOST': 'dpg-cs799h56l47c73941ne0-a.singapore-postgres.render.com',
# #         'PORT': '5432',
# #     }
# # }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Use the PostgreSQL engine
        'NAME': 'famous_y09q',  # The name of your database
        'USER': 'famous_y09q_user',  # Your database username
        'PASSWORD': 'GZwqiG81V91LLlcIajv5gf67auMhu48C',  # Your database password
        'HOST': 'dpg-cs92039u0jms73c41ek0-a.singapore-postgres.render.com',  # The host address of your PostgreSQL server
        'PORT': '5432',  # Default PostgreSQL port
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# Directory where collectstatic will store static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
