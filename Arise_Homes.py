import scrapy
import re
import os
import hashlib
import scrapy
from pygments.lexer import default
from twisted.spread.test.test_jelly import E

from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse


class arisehomes(scrapy.Spider):
    name = 'arisehomes'
    builderNumber = '62763'

    def start_requests(self):
        url = 'https://arise-homes.com/communities/shawnee/legacy-crossing'
        yield scrapy.Request(url=url,callback=self.cmmunity_details)

    def cmmunity_details(self,response):
        try:
            SubdivisionName = response.xpath('//h1/text()').extract_first(default='')
        except Exception as e:
            SubdivisionName = ''
            print(e)
        try:
            Street1 = response.xpath('//*[@class="Carousel_h2Wrapper"]/span/text()').extract_first(default = '')
        except Exception as e:
            Street1 = ''
            print(e)
        try:
            city_state_zip = response.xpath('//h2/span/text()').extract_first(default='')
            city =city_state_zip.split(',')[0]
            state = city_state_zip.split(',')[1].split(' ')[1]
            zip_code = city_state_zip.split(',')[1].split(' ')[2]
        except Exception as e:
            print(e)

        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] =SubdivisionName
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = Street1
        item['City'] = city
        item['State'] = state
        item['ZIP'] = zip_code
        item['AreaCode'] = '913'
        item['Prefix'] = "339"
        item['Suffix'] = "9817"
        item['Extension'] = ""
        item['Email'] = ""
        item['SubDescription'] = "Arise Homes is built on the idea that your new home should be higher quality for lower cost... all through the life of your home. It begins with our 1,350 point construction checklist. Next, we use sustainable, low maintenance materials such as full size, real stone and brick around all four sides of the home. Finally, we have personalized, beautiful finishes to choose from."
        item['SubImage'] = 'https://dlqxt4mfnxo6k.cloudfront.net/arise-homes.com/aHR0cHM6Ly9zMy5hbWF6b25hd3MuY29tL2J1aWxkZXJjbG91ZC9hMWJiZDFhOGMxYTY2MzE5YmYxZWQwNWM1MTVkZmEzNC5qcGVn/exact/2000/1125|https://dlqxt4mfnxo6k.cloudfront.net/arise-homes.com/aHR0cHM6Ly9zMy5hbWF6b25hd3MuY29tL2J1aWxkZXJjbG91ZC9kYmFkM2ZmYTE5MWU4YmI4ZGY2ZWViNzgyMGIwZWZjZS5qcGVn/exact/600/380|https://dlqxt4mfnxo6k.cloudfront.net/arise-homes.com/aHR0cHM6Ly9zMy5hbWF6b25hd3MuY29tL2J1aWxkZXJjbG91ZC83YWJlN2UxZmU1YWViNDQ5YmVmN2Y4MjhkYmFjZWQ1OC5qcGVn/exact/600/380'
        item['SubWebsite'] = 'https://arise-homes.com/'
        item['AmenityType'] = ''
        yield item

        plan_link = 'https://arise-homes.com/plans'
        response45 = requests.request("GET", plan_link)
        res1 = HtmlResponse(url=plan_link, body=response45.content)

        sub_plan_link = res1.xpath('//*[@class="PlanCard_wrapper"]/div/div/a/@href').extract()
        for i in sub_plan_link:
            if 'http' in i:
                sub_plan_link = i
            else:
                sub_plan_link = 'https://arise-homes.com'+i
            yield scrapy.Request(url=sub_plan_link,callback=self.plan_details,meta={"SubdivisionNumber":item['SubdivisionNumber']})

    def plan_details(self,response):
        unique = str("Plan Unknown") + str(self.builderNumber)  # < -------- Changes here
        yyyyyyyyyy = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
        item = BdxCrawlingItem_Plan()
        item['unique_number'] = yyyyyyyyyy
        item['Type'] = "SingleFamily"
        item['PlanNumber'] = yyyyyyyyyy
        item['SubdivisionNumber'] = self.builderNumber
        item['PlanName'] = "Plan Unknown"
        item['PlanNotAvailable'] = 1
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = 0
        item['BaseSqft'] = 0
        item['Baths'] = 1
        item['HalfBaths'] = 1
        item['Bedrooms'] = 0
        item['Garage'] = 0
        item['Description'] = "Mowing And Lawn Care • Snow Removal • Roof And Gutter Repair & Replacement • Exterior Paint • Landscape Maintenance Landscape maintenance is of the original builder installed landscaping. Covers replacement of plant materials for the 1st year from installation These beautiful maintenance provided villas will be constructed by Aruba Homes and Authentic Homes. For more information, please give us a call at 913-277-0033 or send us a message and we'll get back to you as soon as possible!"
        item['ElevationImage'] = ""
        item['PlanWebsite'] = "https://www.boulderspringsks.com/"
        yield item

        SubdivisionNumber = response.meta['SubdivisionNumber']
        try:
            plan_name = response.xpath('//h1/text()').extract_first(default='')
        except Exception as e:
            plan_name=''
            print(e)

        try:
            baseprice  = '0'
        except Exception as e:
            baseprice = '0'
            print(e)

        try:
            BaseSqft = response.xpath('//ul[@class="list-unstyled d-flex PlanOverview_list mt-3"]/li[1]/text()').extract_first(default=0).replace(',','')
            BaseSqft = int(BaseSqft)
        except Exception as e:
            BaseSqft = 0
            print(e)
        try:
            Baths =response.xpath('//ul[@class="list-unstyled d-flex PlanOverview_list mt-3"]/li[3]/text()[1]').extract_first(default=0)
            if '-' in Baths:
                Baths =str(Baths.split('-')[-1])
            if Baths != '':
                tmp = re.findall(r"(\d+)", Baths)
                Baths = int(tmp[0])
                if len(tmp) > 1:
                    HalfBaths = 1
                else:
                    HalfBaths = 0
            else:
                Baths = 0
                HalfBaths = 0
        except Exception as e:
            Baths = 0
            HalfBaths = 0
            print(e)


        try:
            Badroom= response.xpath('//ul[@class="list-unstyled d-flex PlanOverview_list mt-3"]/li[2]/text()[1]').extract_first(default=0)
            Badroom = int(Badroom)
        except Exception as e:
            Badroom = 0
            print(e)
        try:
            Garage = 0
        except Exception as e:
            Garage= 0
            print(e)

        try:
            description = 'Arise Homes is built on the idea that your new home should be higher quality for lower cost... all through the life of your home. It begins with our 1,350 point construction checklist. Next, we use sustainable, low maintenance materials such as full size, real stone and brick around all four sides of the home. Finally, we have personalized, beautiful finishes to choose from.'
        except Exception as e:
            description='Arise Homes is built on the idea that your new home should be higher quality for lower cost... all through the life of your home. It begins with our 1,350 point construction checklist. Next, we use sustainable, low maintenance materials such as full size, real stone and brick around all four sides of the home. Finally, we have personalized, beautiful finishes to choose from.'
            print(e)

        try:
            ElevationImage = '|'.join(response.xpath('//*[@class="Carousel_thumbnailsWrapper"]//li//img/@src').extract())
        except Exception as e:
            ElevationImage = ''
            print(e)

        unique = str(int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(item['PlanName'], "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = baseprice
        item['BaseSqft'] = BaseSqft
        item['Baths'] = Baths
        item['HalfBaths'] = HalfBaths
        item['Bedrooms'] = Badroom
        item['Garage'] = Garage
        item['Description'] = description
        item['ElevationImage'] = ElevationImage
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item
            #========================================home no code che aaa ================================#
        item = BdxCrawlingItem_Spec()
        unique = str(int(hashlib.md5(bytes("12518 S Hedge Ct","utf8")).hexdigest(), 16) % (10 ** 30))
        SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SpecNumber'] = SpecNumber
        item['PlanNumber'] = yyyyyyyyyy
        item['SpecStreet1'] = "12518 S Hedge Ct"
        item['SpecCity'] = "OLATHE"
        item['SpecState'] = "KS"
        item['SpecZIP'] = "66061"
        item['SpecCountry'] = "USA"
        item['SpecPrice'] ="424900"
        item['SpecSqft'] ="0"
        item['SpecBaths'] = 3
        item['SpecHalfBaths'] =0
        item['SpecBedrooms'] = 4
        item['MasterBedLocation'] = "Down"
        item['SpecGarage'] = "0"
        item['SpecDescription'] = ""
        item['SpecElevationImage'] = "https://dlqxt4mfnxo6k.cloudfront.net/arise-homes.com/aHR0cHM6Ly9zMy5hbWF6b25hd3MuY29tL2J1aWxkZXJjbG91ZC81NGQwNDJiOTYyMTNhNzkzNTdjMTUzYzIxYmQzYjU0Ny5qcGVn/exact/2000/1125"
        item['SpecWebsite'] = "https://arise-homes.com/homes/olathe/arbor-woods/12518-s-hedge-ct"
        yield item

        item = BdxCrawlingItem_Spec()
        unique = str(int(hashlib.md5(bytes("23150 W 125th Terr", "utf8")).hexdigest(), 16) % (10 ** 30))
        SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SpecNumber'] = SpecNumber
        item['PlanNumber'] = yyyyyyyyyy
        item['SpecStreet1'] = "23150 W 125th Terr"
        item['SpecCity'] = "OLATHE"
        item['SpecState'] = "KS"
        item['SpecZIP'] = "66061"
        item['SpecCountry'] = "USA"
        item['SpecPrice'] = "429900"
        item['SpecSqft'] = "0"
        item['SpecBaths'] = 3
        item['SpecHalfBaths'] = 0
        item['SpecBedrooms'] = 4
        item['MasterBedLocation'] = "Down"
        item['SpecGarage'] = "0"
        item['SpecDescription'] = ""
        item['SpecElevationImage'] = "https://dlqxt4mfnxo6k.cloudfront.net/arise-homes.com/aHR0cHM6Ly9zMy5hbWF6b25hd3MuY29tL2J1aWxkZXJjbG91ZC81ZGVhMjVmNTE3ZmVjMzIzOGZhY2M3ODNjNWQ3OWJjMC5qcGVn/exact/2000/1125"
        item['SpecWebsite'] = "https://arise-homes.com/homes/olathe/arbor-woods/23150-w-125th-terr"
        yield item

        item = BdxCrawlingItem_Spec()
        unique = str(int(hashlib.md5(bytes("23939 W 82nd Ct", "utf8")).hexdigest(), 16) % (10 ** 30))
        SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SpecNumber'] = SpecNumber
        item['PlanNumber'] = yyyyyyyyyy
        item['SpecStreet1'] = "23939 W 82nd Ct"
        item['SpecCity'] = "LENEXA"
        item['SpecState'] = "KS"
        item['SpecZIP'] = "66227"
        item['SpecCountry'] = "USA"
        item['SpecPrice'] = "429900"
        item['SpecSqft'] = "2568"
        item['SpecBaths'] = 3
        item['SpecHalfBaths'] = 0
        item['SpecBedrooms'] = 4
        item['MasterBedLocation'] = "Down"
        item['SpecGarage'] = "0"
        item['SpecDescription'] = ""
        item['SpecElevationImage'] = "https://dlqxt4mfnxo6k.cloudfront.net/arise-homes.com/aHR0cHM6Ly9zMy5hbWF6b25hd3MuY29tL2J1aWxkZXJjbG91ZC83ZjEyYTQ1Y2E5N2MzZDRiNWJlY2FjZTliNTk5YjlkOS5qcGVn/exact/2000/1125"
        item['SpecWebsite'] = "https://arise-homes.com/homes/lenexa/trinity-landing/23939-w-82nd-ct"
        yield item



if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl arisehomes".split())

