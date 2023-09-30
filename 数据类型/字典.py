dic1 = {'Name':'Li Hua','Age':18,'Sex':'male'}
print (dic1)
print (dic1['Name'])

dic2 = dict (one=1,two=2,three=3,four=4,five=5)
print (dic2)

item1 = zip ('abc','123')
# or item1 = zip (['a','b','c'],'123')
print (item1)
dic3 = dict (item1)
print (dic3)

dic4 = {str(num):num * 2 for num in range (6)}
print (dic4)

for key in dic1 :
    print (f'{key}:{dic1[key]}')