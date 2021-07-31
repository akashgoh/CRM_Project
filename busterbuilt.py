# -*- coding: utf-8 -*-
import re
import os
import hashlib
import scrapy
from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision

class busterbuiltSpiderSpider(scrapy.Spider):
    name = 'busterbuilt'
    allowed_domains = ['busterbuilt.com/']
    start_urls = ['http://www.busterbuilt.com/']
    buildernumber='169997824428359468527692220082'



    def parse(self, response):
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = ''
        item['BuilderNumber'] = self.buildernumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 1
        item['Street1'] = '3050 N Lake Harbor Ln. Suite 128'
        item['City'] = 'Boise    '
        item['State'] = 'ID '
        item['ZIP'] = '83703'
        item['AreaCode'] = '208'
        item['Prefix'] = "342"
        item['Suffix'] = "6067"
        item['Extension'] = ""
        item['Email'] = "jerimy.busterbuilt@gmail.com"
        item['SubDescription'] = "Stuart “Buster” Dancer has been involved in residential construction in the Boise area since 1976. Starting as an apprentice cabinet maker, Buster has hands-on experience in several trades relating to remodeling and construction. “I enjoy being involved in every aspect of construction, from design to final details.”"
        item['SubImage'] = 'http://www.busterbuilt.com/wp-content/uploads/2017/09/3.jpg|http://www.busterbuilt.com/wp-content/uploads/2017/09/slide1.jpg|http://www.busterbuilt.com/wp-content/uploads/2017/09/2.jpg'
        item['SubWebsite'] = response.url
        item['AmenityType'] =''
        yield item



if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl busterbuilt".split())