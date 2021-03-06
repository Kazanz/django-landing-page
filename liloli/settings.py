import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project Apps
    'liloli',
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

ROOT_URLCONF = 'liloli.urls'

WSGI_APPLICATION = 'liloli.wsgi.application'


############
# DATABASE #
############


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#############
# TEMPLATES #
#############


TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


##########
# STATIC #
##########

# url prefix for user uploaded files, stuff that django has to serve directly
MEDIA_URL = '/media/'
# url prefix for static files like css, js, images
STATIC_URL = '/static/'
# url prefix for *static* /admin media
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
# path to django-served media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# path used for collectstatic, *where the webserver not django will expect to find files*
STATIC_ROOT = os.path.join(BASE_DIR, 'public/')
# path to directories containing static files for django project, apps, etc, css/js
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

############
# MESSAGES #
############

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


import warnings
import exceptions
warnings.filterwarnings("ignore", category=exceptions.RuntimeWarning, module='django.db.backends.sqlite3.base', lineno=53)

###########
# TESTING #
###########

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#########################
# LOCAL SETTINGS LOADER #
#########################

DEBUG_APPS = None
try:
    from liloli.local_settings import *
except ImportError:
    pass

try:
    INSTALLED_APPS += DEBUG_APPS
except:
    pass
