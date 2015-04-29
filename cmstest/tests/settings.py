import os

SILENCED_SYSTEM_CHECKS = ('1_6.W001',)

DEBUG = True
SITE_ID = 1
SECRET_KEY = 'fake-key'
LANGUAGE_CODE = 'en-us'
LANGUAGES = (('en', 'English'),('en-us', 'English'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.environ.get('VIRTUAL_ENV', ''), 'test.sqlite3')
    }
}
ROOT_URLCONF = 'cmstest.testurls'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)
MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'cms',
    'mptt',
    'sekizai',
    'djangocms_admin_style',
    'django.contrib.messages',
    'cmstest',
)
CMS_TEMPLATES = ( ('bogus.html', 'Bogus'), )
