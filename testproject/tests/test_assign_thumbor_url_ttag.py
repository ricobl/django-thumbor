# -*- coding: utf-8 -*-

from mock import patch
from unittest import TestCase
from django.template import Template, Context


@patch('django_thumbor.templatetags.thumbor_tags.generate_url')
class TestThumborURLTTagMock(TestCase):
    url = 'domain.com/path/image.jpg'

    def test_should_assign_result_to_variable(self, generate_url):
        dummy_url = "generated.url"
        generate_url.return_value = dummy_url
        source = '''
            {% load thumbor_tags %}
            {% assign_thumbor_url image_url=url as thumb_url %}
            <<{{ thumb_url }}>>'''

        template = Template(source)
        context = dict({'url': self.url})
        rendered = template.render(Context(context)).strip()
        self.assertEqual(rendered, '<<{}>>'.format(dummy_url))
