# -*- coding: utf-8 -*-

from mock import patch
from unittest import TestCase
from django.test.utils import override_settings
from django_thumbor import generate_url, conf


class TestGenerateURL(TestCase):

    url = 'domain.com/path/image.jpg'

    def tearDown(self):
        # Restore changed settings
        reload(conf)

    def assertPassesArgsToCrypto(self, *args, **kwargs):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(*args, **kwargs)
            mock.assert_called_with(*args, **kwargs)

    def test_should_pass_url_arg_to_crypto(self):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(self.url)
            mock.assert_called_with(image_url=self.url)

    def test_should_pass_url_kwarg_to_crypto(self):
        self.assertPassesArgsToCrypto(image_url=self.url)

    def test_should_pass_extra_kwargs_to_crypto(self):
        self.assertPassesArgsToCrypto(
            image_url=self.url, width=300, height=200)

    def test_should_return_the_result(self):
        encrypted_url = 'encrypted-url.jpg'
        encrypted_url_with_host = 'http://localhost:8888/encrypted-url.jpg'

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = encrypted_url
            url = generate_url(self.url)

        self.assertEqual(url, encrypted_url_with_host)

    def test_should_return_the_result_with_a_custom_server(self):
        encrypted_url = 'encrypted-url.jpg'
        custom_server = 'http://localhost:8888/foo'
        encrypted_url_with_host = '{0}/{1}'.format(
            custom_server, encrypted_url)

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = encrypted_url
            url = generate_url(self.url, thumbor_server=custom_server)

        self.assertEqual(url, encrypted_url_with_host)

    def test_should_remove_ending_slash_from_custom_server(self):
        encrypted_url = 'encrypted-url.jpg'
        custom_server = 'http://localhost:8888/foo/'
        encrypted_url_with_host = '{0}{1}'.format(
            custom_server, encrypted_url)

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = encrypted_url
            url = generate_url(self.url, thumbor_server=custom_server)

        self.assertEqual(url, encrypted_url_with_host)

    @override_settings(THUMBOR_ARGUMENTS={'smart': True, 'fit_in': True})
    def test_should_pass_args_from_settings_to_crypto(self):
        reload(conf)
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(image_url=self.url)
            mock.assert_called_with(
                image_url=self.url, smart=True, fit_in=True)

    @override_settings(THUMBOR_ARGUMENTS={'smart': True})
    def test_should_allow_overriding_args_from_settings(self):
        reload(conf)
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(image_url=self.url, smart=False)
            mock.assert_called_with(image_url=self.url, smart=False)


class TestURLFixing(TestCase):

    def assertURLEquals(self, original, expected, **kwargs):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(original, **kwargs)
            mock.assert_called_with(image_url=expected)

    def test_should_prepend_the_domain_to_media_url_images(self):
        self.assertURLEquals('/media/uploads/image.jpg',
                             'localhost:8000/media/uploads/image.jpg')

    def test_should_remove_the_scheme_from_external_images(self):
        self.assertURLEquals('http://some.domain.com/path/image.jpg',
                             'some.domain.com/path/image.jpg')
