# 包（Package）概念
# *包 是一个 包含多个模块 的 特殊目录
# *目录下有一个 特殊的文件 __init__.py
# *包名的 命名方式 和变量名一致，小写字母 + _
# 好处:使用 import 包名 可以一次性导入 包 中 所有的模块

import message

message.send_message.send_message ("Hello")
txt = message.receive_message.receive_message ()
print (txt)