# 1.主线程会等待所有子线程结束以后再结束
# 2.设置守护：
#   * object = threading.Thread (target=work,daemom=True)
#   * object.daemon = True
# 3.线程执行顺序是由系统调配的，是无序的


import time 
import threading

def task () :
    time.sleep (2)
    # threading.current_thread () 获取当前线程的线程对象
    thread = threading.current_thread ()
    print (thread)

if __name__ == "__main__" :
    for i in range (5) :
        sub_thread = threading.Thread (target=task)
        sub_thread.start () 