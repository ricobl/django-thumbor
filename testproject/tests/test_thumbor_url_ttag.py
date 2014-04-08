# -*- coding: utf-8 -*-

from mock import patch
from unittest import TestCase
from django.template import Template, Context


class TestThumborURLTTagMock(TestCase):
    url = 'domain.com/path/image.jpg'
    generate_url_path = 'django_thumbor.templatetags.thumbor_tags.generate_url'

    def render(self, arguments):
        source = '{% load thumbor_tags %}{% thumbor_url ' + arguments + ' %}'
        template = Template(source)
        rendered = template.render(Context({'url': self.url}))
        return rendered.strip()

    def test_should_pass_the_image_url_arg_to_the_helper(self):
        with patch(self.generate_url_path) as mock:
            self.render('url')
            mock.assert_called_with(image_url=self.url)

    def test_should_pass_the_custom_server_arg_to_the_helper(self):
        custom_server = "http://localhost:8888/foo"
        with patch(self.generate_url_path) as mock:
            self.render('url thumbor_server="{0}"'.format(custom_server))
            mock.assert_called_with(
                image_url=self.url, thumbor_server=custom_server)

    def test_should_pass_kwargs_to_the_helper(self):
        with patch(self.generate_url_path) as mock:
            self.render('url width=300 height=200')
            mock.assert_called_with(image_url=self.url, width=300, height=200)

    def test_should_convert_colon_separated_filters_to_a_list(self):
        filters = [
            u'watermark(http://domain.com/images/watermark.png,-10,-10,20)',
            u'brightness(10)']
        with patch(self.generate_url_path) as mock:
            self.render('url filters="{0}"'.format(':'.join(filters)))
            mock.assert_called_with(image_url=self.url, filters=filters)
