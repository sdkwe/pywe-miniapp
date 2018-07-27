# -*- coding: utf-8 -*-

from pywe_base import BaseWechat
from pywe_decrypt import decrypt
from pywe_storage import MemoryStorage


class MiniApp(BaseWechat):
    def __init__(self, appid=None, secret=None, storage=None):
        super(MiniApp, self).__init__()
        self.appid = appid
        self.secret = secret
        self.storage = storage or MemoryStorage()
        # wx.login(OBJECT), Refer: https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-login.html
        # wx.getUserInfo(OBJECT), Refer: https://mp.weixin.qq.com/debug/wxadoc/dev/api/open.html#wxgetuserinfoobject
        self.JSCODE2SESSION = self.API_DOMAIN + '/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type={grant_type}'

    @property
    def sessionKey(self):
        return '{0}:sessionKey'.format(self.appid)

    def update_params(self, appid=None, secret=None, storage=None):
        self.appid = appid or self.appid
        self.secret = secret or self.secret
        self.storage = storage or self.storage

    def get_session_info(self, appid=None, secret=None, code=None, grant_type='authorization_code', storage=None):
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # Fetch sessionInfo
        session_info = self.get(self.JSCODE2SESSION, appid=self.appid, secret=self.secret, code=code, grant_type=grant_type) if code else {}
        # Store sessionKey
        if session_info:
            self.storage.set(self.sessionKey, session_info.get('session_key', ''))
        return session_info

    def get_session_key(self, appid=None, secret=None, code=None, grant_type='authorization_code', storage=None):
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # Fetch sessionKey
        # From storage
        session_key = '' if code else self.storage.get(self.sessionKey)
        # From request api
        if not session_key:
            session_key = get_session_info(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, storage=self.storage).get('session_key', '')
        return session_key

    def get_userinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None, storage=None):
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # If not encryptedData return session_info
        if not encryptedData:
            return get_session_info(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, storage=self.storage)
        # Update sessionKey
        if not session_key:
            session_key = self.get_session_key(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, storage=self.storage)
        return decrypt(appId=self.appid, sessionKey=session_key, encryptedData=encryptedData, iv=iv)

    def get_phone_number(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None, storage=None):
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # If not encryptedData return session_info
        if not encryptedData:
            return get_session_info(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, storage=self.storage)
        # Update sessionKey
        if not session_key:
            session_key = self.get_session_key(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, storage=self.storage)
        return decrypt(appId=self.appid, sessionKey=session_key, encryptedData=encryptedData, iv=iv)


miniapp = MiniApp()
get_session_info = miniapp.get_session_info
get_session_key = miniapp.get_session_key
get_userinfo = miniapp.get_userinfo
get_phone_number = miniapp.get_phone_number
