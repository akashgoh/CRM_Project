# builder no : 63699
# main site : builtbyhomemakers.com


import scrapy
import re
import os
import hashlib
import scrapy
from pygments.lexer import default
from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse

class HomeMakersBuildingGroupLLC(scrapy.Spider):
    name = 'HomeMakersBuildingGroupLLC'
    builderNumber = '63699'

    def start_requests(self):
        url = 'https://builtbyhomemakers.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self, response):
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = ''
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 1
        item['Street1'] = '7001-22nd St'
        item['City'] = 'Lubbock'
        item['State'] = 'TX '
        item['ZIP'] = '79407'
        item['AreaCode'] = '806'
        item['Prefix'] = "583"
        item['Suffix'] = "1144"
        item['Extension'] = ""
        item['Email'] = "sales@builtbyhomemakers.com"
        item['SubDescription'] = "Are you tired of wasting money on rent? Burned out on bidding wars in a seller’s market? We offer you the opportunity to buy your new home how you want it, instead of settling for a pre-owned home you don’t love. All our homes are in the best school districts, are safe and family oriented, and will increase in value to maximize your investment."
        item['SubImage'] = 'https://builtbyhomemakers.com/wp-content/uploads/2021/02/Addington-B-Elevation.jpg|https://builtbyhomemakers.com/wp-content/uploads/2021/02/Addington-C-Elevation.jpg'
        item['SubWebsite'] = response.url
        item['AmenityType'] =''
        yield item

        url = ['https://builtbyhomemakers.com/our-homes/bushland-springs/','https://builtbyhomemakers.com/our-homes/escondido-ranch/']
        for i in url:
            response88 = requests.request("GET", i)
            res33 = HtmlResponse(url=i, body=response88.content, encoding='utf-8')
            sub_plan_url = res33.xpath('//*[contains(text(),"View Plan")]/@href').extract()
            for i2 in sub_plan_url:
                urls= i2
                yield scrapy.Request(url=urls,callback=self.plan_details,meta={"SubdivisionNumber": item['SubdivisionNumber']})

    def plan_details(self, response):
        SubdivisionNumber = '63699'
        try:
            plan_name = response.xpath('//h1/text()').extract_first(default='')
        except Exception as e:
            plan_name = ''
            print(e)
        try:
            BasePrise = response.xpath('//div[@class="price"]/text()').extract_first(default='').replace('$','').replace(',','')
            BasePrise = int(BasePrise)
        except Exception as e:
            BasePrise = 0
            print(e)
        try:
            BaseSqft = response.xpath('//li[@class="sqft"]/text()').extract_first(default='').replace('Sq. Ft.','').replace('Sq. Ft','').replace(',','')
            BaseSqft = int(BaseSqft)
        except Exception as e:
            BaseSqft= 0
            print(e)
        try:
            Baths = response.xpath('//li[@class="bath"]/text()').extract_first(default='').replace('Bath','')
            tmp = re.findall(r"(\d+)", Baths)
            Baths = tmp[0]
            if len(tmp) > 1:
                HalfBaths = 1
            else:
                HalfBaths = 0
        except Exception as e:
            Baths = 0
            HalfBaths = 0
            print(e)
        try:
            Badroom = response.xpath('//li[@class="bed"]/text()').extract_first(default='').replace('Bed','')
            Badroom = ''.join(re.findall(r"(\d+)", Badroom))
            Badroom = int(Badroom)

        except Exception as e:
            Badroom = 0
            print(e)

        try:
            Garage = response.xpath('//li[@class="garage"]/text()').extract_first(default='').replace('Car Garage','')
            Garage = ''.join(re.findall(r"(\d+)", Garage))
            Garage = int(Garage)
        except Exception as e:
            Garage = 0
            print(e)

        try:
            description = ''.join(response.xpath('//*[@class="disclaimer"]/p/text()').extract())
        except Exception as e:
            description = 'Prices, plans, included features, options and co-broke are subject to change without notice. Square footages are approximate. Images and photos are for illustrative purposes only and may differ from home as built. Plans and included features are subject to availability and feasibility. Please see a sales representative for more information'
            print(e)
        try:
            imges = '|'.join(response.xpath('//*[@class="floorplan-thumbnail"]/img/@src|//*[@class="slick-slide slick-current slick-center"]//img/@src').extract())
        except Exception as e:
            imges = 'https://builtbyhomemakers.com/wp-content/uploads/2021/02/Briarwood-Floor-Plan.jpg'
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
    execute("scrapy crawl HomeMakersBuildingGroupLLC".split())