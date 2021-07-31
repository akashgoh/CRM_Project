# -*- coding: utf-8 -*-
import hashlib
import re
import scrapy
from scrapy.utils.response import open_in_browser

from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec


class westanhomesSpider(scrapy.Spider):
    name = 'westanhomes'
    allowed_domains = []
    start_urls = ['http://www.westanhomes.com/']

    builderNumber = "448920123424687621013323607435"


    def parse(self, response):

        # IF you do not have Communities and you are creating the one
        # ------------------- If No communities found ------------------- #

        f = open("html/%s.html" % self.builderNumber, "wb")
        f.write(response.body)
        f.close()

        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = ''
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = "283A Glen Rd."
        item['City'] = "Garner"
        item['State'] = "NC"
        item['ZIP'] = "27529"
        item['AreaCode'] = "919"
        item['Prefix'] = "612"
        item['Suffix'] = "9645"
        item['Extension'] = ""
        item['Email'] = "info@westanhomes.com"
        description = ' '.join(response.xpath('//div[@class="col-md-6 col-sm-12 col-xs-12"]/p/text()').extract()).strip()
        descriptions = re.sub('\s+', ' ', re.sub('\r|\n|\t', ' ', description))

        item['SubDescription'] = descriptions
        item['SubImage'] = "http://www.westanhomes.com/data/slides/large/1473951449.jpg"
        item['SubWebsite'] = response.url
        yield item

        planpages = response.xpath('//div[@class="col-md-3 col-sm-4 col-xs-12 ft-border"]//a[contains(text(),"Our Neighborhoods")][1]/@href').extract_first()

        yield scrapy.FormRequest(url=planpages,callback=self.plans_1)

    def plans_1(self,response):
        plans = response.xpath('//div[@class="col-md-7 col-sm-7 col-xs-12"]//h3/a/@href').extract()
        for plan in plans:
            yield scrapy.FormRequest(url=plan,callback=self.plan_2,dont_filter=True)


    def plan_2(self,response):
        try:
            plans = response.xpath('//li[@class="col-md-4 col-sm-6 col-xs-12 text-center"]')
            for plan in plans:
                url = plan.xpath('./a[1]/@href').extract_first()
                text = ''.join(plan.xpath('.//text()').extract())


                if not "SOLD!" in text:
                    yield scrapy.FormRequest(url=url,callback=self.plan_3,dont_filter=True)


        except Exception as e:
            print("plan_2",e,response.url)

    def plan_3(self,response):
        try:
            try:
                planname = response.xpath('//h2[@class="home-name"]/text()').extract_first().strip().replace('"','')
            except Exception as e:
                print("planname",response.url, e)



            try:
                BasePrice = response.xpath('//span[contains(text(),"Price")]/parent::p/text()').extract_first()
                if BasePrice == None:
                    BasePrice = 0.00
                else:
                    BasePrice = BasePrice.strip().replace(",",'').replace("$",'').replace('"','').strip()

            except Exception as e:
                print("baseprice",response.url, e)

            try:
                garages = response.xpath('//span[contains(text(),"Garage")]/parent::p/text()').extract_first()\
                    .strip().replace("Car",'').replace("car",'').replace('"','').replace("Attached",'').strip()
                if "None" in garages:
                    garages = 0.00

            except Exception as e:
                print("garages",response.url, e)

            try:
                baths = response.xpath('//span[contains(text(),"Bathrooms")]/parent::p/text()').extract_first()\
                    .strip().replace('"','').strip()
                if ".5" in baths:
                    fullbaths = baths[0].replace(".5", '').strip()
                    halfbaths = 1

                else:
                    fullbaths = baths[0].strip()
                    halfbaths = 0

            except Exception as e:
                print("baths",response.url, e)

            try:
                beds = response.xpath('//span[contains(text(),"Bedrooms")]/parent::p/text()').extract_first()\
                    .strip().replace('"','').strip()
            except Exception as e:
                print("beds", response.url,e)

            try:
                sqft = response.xpath('//span[contains(text(),"Sq. Ft.")]/parent::p/text()').extract_first()\
                    .strip().replace('"','').strip()
                if "-" in sqft:
                    sqft = sqft.split("-")[0].strip()

            except Exception as e:
                print("sqft", response.url,e)

            # ------------------- If Plan Found found ------------------------- #
            PlanNumber = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)

            SubdivisionNumber = self.builderNumber  # if subdivision is not available
            unique = str(PlanNumber) + str(SubdivisionNumber)
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = "SingleFamily"
            item['PlanNumber'] = PlanNumber
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = planname
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = "Single Family"
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = sqft
            item['Baths'] = fullbaths
            item['HalfBaths'] = halfbaths
            item['Bedrooms'] = beds
            item['Garage'] = garages
            description = ' '.join(response.xpath('//div[@class="col-md-12 col-sm-12 col-xs-12"]/p[2]//text()').extract())
            if description == '':
                description = ' '.join(response.xpath('//div[@class="row home-info"]//p//text()').extract())
            descriptions = re.sub('\s+', ' ', re.sub('\r|\n|\t', ' ',description))
            item['Description'] = descriptions
            images = response.xpath('//div[@class="img-holder"]//img/@src').extract()
            img = []
            for image in images:
                imageurl = "http://www.westanhomes.com"+image
                img.append(imageurl)

            finalimages = "|".join(img)
            item['ElevationImage'] = finalimages
            item['PlanWebsite'] = response.url
            yield item



        except Exception as e:
            print("plan_3",e,response.url)


# #
# #
# from scrapy.cmdline import execute
# execute("scrapy crawl westanhomes".split())