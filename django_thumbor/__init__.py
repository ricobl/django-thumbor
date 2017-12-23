# -*- coding: utf-8 -*-

from libthumbor import CryptoURL
from django_thumbor import conf
from django.conf import settings
from django.core.files.storage import default_storage
import logging
import re
logger = logging.getLogger(__name__)


crypto = CryptoURL(key=conf.THUMBOR_SECURITY_KEY)


def _remove_prefix(url, prefix):
    if url.startswith(prefix):
        return url[len(prefix):]
    return url


def _remove_schema(url):
    return _remove_prefix(url, 'http://')


# Deny empty or none url
def _handle_empty(url):
    if not url:
        logger.error("Empty URL. Skipping.")
        return ""
    return url


# Ensure we always have an absolute URL that Thumbor can resolve.
def _handle_relative(url):
    # Assume that URLs not beginning with a forward slash or scheme are names
    # to be used with the default storage class. We check this first, because
    # the storage class might return a relative URL that needs further
    # processing.
    if not re.match(r'^(/|https?://)', url):
        url = default_storage.url(url)
    # Return absolute URLs as-is.
    if re.match(r'^https?://', url):
        return url
    # We don't have access to a request object, so we have to assume that
    # protocol relative URLs will be available to Thumbor over HTTP.
    if url.startswith('//'):
        return 'http:' + url
    # Prefix path relative URLs with the root URL from settings. We check this
    # after protocol relative URLs, because path relative URLs will match both
    # tests.
    if url.startswith('/'):
        return '%s/%s' % (conf.THUMBOR_ROOT_URL, url.lstrip('/'))
    assert False, (
        'This should never happen. Something has gone wrong while handling a '
        'relative URL.')


# Accept string url and ImageField or similars classes
# with "url" attr as param
def _handle_url_field(url):
    if hasattr(url, "url"):
        return getattr(url, "url", "")
    return url


def generate_url(image_url, alias=None, **kwargs):
    image_url = _handle_empty(image_url)
    image_url = _handle_url_field(image_url)
    image_url = _handle_relative(image_url)
    image_url = _remove_schema(image_url)

    if alias:
        if alias not in conf.THUMBOR_ALIASES:
            raise RuntimeError(
                'Alias "{}" not found in alias map THUMBOR_ALIASES. '
                'Only found these: {}'
                .format(alias, ", ".join(conf.THUMBOR_ALIASES.keys())))
        alias_args = conf.THUMBOR_ALIASES[alias]
    else:
        alias_args = {}

    final_args = dict(conf.THUMBOR_ARGUMENTS)
    final_args.update(alias_args)
    final_args.update(kwargs)

    thumbor_server = final_args.pop(
        'thumbor_server', conf.THUMBOR_SERVER).rstrip('/')

    encrypted_url = crypto.generate(
        image_url=image_url,
        **final_args).strip('/')

    return '%s/%s' % (thumbor_server, encrypted_url)
