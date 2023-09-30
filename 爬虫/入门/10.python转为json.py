import json
# 把python转化为json字符串
json_str = """[{"provinceName":"美国","currentConfirmedCount":1179041,"confirmedCount":1643499},{"provinceName":"英国","currentConfirmedCount":222227,"confirmedCount":259559}]"""
rs = json.loads (json_str) # 把json转化为python数据
json_str = json.dumps (rs) # "json.dumps" 把python数据转化为json字符串
print (json_str)

# 把python以json格式存储到文件中
with open ("C:/Users/123/OneDrive/桌面/学习/程序/爬虫/text1.json","w") as fp :
    json.dump (rs,fp,ensure_ascii=False)
    # "json.dump (object,fp)" 把python类型数据以json格式写入文件
