# -*- coding: utf-8 -*-

from mock import patch
from unittest import TestCase
from django.template import Template, Context


@patch('django_thumbor.templatetags.thumbor_tags.generate_url')
class TestThumborURLTTagMock(TestCase):
    url = 'domain.com/path/image.jpg'
    generate_url_path = 'django_thumbor.templatetags.thumbor_tags.generate_url'

    def render(self, arguments, context=None):
        source = '{% load thumbor_tags %}{% thumbor_url ' + arguments + ' %}'
        template = Template(source)
        context = context or {}
        context = dict({'url': self.url}, **context)
        rendered = template.render(Context(context))
        return rendered.strip()

    def test_should_pass_the_image_url_arg_to_the_helper(self, generate_url):
        self.render('url')
        generate_url.assert_called_with(image_url=self.url)

    def test_should_pass_the_custom_server_arg_to_the_helper(self, generate_url):
        custom_server = "http://localhost:8888/foo"
        self.render('url thumbor_server="{0}"'.format(custom_server))
        generate_url.assert_called_with(
            image_url=self.url, thumbor_server=custom_server)

    def test_should_pass_kwargs_to_the_helper(self, generate_url):
        self.render('url width=300 height=200')
        generate_url.assert_called_with(image_url=self.url, width=300, height=200)

    def test_should_convert_colon_separated_filters_to_a_list(self, generate_url):
        filters = [
            u'watermark(http://domain.com/images/watermark.png,-10,-10,20)',
            u'brightness(10)']
        self.render('url filters="{0}"'.format(':'.join(filters)))
        generate_url.assert_called_with(image_url=self.url, filters=filters)

    def test_should_accept_filters_from_a_list(self, generate_url):
        filters = [
            u'watermark(http://domain.com/images/watermark.png,-10,-10,20)',
            u'brightness(10)']
        self.render(
            'url filters=filters'.format(':'.join(filters)),
            context={'filters': filters})
        generate_url.assert_called_with(image_url=self.url, filters=filters)
