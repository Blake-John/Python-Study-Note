# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SinaPipeline:
    def process_item(self, item, spider):
        sonUrl = item['sub_SonUrl']
        
        file_path = sonUrl[7:-6].replace ("/","_")
        file_path += ".txt"

        fp = open (item['subFilepath'] + "/" + file_path,"w")
        fp.write (item['content'])
        fp.close ()
        return item
