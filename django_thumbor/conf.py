# -*- coding: utf-8 -*-

from django.conf import settings

THUMBOR_SECURITY_KEY = getattr(settings, 'THUMBOR_SECURITY_KEY',
                               'my-security-key')
