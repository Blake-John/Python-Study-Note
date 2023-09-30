# 线程
# *进程是分配资源的 最小单位 ,一旦创建一个进程就会分配一定的资源
#  就像跟两个人聊QQ就需要打开两个QQ软件一样是比较浪费资源的
# *线程是程序执行的最小单位,实际上进程只负责 分配资源,而利用这些资源 执行程序 的是 线程,
#  也就说进程是线程的 容器,一个进程中 最少有一个线程 来负责执行程序,同时线程自己 不拥有 系统资源,
#  只需要一点儿在运行中必不可少的资源,但它可与同属一个进程的其它线程共享进程所拥有的全部资源.
#  这就像通过一个QQ软件(一个进程打开两个窗口(俩两个线程)跟两个人聊天一样,实现多任务的同时也节省了资源

# 1.导入线程模块
#   import threading
# 2.创建线程对象
#   object = threading.Thread (target,name,group)
# 3.启动线程执行任务
#   object.start ()
# | 参数名  | 说明                                   |
# | :----: | :------------------------------------: |
# | target | 执行的目标任务名，这里指的是函数名(方法名) |
# | name   | 线程名，一般不用设置                     |
# | group  | 线程组，目前只能使用 None                |


import threading
import time 

def sing () :
    for i in range (3) :
        print ("Singing...")
        time.sleep (1)
    
def dance () :
    for i in range (3) :
        print ("Dancing...")
        time.sleep (1)

if __name__ == "__main__" :
    # sing ()
    # dance ()
    sing_thread = threading.Thread (target=sing)
    dance_thread = threading.Thread (target=dance)

    sing_thread.start ()
    dance_thread.start ()
