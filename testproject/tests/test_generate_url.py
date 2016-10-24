# -*- coding: utf-8 -*-

import imp
from mock import patch
from unittest import TestCase
from django.test.utils import override_settings
from django_thumbor import generate_url, conf


URL = 'domain.com/path/image.jpg'
ALIASES = {
    'thumb-square': {
        'width': 300,
        'height': 300,
        'filters': ['brightness(10)']}
}


class MockImageField():
    @property
    def url(self):
        return URL


class TestGenerateURL(TestCase):
    def tearDown(self):
        # Restore changed settings
        imp.reload(conf)

    def assertPassesArgsToCrypto(self, *args, **kwargs):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(*args, **kwargs)
            mock.assert_called_with(*args, **kwargs)

    def test_should_pass_url_arg_to_crypto(self):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(URL)
            mock.assert_called_with(image_url=URL)

    def test_should_pass_url_kwarg_to_crypto(self):
        self.assertPassesArgsToCrypto(image_url=URL)

    def test_should_pass_extra_kwargs_to_crypto(self):
        self.assertPassesArgsToCrypto(
            image_url=URL, width=300, height=200)

    def test_should_return_the_result(self):
        encrypted_url = 'encrypted-url.jpg'
        encrypted_url_with_host = 'http://localhost:8888/encrypted-url.jpg'

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = encrypted_url
            url = generate_url(URL)

        self.assertEqual(url, encrypted_url_with_host)

    def test_should_return_the_result_with_a_custom_server(self):
        encrypted_url = 'encrypted-url.jpg'
        custom_server = 'http://localhost:8888/foo'
        encrypted_url_with_host = '{0}/{1}'.format(
            custom_server, encrypted_url)

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = encrypted_url
            url = generate_url(URL, thumbor_server=custom_server)

        self.assertEqual(url, encrypted_url_with_host)

    def test_should_pass_the_image_with_url_param(self):
        image_mock = MockImageField()
        encrypted_url = image_mock.url
        custom_server = 'http://localhost:8888/foo'
        encrypted_url_with_host = '{0}/{1}'.format(
            custom_server, encrypted_url)

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = image_mock.url
            url = generate_url(image_mock, thumbor_server=custom_server)

        self.assertEqual(url, encrypted_url_with_host)

    def test_should_pass_empty_url(self):
        encrypted_url = ""
        custom_server = 'http://localhost:8888/foo'
        encrypted_url_with_host = '{0}/{1}'.format(
            custom_server, encrypted_url)

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = ""
            url = generate_url(mock.return_value, thumbor_server=custom_server)

        self.assertEqual(url, encrypted_url_with_host)

    def test_should_remove_ending_slash_from_custom_server(self):
        encrypted_url = 'encrypted-url.jpg'
        custom_server = 'http://localhost:8888/foo/'
        encrypted_url_with_host = '{0}{1}'.format(
            custom_server, encrypted_url)

        with patch('django_thumbor.crypto.generate') as mock:
            mock.return_value = encrypted_url
            url = generate_url(URL, thumbor_server=custom_server)

        self.assertEqual(url, encrypted_url_with_host)

    @override_settings(THUMBOR_ARGUMENTS={'smart': True, 'fit_in': True})
    def test_should_pass_args_from_settings_to_crypto(self):
        imp.reload(conf)
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(image_url=URL)
            mock.assert_called_with(
                image_url=URL, smart=True, fit_in=True)

    @override_settings(THUMBOR_ARGUMENTS={'smart': True})
    def test_should_allow_overriding_args_from_settings(self):
        imp.reload(conf)
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(image_url=URL, smart=False)
            mock.assert_called_with(image_url=URL, smart=False)

    @override_settings(THUMBOR_ALIASES=ALIASES)
    def test_should_apply_alias(self):
        imp.reload(conf)
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(image_url=URL, alias='thumb-square')
            mock.assert_called_with(
                image_url=URL, width=300, height=300,
                filters=['brightness(10)'])

    def test_should_raise_with_nonexistent_alias(self):
        imp.reload(conf)
        with self.assertRaises(RuntimeError):
            generate_url(image_url=URL, alias='thumb-square')


class TestURLFixing(TestCase):

    def assertURLEquals(self, original, expected, **kwargs):
        with patch('django_thumbor.crypto.generate') as mock:
            generate_url(original, **kwargs)
            mock.assert_called_with(image_url=expected)

    def test_should_prepend_the_domain_to_media_url_images(self):
        self.assertURLEquals('/media/uploads/image.jpg',
                             'localhost:8000/media/uploads/image.jpg')

    def test_should_prepend_the_domain_to_static_url_images(self):
        conf.THUMBOR_STATIC_ENABLED = True
        self.assertURLEquals('/static/uploads/image.jpg',
                             'localhost:8000/static/uploads/image.jpg')

    @override_settings(MEDIA_URL="")
    def test_should_not_prepend_media_url_if_none_is_set(self):
        self.assertURLEquals('http://www.domain.com/media/uploads/image.jpg', 'www.domain.com/media/uploads/image.jpg')

    @override_settings(STATIC_URL="")
    def test_should_not_prepend_static_url_if_none_is_set(self):
        self.assertURLEquals('http://www.domain.com/static/uploads/image.jpg', 'www.domain.com/static/uploads/image.jpg')

    def test_should_remove_the_scheme_from_external_images(self):
        self.assertURLEquals('http://some.domain.com/path/image.jpg',
                             'some.domain.com/path/image.jpg')
