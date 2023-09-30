# *在pygame中可以使用 pygame.time.set_timer() 来添加 定时器
# *所谓 定时器，就是 每隔一段时间，去 执行一些动作

# ```python
# set_timer(eventid, milliseconds) -> None
# ```

# * set_timer 可以创建一个 事件
# *可以在 游戏循环 的 事件监听 方法中捕获到该事件
# *第 1 个参数 事件代号 需要基于常量 pygame.USEREVENT 来指定
#   * USEREVENT 是一个整数，再增加的事件可以使用 USEREVENT + 1 指定，依次类推...
# *第 2 个参数是 事件触发 间隔的 毫秒值

# 定时器事件的监听
# *通过 pygame.event.get() 可以获取当前时刻所有的 事件列表
# *遍历列表 并且判断 event.type 是否等于 eventid，如果相等，表示 定时器事件 发生

# pygame 的 定时器 使用套路非常固定：
# 1.定义 定时器常量 —— eventid
# 2.在 初始化方法 中，调用 set_timer 方法 设置定时器事件
# 3.在 游戏循环 中，监听定时器事件

# 1) 定义事件
# *在 plane_sprites.py 的顶部定义 事件常量
# ```python
# # 敌机的定时器事件常量
# CREATE_ENEMY_EVENT = pygame.USEREVENT
# ```
# * 在 PlaneGame 的 初始化方法 中 创建用户事件
# ```python
# # 设置定时器事件 - 每秒创建一架敌机
# pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
# ```

# 2) 监听定时器事件
# * 在 __event_handler 方法中增加以下代码：
# ```python
# def __event_handler(self):  
#     for event in pygame.event.get():
#         # 判断是否退出游戏
#         if event.type == pygame.QUIT:
#             PlaneGame.__game_over()
#         elif event.type == CREATE_ENEMY_EVENT:
#             print("敌机出场...")
# ```
