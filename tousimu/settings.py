import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 環境変数は3改装上のファイルに記載
ENV_BASE_DIR = environ.Path(__file__) - 3
env = environ.Env()
env_file = str((ENV_BASE_DIR).path('.tousimu_env'))
env.read_env(env_file)

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['tousimu.work']

# sitesフレームを有効化し、管理サイトで編集可能になる。
SITE_ID = 1

GOOGLE_ANALYTICS_TRACKING_ID = 'UA-138975190-2'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simulators',
    'django_cleanup',  # 余分なファイルを削除
    'bootstrap4',
    'django.contrib.sites',
    'django.contrib.sitemaps'
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

ROOT_URLCONF = 'tousimu.urls'

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
                'tousimu.context_processors.google_analytics',  # 自作のcontext_processors
            ],
            'builtins':[
                'bootstrap4.templatetags.bootstrap4',
            ],

        },
    },
]

WSGI_APPLICATION = 'tousimu.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/usr/share/nginx/html/media'

try:
    from .local_settings import *
except ImportError:
    pass
