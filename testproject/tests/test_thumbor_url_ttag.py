# -*- coding: utf-8 -*-

from mock import patch
from unittest import TestCase
from django.template import Template, Context
from django.test.utils import override_settings
from django_thumbor import conf


class TestThumborURLTTagMock(TestCase):
    url = 'domain.com/path/image.jpg'
    generate_url_path = 'django_thumbor.templatetags.thumbor_tags.generate_url'

    def render(self, arguments):
        source = '{% load thumbor_tags %}{% thumbor_url ' + arguments + ' %}'
        template = Template(source)
        rendered = template.render(Context({'url': self.url}))
        return rendered.strip()

    @override_settings(THUMBOR_ARGUMENTS={})
    def test_should_pass_the_image_url_arg_to_the_helper(self):
        reload(conf)
        with patch(self.generate_url_path) as mock:
            self.render('url')
            mock.assert_called_with(image_url=self.url)

    @override_settings(THUMBOR_ARGUMENTS={})
    def test_should_pass_kwargs_to_the_helper(self):
        reload(conf)
        with patch(self.generate_url_path) as mock:
            self.render('url width=300 height=200')
            mock.assert_called_with(image_url=self.url, width=300, height=200)

    @override_settings(THUMBOR_ARGUMENTS={'smart': True})
    def test_set_smart_on_default_arguments(self):
        reload(conf)
        with patch(self.generate_url_path) as mock:
            print self.render('url width=300 height=200')
            mock.assert_called_with(image_url=self.url, width=300,
                                    height=200, smart=True)

    @override_settings(THUMBOR_ARGUMENTS={'width': 400})
    def test_set_width_400_on_defalt_arguments_and_300_in_templatetag(self):
        reload(conf)
        with patch(self.generate_url_path) as mock:
            print self.render('url width=300 height=200')
            mock.assert_called_with(image_url=self.url, width=300, height=200)

    @override_settings(THUMBOR_ARGUMENTS={'width': 300, 'nose': 40})
    def test_set_more_than_one_attribute_on_defalt_arguments(self):
        reload(conf)
        with patch(self.generate_url_path) as mock:
            print self.render('url')
            mock.assert_called_with(image_url=self.url, width=300, nose=40)
