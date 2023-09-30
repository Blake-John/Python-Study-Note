import random
import threading
import time

class DownloadTask (threading.Thread) :
    def __init__(self,filename) :
        super ().__init__()
        self._filename = filename
    
    def run (self) :
        print (f"Start to download {self._filename}...")
        time_to_finish = random.randint (5,11)
        time.sleep (time_to_finish)
        print (f"Download {self._filename} successfully! Using {time_to_finish} seconds.")

def main () :
    start = time.time ()
    t1 = DownloadTask ('How to learn Python well.pdf')
    t2 = DownloadTask ('How to learn C++ well.pdf')
    t1.start ()
    t2.start ()
    t1.join ()
    t2.join ()
    end = time.time ()
    print (f"All download successfully! Using {end - start} seconds.")
        
if __name__ == '__main__' : 
    main ()