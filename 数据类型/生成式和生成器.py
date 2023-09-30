import sys

f = [x for x in range (10)]
print (f)
print (sys.getsizeof (f))

g = (y for y in range (10))
print (g)
print (sys.getsizeof (g))

for i in g :
    print (i)