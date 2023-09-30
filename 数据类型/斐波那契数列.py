def fib (n) :
    x,y = 1,0
    for i in range (n) :
        x,y = x + y,x
        yield x

def main () :
    lst = []
    for x in fib (10) :
        lst.append (x)
    print (lst)

if __name__ == '__main__' :
    main ()