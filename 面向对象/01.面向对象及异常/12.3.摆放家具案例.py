class HouseItem :
    def __init__(self,name,area) -> None:
        self.name = name
        self.area = area
    
    def __str__(self) -> str:
        return "[%s] covers an area of %.2f square meters." % (self.name,self.area)

# 创建多个类，类与类之间最好应保留 两空行
class House :
    def __init__(self,house_type,area) -> None:
        self.house_type = house_type
        self.area = area 

        self.free_area = area 
        self.item_list = []
    
    def add (self,item) :
        # 判断家具的面积
        if item.area > self.free_area :
            print ("The house is not big enough to add %s." % item.name)
            return
        # 添加家具
        self.item_list.append (item.name)
        print ("It will add [%s]" % item.name)
        #计算剩余面积
        self.free_area -= item.area

    def __str__(self) -> str:
        # python 能够将一对括号内的代码连接在一起
        return ("House type : %s\nArea : %.2f [Free area : %.2f]\nItem : %s" 
        % (self.house_type,self.area,self.free_area,self.item_list))

# 创建家具对象    
bed = HouseItem ("Ximengsi" ,90)
chest = HouseItem ("yigui",2)
table = HouseItem ("canzuo",20)
# print (bed)
# print (chest)
# print (table)

# 创建房子对象
house = House ("Two rooms one hall",100.0)
# 添加家具
house.add (bed)
house.add (chest)
house.add (table)
print (house)