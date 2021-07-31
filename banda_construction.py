
import scrapy
import re
import os
import hashlib
import scrapy
from pygments.lexer import default
from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse


class Baird_Homes_Corporation(scrapy.Spider):
    name = 'banda_construction'
    builderNumber = '62867'

    def start_requests(self):
        url = 'https://banda-construction.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self,response):
        try:
            print("---------- Not_Found_Community ---------")
            item = BdxCrawlingItem_subdivision()
            item['sub_Status'] = "Active"
            item['SubdivisionNumber'] = self.builderNumber
            item['BuilderNumber'] = self.builderNumber
            item['SubdivisionName'] = "No Sub Division"
            item['BuildOnYourLot'] = 0
            item['OutOfCommunity'] = 0
            item['Street1'] = '2875 S US 231'
            item['City'] = 'HUNTINGBURG'
            item['State'] = 'IN'
            item['ZIP'] = '47542'
            item['AreaCode'] = '812'
            item['Prefix'] = "683"
            item['Suffix'] = "4600"
            item['Extension'] = ""
            item['Email'] = "info@banda-construction.com"
            item['SubDescription'] = 'B & A Construction & Design is an Indiana-based company that sells construction and building products. We have been in business for over 35 years, providing excellent workmanship along with grade A materials. '
            item['SubImage'] = 'https://secureservercdn.net/166.62.104.68/5ja.748.myftpupload.com/wp-content/uploads/2021/04/Open-House-Web-image-2021-1-scaled.jpg|https://secureservercdn.net/166.62.104.68/5ja.748.myftpupload.com/wp-content/uploads/2021/03/image003-6084cacb-9d45-4bbf-a708-af0bed691d22.jpg?time=1619593433'
            item['SubWebsite'] = 'https://banda-construction.com/'
            item['AmenityType'] = ''
            yield item
        except Exception as e:
            print(e)

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl banda_construction".split())