============
pywe-miniapp
============

Wechat Module for Python for MiniApp.

Installation
============

::

    pip install pywe-miniapp


Usage
=====

::

    from pywe_miniapp import get_session_key, get_userinfo


Method
======

::

    def get_session_key(self, appid=None, secret=None, code=None, grant_type='authorization_code'):

    def get_userinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None):

