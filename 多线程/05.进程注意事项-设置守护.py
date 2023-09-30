# 1.主进程会等待所有子进程执行完成以后再退出
# 2.设置守护：
#   object.daemon = True
import time 
import multiprocessing

def work () :
    for i in range (10) :
        print ("Working...")
        time.sleep (0.2)

if __name__ == "__main__" :
    work_process = multiprocessing.Process (target=work)
    # 设置守护主进程，主进程结束子进程自动销毁，不再执行
    work_process.daemon = True
    work_process.start ()

    time.sleep (1)
    print ("The main process complete.")
    