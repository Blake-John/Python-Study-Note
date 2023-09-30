import os
import multiprocessing
import random
import time

def download_task (filename) :
    print ("Start the download program...")
    print (f"the number of the program is {os.getpid ()}")
    print (f'Start to download {filename}')
    time_to_download = random.randint (5,11)
    time.sleep (time_to_download)
    print (f"Download Successfully.Using {time_to_download} seconds.")

def main () :
    start = time.time () # 获取现在的时间
    p1 = multiprocessing.Process (target=download_task,args=('How to learn Python.pdf',))
    p2 = multiprocessing.Process (target=download_task,args=('How to learn C++.pdf',))
    p1.start ()
    p2.start ()
    p1.join ()
    p2.join ()
    end = time.time ()
    print (f"All task are downloaded successfully! Using {end - start} seconds.")

if __name__ == '__main__' :
    main ()