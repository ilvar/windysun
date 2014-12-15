# Django settings for villacatalog project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Arcady', 'arcady.chumachenko@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'windy'             # Or path to database file if using sqlite3.
DATABASE_USER = 'windy'             # Not used with sqlite3.
DATABASE_PASSWORD = 'windy'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/zozo/projects/windy/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media-admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'REPLACE IN LOCAL SETTINGS'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'middleware.DomainTransitionMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    '/home/zozo/projects/windy/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',

    'tagging',
    'haystack',
    'tinymce',
    'grappelli',
    'filebrowser',
    'photologue',
    # 'south',
    'fccv',

    'meta',
    'blog',
    'surfblog',
    'enflat',
    'page_blocks',
    )

AKISMET_API_KEY = ""

FCCV_VALIDATORS = (
    'fccv.check_comment_email',
    'fccv.check_comment_ip',
    'fccv.check_comment_link_limit',
    'fccv.check_comment_name',
    'fccv.check_comment_text',
    'fccv.check_comment_url',
    'fccv.check_typepad_antispam',
)

HAYSTACK_SITECONF = 'search_conf'

HAYSTACK_SEARCH_ENGINE = 'whoosh'

HAYSTACK_WHOOSH_PATH = './searchindex'

TEMPLATE_CONTEXT_PROCESSORS  = (
    'django.core.context_processors.csrf',
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'context_processors.path_bits',
    'context_processors.page_blocks',
)

GALLERY_SAMPLE_SIZE = '1'

URL_FILEBROWSER_MEDIA = '/media/filebrowser/'

APPEND_SLASH = False

gettext = lambda s: s

LANGUAGES = (
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
)






TINYMCE_JS_URL = '/media/js/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,filebrowser",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'height':500,
    'relative_urls' : False,

}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = True
TINYMCE_FILEBROWSER = True

try:
    from settings_local import *
except ImportError:
    pass

