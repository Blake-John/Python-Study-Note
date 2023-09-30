# 递归：函数调用自身的 编程技巧 成为递归
# 特点：一个函数内部调用自己
# 代码特点：
#  1、函数内部的代码相同，只是针对 参数 不同，处理的 结果 不同
#  2、当函数满足一个条件时，函数不再执行
#     被称为递归的 出口 ，否则会出现 死循环 

def sum_number (num) :
    print (num)
    # 递归的出口
    if num == 1 :
        return
    # 自己调用自己
    sum_number (num - 1)

sum_number (4)

def sum (number) :
    # 1.出口
    if number == 1 :
        return 1
    # 2.累加 num + (1......num -1)
    # 假设 sum 能正确处理 (1......num -1)
    temp = sum (number - 1)
    return number + temp

result = sum (5)
print (result)