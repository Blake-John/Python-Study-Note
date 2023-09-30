# 游戏的初始化和退出
# * 要使用 pygame 提供的所有功能之前，需要调用 init 方法
# * 在游戏结束前需要调用一下 quit 方法 
# | 方法          | 说明                                                             |
# | ------------- | --------------------------------------------------------------- |
# | pygame.init() | 导入并初始化所有 pygame 模块，使用其他模块之前，必须先调用 init 方法 |
# | pygame.quit() | 卸载所有 pygame 模块，在游戏结束之前调用！                         |

# 理解游戏中的坐标系
# * 坐标系
#   * 原点 在 左上角 (0, 0)
#   * x 轴 水平方向向 右，逐渐增加
#   * y 轴 垂直方向向 下，逐渐增加

# *在游戏中，所有可见的元素 都是以 矩形区域 来描述位置的
#   *要描述一个矩形区域有四个要素：(x, y) (width, height)
# *pygame专门提供了一个类 pygame.Rect 用于描述 矩形区域
# x,y表示原点的位置 width,height表示矩形区域的宽和高
# Rect(x, y, width, height) -> Rect
# * pygame.Rect 是一个比较特殊的类，内部只是封装了一些数字计算
# *不执行 pygame.init() 方法同样能够直接使用

import pygame

pygame.init ()

# 编写游戏代码
print ("The game code......")
hero_rect = pygame.Rect (100,500,120,125)
print ("Hero's origin (%d,%d)" % (hero_rect.x,hero_rect.y))
print ("Hero size (%d,%d)" % (hero_rect.width,hero_rect.height))
print ("Hero size (%d,%d)" % hero_rect.size)
pygame.quit ()