# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='django-geolocation-alert',
    version='0.5.1',
    description=('Geolocation django middleware that check if user IP'
                 ' or agent browser change during session time.'),
    long_description=readme(),
    keywords='django geolocation middleware alert session hash IP agent browser',
    url='https://github.com/lkolacz/django-geolocation-alert.git',
    author='Leszek Andrzej Kołacz',
    author_email='lkolacz@gmail.com',
    license='MIT',
    packages=['geolocation'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
        'Topic :: System :: Monitoring',
    ],
)
