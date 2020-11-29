============
pywe-miniapp
============

Wechat MiniProgram Module for Python.

Installation
============

::

    pip install pywe-miniapp


Usage
=====

::

    from pywe_miniapp import get_session_key, get_userinfo, get_phone_number, get_shareinfo


Method
======

::

    def get_session_key(self, appid=None, secret=None, code=None, grant_type='authorization_code', storage=None):

    def get_userinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None, storage=None):

    def get_phone_number(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None, storage=None):

    def get_shareinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', unid=None, session_key=None, encryptedData=None, iv=None, storage=None):

