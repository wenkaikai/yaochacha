# coding=utf-8
"""
Django settings for yaochacha_formal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4vl^ym0$(rz&tt!)2-2te-d56g85$l9nh42=yaoesc8ll3s)m7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'yaochacha_formal.urls'

WSGI_APPLICATION = 'yaochacha_formal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_ycc',  # 数据库名称
        'USER': 'user_record',  # 数据库用户名
        'PASSWORD': 'rt@#UsRe$',  # 数据库密码
        'HOST': '47.96.162.131',  # 数据库主机，留空默认为localhost
        'PORT': '3306',  # 数据库端口
    },
    '39net': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_39net',  # 数据库名称
        'USER': 'user_record',  # 数据库用户名
        'PASSWORD': 'rt@#UsRe$',  # 数据库密码
        'HOST': '47.96.162.131',  # 数据库主机，留空默认为localhost
        'PORT': '3306',  # 数据库端口
    },
    'apps': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_apps',  # 数据库名称
        'USER': 'user_record',  # 数据库用户名
        'PASSWORD': 'rt@#UsRe$',  # 数据库密码
        'HOST': '47.96.162.131',  # 数据库主机，留空默认为localhost
        'PORT': '3306',  # 数据库端口
    }
}
#为当前项目名称，db_router为上一步编写的db_router.py文件，app02Router为Router
DATABASE_ROUTERS = ['yaochacha_formal.db_router.app01Router', 'yaochacha_formal.db_router.app02Router']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_PATH), 'static')
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ("website", os.path.join(STATIC_ROOT, 'website')),

)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages"
)