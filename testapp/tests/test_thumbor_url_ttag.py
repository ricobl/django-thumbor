# -*- coding: utf-8 -*-

from mock import patch
from unittest import TestCase
from django.template import Template, Context

class TestThumborURLTTagMock(TestCase):

    url = 'domain.com/path/image.jpg'

    def render(self, arguments):
        source = '{% load thumbor_tags %}{% thumbor_url ' + arguments + ' %}'
        template = Template(source)
        rendered = template.render(Context({'url': self.url}))
        return rendered.strip()

    def test_should_pass_the_image_url_arg_to_the_helper(self):
        with patch('django_thumbor.templatetags.thumbor_tags.generate_url') as mock:
            self.render('url')
            mock.assert_called_with(image_url=self.url)

    def test_should_pass_kwargs_to_the_helper(self):
        with patch('django_thumbor.templatetags.thumbor_tags.generate_url') as mock:
            self.render('url width=300 height=200')
            mock.assert_called_with(image_url=self.url, width=300, height=200)
