# -*- coding: utf-8 -*-

from django import template
from django_thumbor import generate_url

register = template.Library()


@register.simple_tag
def thumbor_url(image_url, **kwargs):
    return generate_url(image_url=image_url, **kwargs)
