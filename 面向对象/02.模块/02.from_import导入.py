# *如果希望 从某一个模块 中，导入 部分 工具，就可以使用 from ... import 的方式
# *import 模块名 是 一次性 把模块中 所有工具全部导入，并且通过 模块名/别名 访问

# # 从 模块 导入 某一个工具
# from 模块名1 import 工具名

# *导入之后
#   *不需要 通过 模块名.
#   *可以直接使用 模块提供的工具 —— 全局变量、函数、类

# 注意
# > 如果 两个模块，存在 同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数
# *开发时 import 代码应该统一写在 代码的顶部，更容易及时发现冲突
# *一旦发现冲突，可以使用 as 关键字 给其中一个工具起一个别名

# # 从 模块 导入 所有工具
# from 模块名1 import *

# 注意
# > 这种方式不推荐使用，因为函数重名并没有任何的提示，出现问题不好排查

from test_module_1 import Dog
from test_module_2 import say_hello as Say2
from test_module_1 import say_hello # 若有同名函数，后导入模块的函数会覆盖先导入模块的函数

dog = Dog ()
print (dog)
say_hello ()
Say2 ()