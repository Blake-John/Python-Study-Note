# *pygame专门提供了一个 模块 pygame.display 用于创建、管理 游戏窗口
# | 方法                      | 说明                     |
# | ------------------------- | ----------------------- |
# | pygame.display.set_mode() | 初始化游戏显示窗口        |
# | pygame.display.update()   | 刷新屏幕内容显示，稍后使用 |

# set_mode 方法
# ```python
# set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
# ```

# *作用 —— 创建游戏显示窗口
# *参数
#   * resolution 指定屏幕的 宽 和 高，默认创建的窗口大小和屏幕大小一致
#   * flags 参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
#   * depth 参数表示颜色的位数，默认自动匹配
# *返回值
#   *暂时 可以理解为 游戏的屏幕，游戏的元素 都需要被绘制到 游戏的屏幕 上
# *注意：必须使用变量记录 set_mode 方法的返回结果！因为：后续所有的图像绘制都基于这个返回结果

# *为了做到游戏程序启动后，不会立即退出，通常会在游戏程序中增加一个 游戏循环
# *所谓 游戏循环 就是一个 无限循环
# *在 创建游戏窗口 代码下方，增加一个无限循环
#   *注意：游戏窗口不需要重复创建

import pygame

pygame.init ()

# 创建游戏的窗口
screen = pygame.display.set_mode ((480,700))
while True :
    pass

pygame.quit ()