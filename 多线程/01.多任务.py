# 多任务的概念：同一时间内执行多个任务
# 多任务的表现形式：
# 1.并发：在一段时间内 交替执行 多个任务
#  *例如对于单核cpu处理多任务，操作系统轮流让各个 任务交替执行
# 2.并行：在一段时间内 真正的同时执行多个任务
# 多任务的实现方式：使用多进程来完成

# 进程：进程是资源分配的最小单位，它是操作系统进行资源分配和调度运行的基本单位。
#       通俗地讲：一个正在运行的程序就是一个进程
#  1.主进程：程序执行时默认创建的进程
#  2.子进程：程序执行后再次创建的进程

# 进程的创建步骤：
# 1.导入进程包
#   import multiprocessing
# 2.通过进程类创建进程对象
#   object = multiprocessing.Process (target,name,group)
# | 参数名  | 说明                                   |
# | :----: | :------------------------------------: |
# | target | 执行的目标任务名，这里指的是函数名(方法名) |
# | name   | 进程名，一般不用设置                     |
# | group  | 进程组，目前只能使用 None                |
# 3.启动进程执行任务
#   object.start ()


# 单进程的运行模式
import time

def sing () :
    for i in range (3) :
        print ("Singing...")
        time.sleep (0.5)

def dance () :
    for i in range (3) :
        print ("Dancing...")
        time.sleep (0.5)

if __name__ == "__main__" :
    sing ()
    dance ()