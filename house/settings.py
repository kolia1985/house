import os, sys
import logging

# Dummy ``ugettext`` function
_ = ugettext = lambda s: s

# Get absolute path for current directory
DIRNAME = os.path.dirname(__file__)

INTERNAL_IPS = ('127.0.0.1',)

# Insert parent and lib dirs to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(DIRNAME, '..')))
sys.path.insert(0, os.path.abspath(os.path.join(DIRNAME, '../lib')))
sys.path.insert(0, os.path.abspath(DIRNAME))

# Accounts settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/'

# Database settings
# Please, set up proper values in ``settings_local.py`` file
DATABASE_ENGINE = 'sqlite3'
DATABASE_HOST = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_NAME = ':memory:'
DATABASE_PORT = ''

# Debug settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Email settings
# Please, set up proper email settings in ``settings_local.py`` file
DEFAULT_FROM_EMAIL = 'mail@localhost'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = 'root@localhost'

import time
TIME_ZONE = time.tzname[0]

# Installed applications
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'house.material',
    'house.core',
    'house.foundation',
    'house.overlay',
    'house.roof',
    'house.utils',
    'house.wall',
    'house.sortedtable',
)


# Locale settings
USE_I18N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
)

# Middleware settings
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)



# Template settings
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

# Other **Django** related settings
ROOT_URLCONF = 'house.urls'


# **Registration** settings
# The number of days activation keys will remain valid after an account is
# registered.
ACCOUNT_ACTIVATION_DAYS = 30
AUTH_PROFILE_MODULE = 'accounts.UserProfile'

AUTOCOMPLETE_PRETTIFY = {
    'geo.city': lambda obj: u'%s' % (obj.name),
}

AUTOCOMPLETE_RELATED_FIELDS = {
    'geo.city': ['state', ],
    'geo.state': ['country', ],
}

# Trying to load settings located in ``settings_local.py`` file
try:
    from settings_local import *
except ImportError, e:
    logging.exception(e)
    pass

IMPORT_ROOT = os.path.join(MEDIA_ROOT, "importdata")

CONTACT_EMAIL = 'email@email.email'
