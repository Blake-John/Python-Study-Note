""" calculate the addition from 1 to 100000000

_use 8 threads to accelerate the calculate speed
"""

# import multiprocessing

# lst = [ n for n in range (1,100000001)]

# class calculate (multiprocessing.Process) :
#     def __init__ (self,tg,resultnum) :
#         super ().__init__ ()
#         self.tg = tg
#         self.resultnum = resultnum

#     def cl (self) :
#         a = 0
#         for x in self.tg :
#             a += x
#         self.resultnum.put (a)
        
    
# def main () :
#     resultnum = multiprocessing.Queue()
#     result = 0
#     index = 0
#     ths = []
#     for _ in range (8) :
#         tg = lst[index:index + 12500000]
#         index += 12500000
#         th = calculate (tg,resultnum)
#         ths.append (th)
#         th.start ()        
    
#     for t in ths :
#         t.join ()
    
#     for _ in ths :
#         result += resultnum.get ()
        
    
#     print (result)
    

# if __name__ == '__main__' :
#     main ()


from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()