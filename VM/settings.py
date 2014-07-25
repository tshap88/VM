"""
Django settings for VM project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bv8kcy9-2*=ixe*jd+ha*u+i7zu7yodn=6sd)yj!+&2xx#gkkw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = '/home/tania/PycharmProjects/VM/sites/media/'

MEDIA_URL = '/media/'

STATIC_ROOT = ' '#'/home/tania/PycharmProjects/VM//sites/static/'

STATIC_URL = '/static/'

DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')
MEDIA_ROOT = getattr(settings, "FILEBROWSER_MEDIA_ROOT", settings.MEDIA_ROOT)
MEDIA_URL = getattr(settings, "FILEBROWSER_MEDIA_URL", settings.MEDIA_URL)
FILEBROWSER_DIRECTORY = MEDIA_ROOT
#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = '/media-admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    '/home/tania/PycharmProjects/VM/sites/static',

    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'disqus',
    'news',
    'django.contrib.sites',
)

DISQUS_API_KEY = 'ICgFGEuqMakHCxKobko9rGTzMz5x6vD1V7R4hk9T29DxYCmucdw2VD9zWwHdz3YM'
DISQUS_WEBSITE_SHORTNAME = 'vm4game'
SITE_ID = 1


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'VM.urls'

WSGI_APPLICATION = 'VM.wsgi.application'

TEMPLATE_DIRS = (
     '/home/tania/PycharmProjects/VM/VM/templates'
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'VM',
	    'USER': 'root',
        'PASSWORD': 'wxyiw370',
        'HOST': '',
        'PORT': '',

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
