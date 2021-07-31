# builder no : 63700
# main site : https://www.burnetcustomhomes.com/

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
    name = 'BenchmarkCustomHomes'
    builderNumber = '63700'

    def start_requests(self):
        url = 'https://www.burnetcustomhomes.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self,response):

        print("---------- Not_Found_Community ---------")
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = 'Mathias House, 2nd Floor'
        item['City'] = 'CampalPanjim'
        item['State'] = 'NH'
        item['ZIP'] = '00000'
        item['AreaCode'] = '830'
        item['Prefix'] = "613"
        item['Suffix'] = "2082"
        item['Extension'] = ""
        item['Email'] = "sales@bnbcustomhomes.com"
        item['SubDescription'] = 'We consider ourselves very lucky to have found Cory and Benchmark Construction Co. They did a beautiful job and it was a big project, probably bigger than initially planned. He had to tear down the existing house and fence to create the construction site. A new septic system had to be installed and the well water had to be purified'
        item['SubImage'] = 'https://www.burnetcustomhomes.com/wp-content/uploads/2020/04/BurnetCustomHomes359-845x684.jpg|https://www.burnetcustomhomes.com/wp-content/uploads/2020/04/BurnetCustomHomes303-845x684.png|https://www.burnetcustomhomes.com/wp-content/uploads/2020/04/BurnetCustomHomes132-845x684.png|https://www.burnetcustomhomes.com/wp-content/uploads/2020/04/BurnetCustomHomes115-845x684.jpg'
        item['SubWebsite'] = 'https://www.burnetcustomhomes.com/'
        item['AmenityType'] = ''
        yield item

        main_plan_url = 'https://www.burnetcustomhomes.com/floor-plans/'
        response88 = requests.request("GET", main_plan_url)
        res33 = HtmlResponse(url=main_plan_url, body=response88.content, encoding='utf-8')
        # sub_plan_url = res33.xpath('//*[contains(text(),"Click for Details")]/../@href').extract()
        sub_plan_url = ['https://www.burnetcustomhomes.com/floor-plans/the-bradford/','https://www.burnetcustomhomes.com/floor-plans/the-paxton/','https://www.burnetcustomhomes.com/floor-plans/hill-country-craftsman/','https://www.burnetcustomhomes.com/floor-plans/the-landry/','https://www.burnetcustomhomes.com/floor-plans/the-dylan/','https://www.burnetcustomhomes.com/floor-plans/the-camryn/','https://www.burnetcustomhomes.com/floor-plans/the-poe/','https://www.burnetcustomhomes.com/floor-plans/the-blanco/','https://www.burnetcustomhomes.com/floor-plans/the-haas/']
        # sub_plan_url = ['https://www.burnetcustomhomes.com/floor-plans/the-camryn/']
        for i in sub_plan_url:
            url = i
            yield scrapy.Request(url=url, callback=self.plan_details,
                                 meta={"SubdivisionNumber": item['SubdivisionNumber']})
    def plan_details(self, response):
        SubdivisionNumber = response.meta['SubdivisionNumber']
        try:
            plan_name =response.xpath('//h1/text()').extract_first(default='')
        except Exception as e:
            plan_name = ''
            print(e)
        try:
            BasePrise = 0
        except Exception as e:
            BasePrise =0
            print(e)
        try:
            BaseSqft= response.xpath('//*[contains(text(),"Total Heated Area:")]/text()').extract_first(default='').replace('Total Heated Area: ','').replace(' sq. ft','').replace(',','').replace('w/ Added Bonus Room','').replace('sq. ft','')
            if BaseSqft =='':
                BaseSqft= response.xpath('//*[contains(text(),"Total Heated Area:")]/span/text()').extract_first(default='').replace('Total Heated Area: ','').replace(' sq. ft','').replace(',','').replace('w/ Added Bonus Room','').replace('sq. ft','')

            BaseSqft = ''.join(re.findall(r"(\d+)", BaseSqft))
        except Exception as e:
            BaseSqft = 0
            print(e)
        try:
            Baths = response.xpath('//*[contains(text(),"Full Bathrooms:")]/text()').extract_first(default='').replace('Full Bathrooms: ','')
            if 'or' in Baths:
                Baths = ''.join(Baths.split('or')[-1])
            if '/' in Baths:
                Baths = ''.join(Baths.split('/')[-1])
        except Exception as e:
            Baths = 0
            print(e)
        try:
            HalfBaths = response.xpath('//*[contains(text(),"Half Bathrooms:")]/text()').extract_first(default='').replace('Half Bathrooms: ','')
            if '/' in HalfBaths:
                HalfBaths =''.join( HalfBaths.split('/')[-1])
        except Exception as e:
            HalfBaths =0
            print(e)

        try:
            Badroom = response.xpath('//*[contains(text(),"Bedrooms:")]/text()').extract_first(default='').replace('Bedrooms:','')
            if '/' in Badroom:
                Badroom = ''.join(Badroom.split('/')[-1])
        except Exception as e:
            Badroom = 0
            print(e)

        try:
            Garage = response.xpath('//div[2]/div/div/div/div[9]/section/div/p[3]').extract_first(default='')
            Garage = response.xpath('//*[contains(text(),"Count:")]').extract_first().replace('Count:','').replace('cars','').replace('</p>','')
            # Garage = ''.join(re.findall(r"(\d+)", Garage))
            if '/' in Garage:
                Garage = ''.join(Garage.split('/')[-1])
                # Garage = ''.join(re.findall(r"(\d+)", Garage))
            else:
                Garage = ''.join(re.findall(r"(\d+)", Garage))

        except Exception as e:
            Garage = 0
            print(e)

        try:
            description = 'We consider ourselves very lucky to have found Cory and Benchmark Construction Co. They did a beautiful job and it was a big project, probably bigger than initially planned. He had to tear down the existing house and fence to create the construction site. A new septic system had to be installed and the well water had to be purified'
        except Exception as e:
            description =''
            print(e)
        try:
            imges = '|'.join(response.xpath('//div/div[2]/div/div/div/div[3]/div[2]/div/div/img/@src').extract())
        except Exception as e:
            imges= ''
            print(e)

        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = BasePrise
        item['BaseSqft'] = BaseSqft
        item['Baths'] = Baths
        item['HalfBaths'] = HalfBaths
        item['Bedrooms'] = Badroom
        item['Garage'] = Garage
        item['Description'] = description
        item['ElevationImage'] = imges
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl BenchmarkCustomHomes".split())

