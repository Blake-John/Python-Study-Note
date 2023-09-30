# | 参数名  | 说明                                                      |
# | :----: | :-------------------------------------------------------: |
# | target | 执行的目标任务名，这里指的是函数名(方法名)                    |
# | args   | 以元组的方式给执行任务传递参数,按照元组元素顺序传递            |
# | kwargs | 以字典的方式给执行任务传递参数，按照 key值 传递，key就是参数名 |

import threading
import time 

def sing (count,name) :
    for i in range (count) :
        print ("%s is singing..." % name)
        time.sleep (1)
    
def dance (count,name) :
    for i in range (count) :
        print ("%s is dancing..." % name)
        time.sleep (1)

if __name__ == "__main__" :
    # sing ()
    # dance ()
    sing_thread = threading.Thread (target=sing,args=(3,"Xiaoming"))
    dance_thread = threading.Thread (target=dance,kwargs={"count":2,"name":"Xiaoming"})

    sing_thread.start ()
    dance_thread.start ()
