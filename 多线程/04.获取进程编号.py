# 1.获取当前进程编号
#   os.getpid ()
# 2.获取父进程编号
#   os.getppid ()

import os
import multiprocessing
import time

def sing (num,name) :
    print ("Sing Process ID: %d." % os.getpid ())
    print ("The ID of the parent of Sing Process: %d." % os.getppid ())
    for i in range (num) :
        print ("%s Singing..." % name)
        time.sleep (0.5)

def dance (num,name) :
    print ("The ID of the parent of Dance Process: %d." % os.getppid ())
    print ("Dance Process ID: %d." % os.getpid ())
    for i in range (num) :
        print ("%s Dancing..." % name)
        time.sleep (0.5)

# 主进程：
if __name__ == "__main__" :
    print ("Main Process ID: %d." % os.getpid ())
    # 1.创建子进程对象并指定执行的任务
    sing_process = multiprocessing.Process (target=sing,args=(3,"Xiaoming"))    
    dance_process = multiprocessing.Process (target=dance,kwargs={"name":"Xiaoming","num":2})  
    # 2.启动子进程并执行任务
    sing_process.start ()
    dance_process.start ()