import json

# def read_two (position) :
#     try :
#         with open (position,'rb') as f1 :
#             data = f1.read ()
#         with open ('F:/艺术/copy.jpg','wb') as f2 :
#             f2.write (data)
#     except FileNotFoundError :
#         print ("Could not find the file!")
#     except IOError :
#         print ("There is an error while writing the file!")

# if __name__ == '__main__' :
    # read_two ('F:/艺术/板绘/原画/战双/百感交集.jpg')
    
def main () :
    mydict = {
        'name':'Lihua',
        'sex':'male',
        'age':18,
        'QQ number':123456,
        'friends':['Xiao Mei','Xiao Ming'],
        'cars':[
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    
    try :
        with open ('D:/计算机/python学习/程序/面向对象/03.文件/data.json','w',encoding='utf-8') as f :
            json.dump (mydict,f)
    except IOError as e :
        print (e)

if __name__ == '__main__' :
    main ()
    
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象