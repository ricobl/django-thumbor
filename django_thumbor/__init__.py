# -*- coding: utf-8 -*-

from libthumbor import CryptoURL
from django_thumbor import conf

crypto = CryptoURL(key=conf.THUMBOR_SECURITY_KEY)

def generate_url(image_url, **kwargs):
    return crypto.generate(image_url=image_url, **kwargs)

