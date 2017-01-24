# pywe-miniapp

Wechat Module for Python for MiniApp.

# Installation

```shell
pip install pywe-miniapp
```

# Usage

```python
from pywe_miniapp import get_session_key, get_userinfo
```

# Method

```python
def get_session_key(self, appid=None, secret=None, code=None, grant_type='authorization_code'):

def get_userinfo(self, appid=None, secret=None, code=None, grant_type='authorization_code', session_key=None, encryptedData=None, iv=None):
```

# Usage

* Get Userinfo for Mini App
  ```python
  from pywe_miniapp import get_userinfo

  userinfo = get_userinfo(appid=appid, secret=secret, code=code, encryptedData=encryptedData, iv=iv)
  ```
