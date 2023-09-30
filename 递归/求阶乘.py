def recursion (n) :
    result = n
    for i in range (1,n) :
        result *= i
    return result

number = int (input ("请输入要进行运算的整数"))
result = recursion (number)
print ("%d5的阶乘是: %d " % (number,result))