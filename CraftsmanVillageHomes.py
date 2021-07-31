# -*- coding: utf-8 -*-
import hashlib
from lxml import html
import re
import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http import HtmlResponse
import requests

from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec


class blueribbonokSpider(scrapy.Spider):
    name = 'craftsmanvillages'
    # allowed_domains = ['bobthompsonhomes.com']
    start_urls = ['http://craftsmanvillagehomes.com/']
    builderNumber = "167288689284911247833216190772"


    def parse(self, response):

        # IF you do not have Communities and you are creating the one
        # --------------------------------------------------------------------------- If No communities found ------------------------------------------------------------------------------------------------ #

        f = open("html/%s.html" % self.builderNumber, "wb")
        f.write(response.body)
        f.close()
        try:

            item = BdxCrawlingItem_subdivision()
            item['sub_Status'] = "Active"
            item['SubdivisionNumber'] = ''
            item['BuilderNumber'] = self.builderNumber
            item['SubdivisionName'] = "No Sub Division"
            item['BuildOnYourLot'] = 0
            item['OutOfCommunity'] = 0
            item['Street1'] = "Putnam St."
            item['City'] = "Needham"
            item['State'] = "MA"
            item['ZIP'] = "02494"
            item['AreaCode'] = '978'
            item['Prefix'] = '456'
            item['Suffix'] = '8388'
            item['Extension'] = ""
            item['Email'] = "mark@craftsmanvillagehomes.com"
            item['SubImage'] = self.start_urls[0]+response.xpath('//div[@id="photo"]/img/@src').get()
            item['SubDescription'] = """Craftsman Village Homes specializes in the development and building of residential communities with smaller, designed focused homes with a high level of energy efficiency. We have created a home series which is truly unique to the area, providing Craftsman and Bungalow style residences in high value, close knit communities in the Greater Boston area.
                                        Please review our site to see our current and upcoming locations. We are adding new sites regularly and are always looking for more suitable locations for our concept. If you like our homes, but do not see a location that suits your needs, please join our email list. We will keep you updated on any new developments and we pledge to release new projects to our email list before the general market. We can also build our homes on your lot and will customize our product to truly suit your household’s needs."""
            item['SubWebsite'] = ''
            yield item

        except Exception as e:
            print("Problem in Community :", e)

        try:
            item = BdxCrawlingItem_Plan()
            unique = str("Plan Unknown") + str(self.builderNumber)
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['Type'] = "SingleFamily"
            item['PlanNumber'] = "Plan Unknown"
            item['SubdivisionNumber'] = self.builderNumber
            item['PlanName'] = "Plan Unknown"
            item['PlanNotAvailable'] = 1
            item['PlanTypeName'] = "Single Family"
            item['BasePrice'] = 0
            item['BaseSqft'] = 0
            item['Baths'] = 0
            item['HalfBaths'] = 0
            item['Bedrooms'] = 0
            item['Garage'] = 0
            item['Description'] = ""
            item['ElevationImage'] = ""
            item['PlanWebsite'] = ""
            yield item

        except Exception as e:
            print("Problem in Unknown_Plan creation:", e)
        # --------------------------------------------------------------------- #
#
# from scrapy.cmdline import execute
# execute("scrapy crawl craftsmanvillages".split())