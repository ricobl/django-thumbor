django-thumbor
==============

.. image:: https://travis-ci.org/ricobl/django-thumbor.png?branch=master

A django application to resize images using the
`thumbor <https://github.com/globocom/thumbor>`_ service.

Usage
-----

Both ``thumbor_url`` templatetag and the ``generate_url`` helper uses the same
arguments as `libthumbor <https://github.com/heynemann/libthumbor>`_, you can
check the `wiki <https://github.com/heynemann/libthumbor/wiki>`_ for more info.

On templates:

.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% thumbor_url '/media/image.jpg' width=300 %}" width="300" />

On code:

.. code-block:: python

    from django_thumbor import generate_url
    resized = generate_url("/media/image.jpg", width=300)


Installation
------------

.. code-block:: bash

    pip install django-thumbor


Configuration
-------------

Add the app to the ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'django_thumbor',
    )

Here are the default settings that you can override:

.. code-block:: python

    # The host serving the thumbor resized images
    THUMBOR_SERVER = 'http://localhost:8888'

    # The prefix for the host serving the original images
    # This must be a resolvable address to allow thumbor to reach the images
    THUMBOR_MEDIA_URL = 'http://localhost:8000/media'

    # The same security key used in the thumbor service to
    # match the URL construction
    THUMBOR_SECURITY_KEY = 'MY_SECURE_KEY'
