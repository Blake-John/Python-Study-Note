# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class PunishPipeline:
    def __init__(self) -> None:
        # json 格式需要以 "utf-8" 来编码
        self.f = open ("result.json","w",encoding="utf-8")

    def process_item(self, item, spider):
        # 千万记住有中文要设置 ensure_ascii=False
        content = json.dumps (dict (item),ensure_ascii=False) + "\n"
        self.f.write (content)
        return item

    def close_spider (self,spider) :
        self.f.close ()