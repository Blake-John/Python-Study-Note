# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MyspiderPipeline:
    def __init__(self) -> None:
        self.f = open ("tencent.json","w",encoding="utf-8")

    def process_item(self, item, spider):
        # 因为 item 格式并不是真正的字典，所以先将 item 转化为字典
        # 然后再使用 json.dump () 转化为 json 格式，因为文件里有中文，所以设置属性 ensure_ascii = False
        content = json.dumps (dict (item),ensure_ascii = False) + ",\n"
        self.f.write (content)
        return item
    
    def close_spider (self,spider) :
        self.f.close ()
