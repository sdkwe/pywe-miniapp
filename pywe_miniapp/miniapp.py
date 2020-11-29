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
        # wx.login(Object object), Refer: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html
        # wx.getUserInfo(Object object), Refer: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserInfo.html
        # wx.getShareInfo(Object object), Refer: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.getShareInfo.html
        self.JSCODE2SESSION = self.API_DOMAIN + '/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type={grant_type}'

    def sessionKey(self, unid=None):
        # https://developers.weixin.qq.com/community/develop/doc/00088a409fc308b765475fa4351000?highLine=session_key
        # sessionKey 非共用
        return '{0}:{1}:sessionKey'.format(self.appid, unid or '')

    def update_params(self, appid=None, secret=None, storage=None):
        self.appid = appid or self.appid
        self.secret = secret or self.secret
        self.storage = storage or self.storage

    def store_session_key(self, appid=None, secret=None, session_key=None, unid=None, storage=None):
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # Store sessionKey
        return self.storage.set(self.sessionKey(unid=unid), session_key)

    def get_session_info(self, appid=None, secret=None, code=None, grant_type='authorization_code', unid=None, storage=None):
        """
        // 正常返回的JSON数据包
        {
            "openid": "OPENID",
            "session_key": "SESSIONKEY",
        }

        // 满足UnionID返回条件时，返回的JSON数据包
        {
            "openid": "OPENID",
            "session_key": "SESSIONKEY",
            "unionid": "UNIONID"
        }
        // 错误时返回JSON数据包(示例为Code无效)
        {
            "errcode": 40029,
            "errmsg": "invalid code"
        }
        """
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # Fetch sessionInfo
        session_info = self.get(self.JSCODE2SESSION, appid=self.appid, secret=self.secret, code=code, grant_type=grant_type) if code else {}
        # Store sessionKey
        if session_info and unid:
            self.storage.set(self.sessionKey(unid=unid), session_info.get('session_key', ''))
        return session_info

    def get_session_key(self, appid=None, secret=None, code=None, grant_type='authorization_code', unid=None, storage=None, only_frorage=False):
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # Only get sessionKey from storage
        if only_frorage:
            return self.storage.get(self.sessionKey(unid=unid))
        # Fetch sessionKey
        # From storage
        session_key = '' if code or not unid else self.storage.get(self.sessionKey(unid=unid))
        # From request api
        if not session_key:
            session_key = self.get_session_info(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, storage=self.storage).get('session_key', '')
        return session_key

    def get_userinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', unid=None, session_key=None, encryptedData=None, iv=None, storage=None):
        """
        {
            "avatarUrl": "avatarUrl",
            "city": "city",
            "country": "country",  # CN
            "gender": gender,  # 0 or 1
            "language": "language",  # zh_CN
            "nickName": "nickName",
            "openId": "openId",
            "province": "province",
            "unionId": "unionId",
            "watermark": {
                "appid": "appid",
                "timestamp": timestamp  # 1477314187
            }
        }
        """
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # If not encryptedData return session_info
        if not encryptedData:
            return self.get_session_info(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, unid=unid, storage=self.storage)
        # Update sessionKey
        if not session_key:
            session_key = self.get_session_key(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, unid=unid, storage=self.storage)
        return decrypt(appId=self.appid, sessionKey=session_key, encryptedData=encryptedData, iv=iv)

    def get_phone_number(self, appid=None, secret=None, code=None, grant_type='authorization_code', unid=None, session_key=None, encryptedData=None, iv=None, storage=None):
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # If not encryptedData return session_info
        if not encryptedData:
            return self.get_session_info(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, unid=unid, storage=self.storage)
        # Update sessionKey
        if not session_key:
            session_key = self.get_session_key(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, unid=unid, storage=self.storage)
        return decrypt(appId=self.appid, sessionKey=session_key, encryptedData=encryptedData, iv=iv)

    def get_shareinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', unid=None, session_key=None, encryptedData=None, iv=None, storage=None):
        """
        {
            "openGId": "OPENGID"
        }
        """
        # Update params
        self.update_params(appid=appid, secret=secret, storage=storage)
        # If not encryptedData return session_info
        if not encryptedData:
            return self.get_session_info(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, unid=unid, storage=self.storage)
        # Update sessionKey
        if not session_key:
            session_key = self.get_session_key(appid=self.appid, secret=self.secret, code=code, grant_type=grant_type, unid=unid, storage=self.storage)
        return decrypt(appId=self.appid, sessionKey=session_key, encryptedData=encryptedData, iv=iv)


miniapp = MiniApp()
store_session_key = miniapp.store_session_key
get_session_info = miniapp.get_session_info
get_session_key = miniapp.get_session_key
get_userinfo = miniapp.get_userinfo
get_phone_number = miniapp.get_phone_number
get_shareinfo = miniapp.get_shareinfo
