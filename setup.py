# -*- coding: utf-8 -*-
import os
from setuptools import setup


README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='Clay',
    version='0.3',
    author='Juan-Pablo Scaletti',
    author_email='juanpablo@lucumalabs.com',
    packages=['clay'],
    package_data={'clay': [
            '*.*',
            'skeleton/.gitignore',
            'skeleton/*.*',
            'skeleton/static/*.*',
            'skeleton/static/images/*.*',
            'skeleton/static/scripts/*.*',
            'skeleton/static/styles/*.*',
            'skeleton/views/*.*',
            'views/*.*',
        ]},
    zip_safe=False,
    url='http://github.com/lucuma/Clay',
    license='MIT license (http://www.opensource.org/licenses/mit-license.php)',
    description='A rapid prototyping tool',
    long_description=open(README).read(),
    install_requires=[
        'Shake>=0.11',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points="""
    [console_scripts]
    clay = clay.manage:main
    """
)
