# # -*- coding: utf-8 -*-
# import scrapy
# import re
# import os
# import hashlib
# import scrapy
# from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, \
#     BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
# import requests
# from scrapy.http import HtmlResponse
#
#
# class acadianahomeguide(scrapy.Spider):
#     name = 'acadianahomeguide'
#     allowed_domains = []
#     start_urls = ['https://www.acadianahomeguide.com/neighborhoods/']
#     builderNumber = '12562'
#
#     def parse(self, response):
#
#         subdivisonNumber = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
#
#         f = open("html/%s.html" % subdivisonNumber, "wb")
#         f.write(response.body)
#         f.close()
#
#
#         item2 = BdxCrawlingItem_subdivision()
#         item2['sub_Status'] = "Active"
#         item2['SubdivisionName'] = subdivisonName
#         item2['SubdivisionNumber'] = subdivisonNumber
#         item2['BuilderNumber'] = self.builderNumber
#         item2['BuildOnYourLot'] = 0
#         item2['OutOfCommunity'] = 1
#         item2['Street1'] = Street1
#         item2['City'] = City
#         item2['State'] = State
#         item2['ZIP'] = ZIP
#         item2['AreaCode'] = AreaCode
#         item2['Prefix'] = Prefix
#         item2['Suffix'] = Suffix
#         item2['Extension'] = ""
#         item2['Email'] = Email
#         item2['SubDescription'] = SubDescription
#         item2['SubImage'] = SubImage
#         item2['SubWebsite'] = response.url
#         item2['AmenityType'] = ''
#         yield item2
#
#
#
# if __name__ == '__main__':
#     from scrapy.cmdline import execute
#     execute("scrapy crawl acadianahomeguide".split())