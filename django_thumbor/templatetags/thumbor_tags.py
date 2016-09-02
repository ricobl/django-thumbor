# -*- coding: utf-8 -*-

from django import template
from django_thumbor import generate_url

register = template.Library()

try:
    # Python 2
    STRING_TYPES = (basestring,)
except:
    # Python 3
    STRING_TYPES = (str,)

def _parse_filters(filters):
    # Forces an empty filter to the end of the list
    filters += ':'
    # Splits and restores filter closing parenthesis
    filters = [f + ')' for f in filters.split('):')]
    # Ignores the empty filter at the end
    return filters[:-1]

@register.simple_tag
def thumbor_url(image_url, **kwargs):
    filters = kwargs.get('filters')
    if filters and isinstance(filters, STRING_TYPES):
        kwargs['filters'] = _parse_filters(filters)

    return generate_url(image_url=image_url, **kwargs)
