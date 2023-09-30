import tool

# 显示功能菜单
while True :
    # 显示功能菜单
    tool.menuUI ()
    
    a = input ("请选择希望执行的操作：")
    print ("您选择的操作是【%s】" % a)

    if a in ["1","2","3"] :# 如果不希望立刻编写，则使用 pass
                           # pass 表示一个占位符，保证代码结构正确
        if a == "1" :
            tool.new_card ()
        elif a == "2" :
            tool.show_all ()
        else :
            tool.search_card ()
    
    elif a == "0" :
        print ("欢迎再次使用【名片管理系统】")
        break 
    else :
        print ("您输入的不正确，请重新选择")

    
