# pywe-miniapp

Wechat Module for Python for MiniApp.

# Installation

```shell
pip install pywe-miniapp
```

# Usage

```python
from pywe_miniapp import get_session_key, get_userinfo, get_phone_number
```

# Method

```python
def get_session_key(self, appid=None, secret=None, code=None, grant_type='authorization_code', storage=None):

def get_userinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None, storage=None):

def get_phone_number(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None, storage=None):
```

# UserInfo & PhoneNumberInfo
  ```python
  from pywe_miniapp import get_userinfo
  from pywe_storage import RedisStorage

  from utils.redis.connect import r

  # {
  #     u'avatarUrl': u'AVATARURL',
  #     u'city': u'CITY',
  #     u'country': u'CN',
  #     u'gender': 1,
  #     u'language': u'ZH_CN',
  #     u'nickName': u'NICKNAME',
  #     u'openId': u'OPENID',
  #     u'province': u'PROVINCE',
  #     u'unionId': u'UNIONID',
  #     u'watermark': {u'appid': u'APPID', u'timestamp': TIMESTAMP}
  # }
  user_info = get_userinfo(appid=appid, secret=secret, code=code, encryptedData=encryptedData, iv=iv, storage=RedisStorage(r))

  # {
  #     "phoneNumber": "13580006666",
  #     "purePhoneNumber": "13580006666",
  #     "countryCode": "86",
  #     "watermark":
  #         {
  #             "appid": "APPID",
  #             "timestamp": TIMESTAMP
  #         }
  # }
  phone_number_info = get_phone_number(appid=appid, secret=secret, encryptedData=encryptedData, iv=iv, storage=RedisStorage(r))
  ```
