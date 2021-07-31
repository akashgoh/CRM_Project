# -*- coding: utf-8 -*-
import hashlib
import re
import scrapy
from scrapy.utils.response import open_in_browser

from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec


class needlepointhomesSpider(scrapy.Spider):
    name = 'needlepointhomes'
    allowed_domains = []
    start_urls = ['https://www.needlepointhomes.com/']

    builderNumber = "654188053703761179463925469905"


    def parse(self, response):
        try:
            # IF you do not have Communities and you are creating the one
            # ------------------- If No communities found ------------------- #

            f = open("html/%s.html" % self.builderNumber, "wb")
            f.write(response.body)
            f.close()
            SubdivisionNumber = ''
            item = BdxCrawlingItem_subdivision()
            item['sub_Status'] = "Active"
            item['SubdivisionNumber'] = ''
            item['BuilderNumber'] = self.builderNumber
            item['SubdivisionName'] = "No Sub Division"
            item['BuildOnYourLot'] = 0
            item['OutOfCommunity'] = 0
            item['Street1'] = "108 North Union Avenue Suite #5"
            item['City'] = "Cranford"
            item['State'] = "NJ"
            item['ZIP'] = "07016"
            item['AreaCode'] = "908"
            item['Prefix'] = "301"
            item['Suffix'] = "1000"
            item['Extension'] = ""
            item['Email'] = "needlepointhomes@gmail.com"
            item['SubDescription'] = "Needle Point Homes specializes in the design and construction of single family custom homes, apartments and commercial properties. We strive to create works of art that resonate luxury and integrity, as well as comfort and style. Thank you for the opportunity to be considered as your builder."
            item['SubImage'] = 'http://www.needlepointhomes.com/wp-content/uploads/2016/03/cooper-2-1-e1457039535389.jpg|http://www.needlepointhomes.com/wp-content/uploads/2016/03/cooper-2-2-e1457039098927.jpg|http://www.needlepointhomes.com/wp-content/uploads/2016/03/001-188151-afront1crop-s-_3814947-e1456246706682.jpg'
            item['SubWebsite'] = ''
            item['AmenityType'] = ''
            yield item

            # plan_link = 'https://www.needlepointhomes.com/current-properties/westfield/'
            yield scrapy.Request(url='https://www.needlepointhomes.com/current-properties/1200-donamy-glen-scotch-plains/',dont_filter=True,callback=self.plan_details)
        except Exception as e:
            print("needle",e,response.url)

    def plan_details(self,response):
        item = BdxCrawlingItem_Plan()

        PlanName ='1200 Donamy Glen'
        PlanNumber = int(hashlib.md5(bytes(str(PlanName), "utf8")).hexdigest(), 16) % (10 ** 30)

        SubdivisionNumber = self.builderNumber  # if subdivision is not available
        unique = str(PlanNumber) + str(SubdivisionNumber)
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)


        item['Type']='SingleFamily'
        item['PlanNumber']=PlanNumber
        item['SubdivisionNumber']=SubdivisionNumber
        item['PlanName']=PlanName
        item['PlanNotAvailable']=0
        item['PlanTypeName']='Single Family'
        item['BasePrice']=0
        item['BaseSqft']=0
        item['Baths']= 3
        item['HalfBaths']=1
        item['Bedrooms']=4
        item['Garage']=0
        item['Description']='Needle Point Homes, a premier custom builder/renovator is proud to present 1200 Donamy Glen in Scotch Plains. Located 25 miles from NYC and close proximity to NYC transportation sits this sprawling custom renovated 107 foot long ranch, with 4 bedrooms and 3.5 baths. This home is situated on a private one acre tree lined cul-de-sac, with an inviting in-ground pool, and located in one of NJ’s top rated school districts with access to prime shopping.'
        item['ElevationImage']='https://www.needlepointhomes.com//wp-content/uploads/2020/11/1200donamyfloorplan__UBq8G.jpg|https://www.needlepointhomes.com//wp-content/uploads/2020/12/survey2-e1607631581423.png|https://www.needlepointhomes.com//wp-content/uploads/2021/01/526-1.png|https://www.needlepointhomes.com//wp-content/uploads/2021/01/526-5.png|https://www.needlepointhomes.com/wp-content/uploads/2020/11/donameyfinal__4_.jpg'
        item['PlanWebsite']='https://www.needlepointhomes.com/current-properties/westfield/'
        item['unique_number']=unique_number
        yield item



if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl needlepointhomes".split())