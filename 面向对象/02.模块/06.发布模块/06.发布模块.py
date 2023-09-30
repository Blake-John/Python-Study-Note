# 1.创建 setup.py
# * setup.py 的文件

# ```python
# from distutils.core import setup

# setup(name="hm_message",  # 包名
#       version="1.0",  # 版本
#       description="itheima's 发送和接收消息模块",  # 描述信息
#       long_description="完整的发送和接收消息模块",  # 完整描述信息
#       author="itheima",  # 作者
#       author_email="itheima@itheima.com",  # 作者邮箱
#       url="www.itheima.com",  # 主页
#       py_modules=["hm_message.send_message",
#                   "hm_message.receive_message"])
# ```

# 有关字典参数的详细信息，可以参阅官方网站： https://docs.python.org/2/distutils/apiref.html

# 2.构建模块

# ```bash
# $ python3 setup.py build
# ```

# 3.生成发布压缩包

# ```bash
# $ python3 setup.py sdist
# ```

# > 注意：要制作哪个版本的模块，就使用哪个版本的解释器执行！