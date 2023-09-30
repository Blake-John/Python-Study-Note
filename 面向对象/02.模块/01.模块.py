# > 模块是 Python 程序架构的一个核心概念
# *每一个以扩展名 py 结尾的 Python源代码文件都是一个 模块
# *模块名 同样也是一个 标识符，需要符合标识符的命名规则
# *在模块中定义的 全局变量 、函数、类 都是提供给外界直接使用的 工具
# *模块 就好比是 工具包，要想使用这个工具包中的工具，就需要先 导入 这个模块
# >提示：在导入模块时，每个导入应该独占一行

# import 模块名1

# import 模块名2 
# *导入之后
#   *通过 模块名. 使用 模块提供的工具 —— 全局变量、函数、类

# 使用 as 指定模块的别名
# > 如果模块的名字太长，可以使用 as 指定模块的名称，以方便在代码中的使用

# import 模块名1 as 模块别名

# > 注意：模块别名 应该符合 大驼峰命名法

import test_module_1 as Test1
import test_module_2 as Test2

Test1.say_hello ()
Test2.say_hello ()

dog = Test1.Dog ()
print (dog)

cat = Test2.Cat ()
print (cat)