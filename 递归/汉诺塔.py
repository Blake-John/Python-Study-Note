def hanoi (n,x,y,z) :
    if n == 1 :
        print (x,"-->",z) #如果只有一层，直接从x移动到z
    else :
        hanoi (n-1,x,z,y) #将前n-1个盘子从x移动到y上
        print (x,"-->",z) #将最底下的第64个盘子从x移动到z上
        hanoi (n-1,y,x,z) #将以上的第63个盘子移动到z上

n = int (input ("请输入汉诺塔的层数"))
hanoi (n,"x","y","z")