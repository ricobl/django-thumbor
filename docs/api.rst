API
===

Helpers
-------

generate_url
............

.. autofunction:: django_thumbor.generate_url
.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% thumbor_url '/media/image.jpg' width=300 %}" width="300" />


Templates
---------

thumbor_url
...........

.. autofunction:: django_thumbor.templatetags.thumbor_tags.thumbor_url
.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% thumbor_url '/media/image.jpg' width=300 %}" width="300" />
