# -*- coding: utf-8 -*-

import os
LOCAL_FILE = lambda *p: os.path.abspath(os.path.join(__file__, '../..', *p))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '_data.db',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
USE_TZ = True
MEDIA_ROOT = LOCAL_FILE('media')
MEDIA_URL = '/media/'
STATIC_ROOT = LOCAL_FILE('staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    LOCAL_FILE('static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'qtn(i0@70^3%pvc-^c6!tuq_d=norv1t_*urp3dqc$%1-ci5y*'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
)

ROOT_URLCONF = 'testproject.urls'
WSGI_APPLICATION = 'testproject.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django_thumbor',
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--nocapture',
    '--nologcapture',
    '--verbosity', '2',
]
