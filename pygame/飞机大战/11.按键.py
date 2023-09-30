# > 在 pygame 中针对 键盘按键的捕获，有 两种 方式
# * 第一种方式 判断 event.type == pygame.KEYDOWN
# * 第二种方式
#   1.首先使用 pygame.key.get_pressed() 返回 所有按键元组
#   2.通过 键盘常量，判断元组中 某一个键是否被按下 —— 如果被按下，对应数值为 1

# 提问 这两种方式之间有什么区别呢？
# *第一种方式
# ```python
# elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
#     print("向右移动...")
# ```

# *第二种方式
# ```python
# # 返回所有按键的元组，如果某个键被按下，对应的值会是1
# keys_pressed = pygame.key.get_pressed()
# # 判断是否按下了方向键
# if keys_pressed[pygame.K_RIGHT]:
#     print("向右移动...")
# ```

# 结论
# *第一种方式 event.type 用户 必须要抬起按键 才算一次 按键事件，操作灵活性会大打折扣
# *第二种方式 用户可以按住方向键不放，就能够实现持续向某一个方向移动了，操作灵活性更好