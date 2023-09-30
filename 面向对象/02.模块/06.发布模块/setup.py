from distutils.core import setup

setup (name = "message", # 包名
version = "1.0", # 版本
description = "The code by Blake John.", # 描述
long_description = "Send message and recevie message.", # 完整描述
author = "Blake John", # 作者
author_email = "BlakeJohn.@qq.com", # 作者邮箱
url = "www.BlakeJohn.com", # 作者网站
py_modules = ["message.send_message",
"message.receive_message"])