# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-thumbor',
    version='0.5.5',
    description=(
        'A django application to resize images using the thumbor service'),
    long_description=open('README.rst').read(),
    author=u'Enrico Batista da Luz',
    author_email='rico.bl@gmail.com',
    url='http://github.com/ricobl/django-thumbor/',
    license=(
        'django-thumbor is licensed under the MIT license. '
        'For more information, please see LICENSE file.'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    packages=[
        'django_thumbor',
        'django_thumbor.templatetags',
    ],
    install_requires=(
        'Django>=1.4',
        'libthumbor>=1.2.0',
    ),
    tests_require=(
        'django-nose',
        'mock',
    )
)
