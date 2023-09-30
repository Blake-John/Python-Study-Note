# | 参数名  | 说明                                                      |
# | :----: | :-------------------------------------------------------: |
# | target | 执行的目标任务名，这里指的是函数名(方法名)                    |
# | args   | 以元组的方式给执行任务传递参数,按照元组元素顺序传递            |
# | kwargs | 以字典的方式给执行任务传递参数，按照 key值 传递，key就是参数名 |

# 1.导入进程包
import multiprocessing
import time

def sing (num,name) :
    for i in range (num) :
        print ("%s Singing..." % name)
        time.sleep (0.5)

def dance (num,name) :
    for i in range (num) :
        print ("%s Dancing..." % name)
        time.sleep (0.5)

if __name__ == "__main__" :
    # 2.使用进程类创建进程
    sing_process = multiprocessing.Process (target=sing,args=(3,"Xiaoming")) # 以元组的方式传参    
    dance_process = multiprocessing.Process (target=dance,kwargs={"name":"Xiaoming","num":2}) # 以字典的方式传参  
    
    # 3.使用进程对象启动进程执行指定任务
    sing_process.start ()
    dance_process.start ()