card_list = []
def menuUI () :
    print ("*" * 80)
    print ("欢迎使用【名片管理系统】V1.0")
    print ("")
    print ("1.新建名片")
    print ("2.显示全部")
    print ("3.查询名片")
    print ("")
    print ("0.退出程序")
    print ("*" * 80)

def new_card () :
    print ("-" * 80)
    print ("新增名片")
    name = input ("请输入姓名：")
    age = input ("请输入年龄：")
    phone = input ("请输入电话号码：")
    qq = input ("请输入QQ号码：")
    e_mail = input ("请输入邮箱：")
    dict = {"姓名": name,"年龄": age,"电话号码": phone,"QQ号码": qq,"邮箱": e_mail}
    card_list.append (dict)
    print (card_list)
    print ("添加 %s 的名片成功！" % name)

def show_all () :
    print ("-" * 80)
    print ("显示所有名片")
    # 遍历名片列表一次输出字典信息
    # for card_dict in card_list :
    #     print ("*" * 80)
    #     print (card_dict)
    if len (card_list) == 0 :
        print ("当前没有任何名片记录，请先新建名片")
        return
        # return 可以返回一个函数的执行结果
        # return 下方的代码不会被执行
        # 如果 return 后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不反悔任何结果

    # 打印表头
    for name in ["姓名","年龄","电话","QQ号吗","邮箱"] :
        print (name,end="\t\t")
    print ("")
    print ("=" * 80)
    for card_dict in card_list :
        print ("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["姓名"],card_dict["年龄"],card_dict["电话号码"],card_dict["QQ号码"],card_dict["邮箱"]))
    
        


def search_card () :
    print ("-" * 80)
    print ("查找名片")

    # 提示用户输入要搜索的姓名
    find_name = input ("请输入要搜索的姓名")
    # 遍历名片列表，查询要搜索的姓名
    for card_dict in card_list :
        if card_dict["姓名"] == find_name :
            print ("姓名\t\t年龄\t\t电话\t\tQQ号吗\t\t邮箱")
            print ("=" * 80)
            print ("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["姓名"],card_dict["年龄"],card_dict["电话号码"],card_dict["QQ号码"],card_dict["邮箱"]))
            deal_card (card_dict)
            break
        else :
            print ("查无此人%s" % find_name)

def deal_card (find_dict) :
    print (find_dict)
    action = input ("请选择要进行的操作：1.修改 2.删除 0.返回")
    if action == "2" :
        card_list.remove(find_dict)
        print ("成功删除")
    elif action == "1" :
        find_dict["姓名"] = input_card (find_dict["姓名"],"姓名：")
        find_dict["年龄"] = input_card (find_dict["年龄"],"年龄")
        find_dict["电话号码"] = input_card (find_dict["电话号码"],"电话")
        find_dict["QQ号吗"] = input_card (find_dict["QQ号码"],"QQ号码")
        find_dict["邮箱"] = input_card (find_dict["邮箱"],"邮箱")
        print ("修改成功")
    elif action == "0" :
        pass
    else :
        print ("请重新输入")

def input_card (dict_value,tip_message) :
    # 1.提示用户输入内容
    result_str = input (tip_message)
    # 2.针对用户的输入进行判断秒如果用户输入了内容，直接返回结果
    if len(result_str) > 0 :
        return result_str
    # 3.如果用户没有输入内容，返回“字典中原有的值”
    else :
        return dict_value