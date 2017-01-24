# -*- coding: utf-8 -*-

from pywe_base import BaseWechat
from pywe_decrypt import decrypt


class MiniApp(BaseWechat):
    def __init__(self):
        super(MiniApp, self).__init__()
        # wx.login(OBJECT), Refer: https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-login.html
        # wx.getUserInfo(OBJECT), Refer: https://mp.weixin.qq.com/debug/wxadoc/dev/api/open.html#wxgetuserinfoobject
        self.JSCODE2SESSION = self.API_DOMAIN + '/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type={grant_type}'

    def get_session_key(self, appid=None, secret=None, code=None, grant_type='authorization_code'):
        return self.get(self.JSCODE2SESSION, appid=appid, secret=secret, code=code, grant_type=grant_type)

    def get_userinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None):
        if not session_key:
            session_key = self.get_session_key(appid=appid, secret=secret, code=code, grant_type=grant_type).get('session_key', '')
        return decrypt(appId=appid, sessionKey=session_key, encryptedData=encryptedData, iv=iv)


miniapp = MiniApp()
get_session_key = miniapp.get_session_key
get_userinfo = miniapp.get_userinfo
