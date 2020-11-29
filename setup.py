# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.1.6'


setup(
    name='pywe-miniapp',
    version=version,
    keywords='Wechat Weixin Mini App',
    description='Wechat MiniProgram Module for Python.',
    long_description=open('README.rst').read(),

    url='https://github.com/sdkwe/pywe-miniapp',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pywe_miniapp'],
    py_modules=[],
    install_requires=['pywe_base', 'pywe_decrypt', 'pywe_storage'],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
