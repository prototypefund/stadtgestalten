"""
Django settings for stadt project.

Generated by 'django-admin startproject' using Django 1.9.

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
SECRET_KEY = '_^n8g4hg!u&c9u_+wve-euni)cr-tov*f5k45*akwg@k)a2s+m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'bootstrap3',
    'content',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'entities.apps.EntitiesConfig',
    'rules.apps.AutodiscoverRulesConfig',
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

ROOT_URLCONF = 'stadt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'stadt', 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'content.context_processors.statistics',
                'entities.context_processors.gestalt',
                'entities.context_processors.groups',
                'entities.context_processors.statistics',
                'stadt.context_processors.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'stadt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Authentication backends
# https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#authentication-backends

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'rules.permissions.ObjectPermissionBackend',
]


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/stadt/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# User uploaded files
# https://docs.djangoproject.com/en/1.9/topics/files/

MEDIA_URL = '/stadt/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Email
# https://docs.djangoproject.com/en/1.9/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Sites
# https://docs.djangoproject.com/en/1.9/ref/contrib/sites/

SITE_ID = 1


# Authentication
# http://django-allauth.readthedocs.org/

LOGIN_URL = 'account_login'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_USERNAME_REQUIRED = False


# Crispy forms
# http://django-crispy-forms.readthedocs.org/

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Stadtgestalten
#

ABOUT_GROUP_ID = 2
