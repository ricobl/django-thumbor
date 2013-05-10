# -*- coding: utf-8 -*-

from django.conf import settings

# The host serving the thumbor resized images
THUMBOR_SERVER = getattr(settings, 'THUMBOR_SERVER',
                         'http://localhost:8888').rstrip('/')

# The prefix for the host serving the original images
# This must be a resolvable address to allow thumbor to reach the images
THUMBOR_MEDIA_URL = getattr(settings, 'THUMBOR_MEDIA_URL',
                            'http://localhost:8000/media').rstrip('/')

# The same security key used in the thumbor service to
# match the URL construction
THUMBOR_SECURITY_KEY = getattr(settings, 'THUMBOR_SECURITY_KEY',
                               'MY_SECURE_KEY')

THUMBOR_ARGUMENTS = getattr(settings, 'THUMBOR_ARGUMENTS', {})
