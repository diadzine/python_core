# -*- coding: utf-8 -*-
"""
Django settings for python_core project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CURRENT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


APPEND_SLASH = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_ku#6yqh7op83jgr^s_2qf^8^#w)v1*q67c*#l#4ey7fn4bu7+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*.tooski.ch', '*.webfaction.com']

ADMINS = (
    ('Sebastien Arnold', 'seba-1511@hotmail.com'),
    # ('Your Name', 'your_email@example.com'),
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Additionnal Apps
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    "pageviews",
    # Custom Apps
    'news',
    'users',
    'pages',
    'blogs',
    'ads',
    'rankings',
    'pictures',
    'skiclubs',
    'widgets',
    'angulation',
    'multiselectfield',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Django Pageviews:
    "pageviews.middleware.PageViewsMiddleware",

    # Django Cors:
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'python_core.urls'

WSGI_APPLICATION = 'python_core.wsgi.application'

AUTH_USER_MODEL = 'users.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
    #
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'db_tooski',
    #     'USER': 'application',
    #     'PASSWORD': '<db_password>',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }
}

# Cache
CACHE_BACKEND = 'dummy:///'

# URLs
ROOT_URLCONF = 'python_core.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-ch'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'spider': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'spider': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'spider'),
            'when': 'midnight',
            'formatter': 'spider',
            'backupCount': 5,
        },
    },
    'loggers': {
        'dev': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'spider': {
            'handlers': ['console', 'spider'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


ADS_PLACEHOLDERS = (
    ('actu-top', "Page Actu, haut de page"),
    ('actu-side', "Page Actu, colonne droite"),
    ('actu-bottom', "Page Actu, base de page"),
    ('results-top', "Pages Résultats, haut de page"),
    ('results-side', "Pages Résultats, colonne droite"),
    ('results-bottom', "Pages Résultats, base de page"),
    ('blog-top', "Pages Blog, haut de page"),
    ('blog-side', "Pages Blog, colonne droite"),
    ('blog-bottom', "Pages Blog, base de page"),
    ('shop-top', "Page Angulation, haut de page"),
    ('shop-bottom', "Page Angulation, base de page"),
    ('sponsors-top', "Page Mentors & Sponsors, haut de page"),
    ('sponsors-side', "Page Mentors & Sponsors, colonne droite"),
    ('sponsors-bottom', "Page Mentors & Sponsors, base de page"),
)
