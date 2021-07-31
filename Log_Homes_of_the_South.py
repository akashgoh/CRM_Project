
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
    name = 'Log_Homes_of_the_South'
    builderNumber = '62868'

    def start_requests(self):
        url = 'https://loghomesofthesouth.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)


    def comm_details(self, response):
        print("---------- Not_Found_Community ---------")
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = '7521 Broad River Rd'
        item['City'] = 'Irmo'
        item['State'] = 'SC'
        item['ZIP'] = '29063'
        item['AreaCode'] = '855'
        item['Prefix'] = "324"
        item['Suffix'] = "8200"
        item['Extension'] = ""
        item['Email'] = "theloghead@bellsouth.net"
        item['SubDescription'] = 'Log Homes offers milled packages in various log styles and dimensions and features the companys unique "Profiled" Saddle Notch Corner System. With it’s comprehensive selection of individual log wall systems, capped off by a total systems material package that includes almost everything from sill plates to porch supports, Log Homes of the South offers the finest log home you can build.'
        # img = '|'.join("https://loghomesofthesouth.com"+response.xpath('//*[@id="slider1"]/ul/li/div/div/@src').extract())
        img = response.xpath('//*[@id="slider1"]/ul/li/div/div/@src').extract()
        img =list()
        for i in img:
            img.append("https://loghomesofthesouth.com"+i)
        item['SubImage'] = '|'.join(img)
        item['SubWebsite'] = 'https://loghomesofthesouth.com/'
        item['AmenityType'] = ''
        yield item


        main_plan_url ='https://loghomesofthesouth.com/Floorplans/Planbook-Models'
        response88 = requests.request("POST", main_plan_url)
        res33 = HtmlResponse(url=main_plan_url, body=response88.content, encoding='utf-8')
        # plan_url = res33.xpath('//*[@class="row normal-gallery gallery-v4"]/a/@href').extract()
        plan_url = ['https://loghomesofthesouth.com/floorplans/detail/23','https://loghomesofthesouth.com/floorplans/detail/24','https://loghomesofthesouth.com/floorplans/detail/25','https://loghomesofthesouth.com/floorplans/detail/26','https://loghomesofthesouth.com/floorplans/detail/27','https://loghomesofthesouth.com/floorplans/detail/28','https://loghomesofthesouth.com/floorplans/detail/29','https://loghomesofthesouth.com/floorplans/detail/30','https://loghomesofthesouth.com/floorplans/detail/31','https://loghomesofthesouth.com/floorplans/detail/32','https://loghomesofthesouth.com/floorplans/detail/33','https://loghomesofthesouth.com/floorplans/detail/34']
        for i in plan_url:
            # if '.pdf' in i:
            #     pass
            # else:
            #     url1231 = "https://loghomesofthesouth.com/" + i
            yield scrapy.Request(url=str(i),callback=self.plan_details,meta={"SubdivisionNumber":item['SubdivisionNumber']})

    def plan_details(self,response):
        SubdivisionNumber =response.meta['SubdivisionNumber']

        try:
            plan_name = response.xpath('//h2/text()').extract_first(default='')
        except  Exception as e:
            plan_name=''
            print(e)
        try:
            main_lin = response.xpath('//div[@class="img-holder"]/../p/text()').extract_first(default='')
            if '|' in main_lin:
                BaseSqft = main_lin.split('|')[-1].split('sq. ft.')[0].replace(',','').replace(' ','')
                if BaseSqft =='':
                    BaseSqft = main_lin.split('|')[-1].split('Sq. Ft')[0].replace(',','').replace(' ','')
                Baths = main_lin.split('|')[-2].split('Bathrooms')[0]
                tmp = re.findall(r"(\d+)", Baths)
                Baths = tmp[0]
                if len(tmp) > 1:
                    HalfBaths = 1
                else:
                    HalfBaths = 0

                Badroom = main_lin.split('|')[0].split('Bedrooms')[0]
                Badroom = int(''.join(re.findall(r"(\d+)", Badroom)))
        except Exception as e:
            BaseSqft = 0
            Baths =0
            HalfBaths = 0
            Badroom = 0
            print(e)
        try:
            description = 'Log Homes offers milled packages in various log styles and dimensions and features the companys unique "Profiled" Saddle Notch Corner System. With it’s comprehensive selection of individual log wall systems, capped off by a total systems material package that includes almost everything from sill plates to porch supports, Log Homes of the South offers the finest log home you can build.'
        except Exception as e:
            description = ''
            print(e)

        try:
            imges = list()
            img=response.xpath('//*[@class="img-holder"]//img/@src').extract()
            for i in img:
                if 'http' in i:
                    url = i
                else:
                    url = 'https://loghomesofthesouth.com/'+i
                imges.append(url)
            imges = '|'.join(imges)

        except Exception as e:
            img = ''
            print(e)



        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] =SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = BaseSqft
        item['Baths'] = Baths
        item['HalfBaths'] = HalfBaths
        item['Bedrooms'] = Badroom
        item['Garage'] = 0
        item['Description'] = description
        item['ElevationImage'] = imges
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl Log_Homes_of_the_South".split())

