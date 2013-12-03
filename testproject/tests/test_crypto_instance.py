# -*- coding: utf-8 -*-

import imp
from unittest import TestCase
from django_thumbor import crypto, conf
from django.test.utils import override_settings


class TestCryptoInstance(TestCase):

    def test_should_have_a_default_secret_key(self):
        self.assertEqual(crypto.key, 'MY_SECURE_KEY')
        self.assertEqual(crypto.key, conf.THUMBOR_SECURITY_KEY)

    @override_settings(THUMBOR_SECURITY_KEY='custom-security-key')
    def test_should_read_key_from_settings(self):
        imp.reload(conf)
        self.assertEqual(conf.THUMBOR_SECURITY_KEY, 'custom-security-key')
