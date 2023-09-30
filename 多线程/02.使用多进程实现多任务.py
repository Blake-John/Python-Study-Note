# 1.导入进程包
import multiprocessing
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
    # 2.使用进程类创建进程
    sing_process = multiprocessing.Process (target=sing)     # target为执行的目标任务名
    dance_process = multiprocessing.Process (target=dance)   # 这里指的是函数名(方法名)
    
    # 3.使用进程对象启动进程执行指定任务
    sing_process.start ()
    dance_process.start ()