#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-thumbor',
    version='0.2',
    description='A django application to resize images using the thumbor service',
    long_description=open('README.rst').read(),
    author=u'Enrico Batista da Luz',
    author_email='rico.bl@gmail.com',
    url='http://github.com/ricobl/django-thumbor/',
    packages=[
        'django_thumbor',
        'django_thumbor.templatetags',
    ],
    install_requires=(
        'Django>=1.4',
        'libthumbor',
    ),
    tests_require=(
        'django-nose',
        'mock',
    )
)
