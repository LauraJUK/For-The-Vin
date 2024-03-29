# Django settings for forthevin project.
import sys, os
import socket
if socket.gethostname() == 'Laura-Johnsons-MacBook.local':
    #Development (Local) Server Settings go here
    DEBUG = TEMPLATE_DEBUG = True
    ADMIN_MEDIA_PREFIX = '/static/admin/'
    TEMPLATE_DIRS = ('/Users/laurajohnson/Documents/Aptana Studio 3 Workspace/forthevin/forthevin/templates/',)
    STATICFILES_DIRS = ('/Users/laurajohnson/Documents/Aptana Studio 3 Workspace/forthevin/forthevin/static/',)
else:
    #Production (Live) Server Settings go here
    DEBUG = TEMPLATE_DEBUG = False
    ADMIN_MEDIA_PREFIX = 'http://forthevin.com/static/admin/'
    TEMPLATE_DIRS = ('/app/forthevin/templates/',)
    STATICFILES_DIRS = ('/app/forthevin/static/',)
    
#DEBUG = True
#TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Laura Johnson', 'laura.lj.johnson@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'forthevin',                      # Or path to database file if using sqlite3.
        'USER': 'laura',                      # Not used with sqlite3.
        'PASSWORD': 'laura1',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

DIRNAME = os.path.abspath(os.path.dirname(__file__))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(DIRNAME,'uploads/')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = ''
STATIC_ROOT = os.path.join(DIRNAME, '/static/')


STATIC_MEDIA_ROOT = os.path.join(DIRNAME, 'static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# I moved this to the top of this file.  
# ADMIN_MEDIA_PREFIX = 'http://forthevin.com/static/admin/'


# Additional locations of static files
# I moved this to the top of this file.
#STATICFILES_DIRS = (
                    # '/Users/laurajohnson/Documents/Aptana Studio 3 Workspace/forthevin/forthevin/static/',
                    # '/app/forthevin/static/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c8cffo+5ow%i4n17o%w1%j4i5ig^!=$pypk=u%wc1$2lg!35-)'

# List of callables that know how to import templates from various sources.
_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request')

ROOT_URLCONF = 'forthevin.urls'

# I moved this to the top of this file.  
# TEMPLATE_DIRS = (
    # '/app/forthevin/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'forthevin.wineries',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
     'south'
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
