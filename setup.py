# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='django-geolocation-alert',
    version='0.1',
    description=('Geolocation django middleware that check if user IP'
                 ' or agent browser change during session time.'),
    long_description=readme(),
    keywords='django-geolocation-alert',
    url='https://github.com/lkolacz/django-geolocation-alert.git',
    author='Leszek Andrzej Kołacz',
    author_email='lkolacz@gmail.com',
    license='MIT',
    packages=['geolocation'],
    zip_safe=False
)
