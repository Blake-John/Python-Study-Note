set1 = {1,2,3,4,5}
set2 = set (range (1,10))
set3 = set ((1,2,3,3,2,1))
print (set2,'\n',set3)

set1.add (6)
set2.discard (5)
set3.update ([6,7])
print (set1,'\n',set2,'\n',set3)