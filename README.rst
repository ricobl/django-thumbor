django-thumbor
==============

.. image:: https://travis-ci.org/ricobl/django-thumbor.png?branch=master
    :target: https://travis-ci.org/ricobl/django-thumbor
    :alt: CI status on Travis CI

.. image:: https://pypip.in/v/django-thumbor/badge.png
    :target: https://crate.io/packages/django-thumbor/
    :alt: Latest django-thumbor PyPI version


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

    # Default arguments passed to the `generate_url` helper or
    # the `thumbor_url` templatetag
    THUMBOR_ARGUMENTS = {}


Contributing
------------

Install
.......

Fork, clone, create a virtualenv and run:

.. code-block:: bash

    git clone git://github.com/ricobl/django-thumbor.git
    mkvirtualenv django-thumbor
    make install

Test
....

Add tests on ``testproject/tests``, add code and run:

.. code-block:: bash

    make test
