# builderno: 62792
# main site : ascotgrp.com

# *- coding: utf-8 -*-
import scrapy
import re
import os
import hashlib
import scrapy
# from pygments.lexer import default

from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse


class ascotgrp(scrapy.Spider):
    name = 'ascotgrp'
    builderNumber = '62792'

    def start_requests(self):
        url = 'https://www.ascotgrp.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self,response):
        # ============================ Street_Address Not Availble In Any Comm.=======================
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = '30 Country Club Blvd'
        item['City'] = 'Whispering Pines'
        item['State'] = 'NC'
        item['ZIP'] = '28327'
        item['AreaCode'] = '910'
        item['Prefix'] = "688"
        item['Suffix'] = "7361"
        item['Extension'] = ""
        item['Email'] = "info@ascotgrp.com"
        item['SubDescription'] = 'ASCOT ranks among the top builders in Moore County, NC. We specialize in the design and construction of distinctive, affordable homes from the high $200’s to low $400’s though we have built million dollar homes too.'
        img ='|'.join(response.xpath('//*[@class="container"]//div[@class="flex-column-33 home-images-item"]//img/@src').extract())
        item['SubImage'] = img
        item['SubWebsite'] = 'https://www.ascotgrp.com/'
        item['AmenityType'] = ''
        yield item

        plan_url = 'https://www.ascotgrp.com/home-plans/'
        yield scrapy.Request(url=plan_url,callback=self.plan_links,meta={'SubdivisionNumber':item['SubdivisionNumber']})


    def plan_links(self,response):
        SubdivisionNumber = response.meta['SubdivisionNumber']
        print("Sub_plna_no:",SubdivisionNumber)
        plan_links = response.xpath('//*[@class="flex-column-25 homeplans-overview"]/a/@href').extract()
        for i in plan_links:
            plan_link = i
            yield scrapy.Request(url=plan_link,callback=self.plan_details,meta={'SubdivisionNumber':SubdivisionNumber})

    def plan_details(self,response):
        SubdivisionNumber = response.meta['SubdivisionNumber']
        print("Plan_detail:",SubdivisionNumber)
        try:
            plan_name = response.xpath('//div[@class="community-details"]//h2/text()').extract_first(default='')
        except Exception as e:
            plan_name = ''
            print(e)
        try:
            baseprice = response.xpath('//*[contains(text(),"Starting Price")]/strong/text()').extract_first(default=0).replace(',','').replace('$','')
            baseprice =int(baseprice)
        except Exception as e:
            baseprice=0
            print(e)
        try:
            BaseSqft= response.xpath('//*[contains(text(),"Sq. Ft. Range")]/strong/text()').extract_first(default=0).replace('Sq. Ft. Range','')
            if '-'in BaseSqft:
                BaseSqft = str(BaseSqft.split('-')[-1])
            BaseSqft = int(BaseSqft)
        except Exception as e:
            BaseSqft = 0
            print(e)
        try:
            Baths = response.xpath('//*[contains(text(),"Bath")]/strong/text()').extract_first(default='').strip()
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
            Badroom =response.xpath('//*[contains(text(),"Bed")]/strong/text()').extract_first(default=0).replace('Bedrooms:','')
            if '-' in Badroom:
                Badroom = str(Badroom.split('-')[-1])
            if 'or' in Badroom:
                Badroom = Badroom.split(' or ')[-1]

            Badroom = ''.join((re.findall(r"(\d+)", Badroom)))
        except Exception as e:
            Badroom = 0
            print(e)
        try:
            Garage = response.xpath('//*[contains(text(),"Garages")]/strong/text()').extract_first(default=0).replace('-Car','').strip()
            if '-'in Garage:
                Garage = Garage.split('-')[-1]
            Garage = int(''.join(re.findall(r"(\d+)", Garage)))
        except Exception as e:
            Garage =0
            print(e)
        try:
            description = '|'.join(response.xpath('//*[contains(text(),"Description")]/../p/text()').extract()[0:1000]).strip()
        except Exception as e:
            description = ''
            print(e)
        try:
            ElevationImage = '|'.join(response.xpath('//*[@class="slider slider-nav slick-initialized slick-slider"]/div//div/img/@src').extract()).replace('\xa0','')
            if ElevationImage =='':
                ElevationImage = '|'.join(response.xpath('//div[@class="slider slider-for"]//img/@src|//div[@class="slider slider-nav"]/img/@src').extract())
        except Exception as e:
            ElevationImage = ''
            print(e)

        unique = str(int(hashlib.md5(bytes(response.url+plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = str(plan_name).strip()
        # item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['PlanNumber'] = unique_number
        print("plan_number:",item['PlanNumber'])
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

        if plan_name == 'Essex':
            home_plan_url = 'https://www.ascotgrp.com/inventory/258-cameron-avenue/'
            yield scrapy.Request(url=home_plan_url,callback=self.home_details,meta={"SubdivisionNumber":item['SubdivisionNumber'],"PlanNumber":item['PlanNumber'],"Planname":item['PlanName']})

    def home_details(self,response):
        pn = response.meta['Planname']
        plan = response.xpath('//*[contains(text(),"Home Plan:")]/a/text()').get().strip()
        if str(pn) in str(plan):
            PlanNumber = response.meta['PlanNumber']
            try:
                SpecStreet1 = response.xpath('//*[@class="community-details"]/h2/text()').extract_first(default='')
            except Exception as e:
                SpecStreet1 = ''
                print(e)
            try:
                SpecCity = response.xpath('//*[@class="community-details"]/h3/text()').extract_first(default='').split(',')[0]
            except Exception as e:
                SpecCity = ''
                print(e)
            try:
                SpecState =response.xpath('//*[@class="community-details"]/h3/text()').extract_first(default='').split(',')[1].strip()
            except Exception as e:
                SpecState = ''
                print(e)

            try:
                SpecZIP = 00000
            except Exception as e:
                print(e)

            try:
                SpecPrice = str(response.xpath('//div[@class="flex-row flex-top community-details-section pricing-sqft"]//*[contains(text(),"Price")]/strong/text()').extract_first(default=0).replace('$','').replace(',',''))
                SpecPrice = int(SpecPrice)
            except Exception as e:
                SpecPrice = 0
                print(e)
            try:
                SpecSqft = str(response.xpath('//div[@class="flex-row flex-top community-details-section pricing-sqft"]//*[contains(text(),"Square Feet")]/strong/text()').extract_first(default=0).replace(',',''))
                SpecSqft = int(SpecSqft)
            except Exception as e:
                SpecSqft = 0
                print(e)
            try:
                SpecBaths =str(response.xpath('//div[@class="flex-row flex-top community-details-section bed-bath-sqft"]//*[contains(text(),"Bath")]/strong/text()').extract_first(default=0))
                SpecBaths = int(SpecBaths)
                SpecHalfBaths = 0
            except Exception as e:
                SpecBaths = 0
                SpecHalfBaths =0
                print(e)
            try:
                bad =response.xpath('//div[@class="flex-row flex-top community-details-section bed-bath-sqft"]//*[contains(text(),"Bed")]/strong/text()').extract_first(default=0)
                bad = int(bad)
            except Exception as e:
                bad = 0
                print(e)
            try:
                SpecGarage = str(response.xpath('//div[@class="flex-row flex-top community-details-section bed-bath-sqft"]//*[contains(text(),"Garages")]/strong/text()').extract_first(default=0))
                # SpecGarage = int(SpecGarage)
            except Exception as e:
                SpecGarage = 0
                print(e)
            try:
                SpecDescription = '|'.join(response.xpath('//*[contains(text(),"Description")]/../p[1]/text()').extract())
            except Exception as e:
                SpecDescription = ''
                print(e)
            try:
                # SpecElevationImage= '|'.join(response.xpath('//div[@class="slider slider-for"]/img/@src|//div[@class="slider slider-nav"]/img/@src').extract())
                SpecElevationImage= 'https://www.ascotgrp.com/wp-content/uploads/2020/11/Essex-B-3-car-1st-fl-750x510.jpg|https://www.ascotgrp.com/wp-content/uploads/2020/11/Essex-B-3-car-1st-fl-750x510.jpg|https://www.ascotgrp.com/wp-content/uploads/2020/11/Essex-B-3-car-1st-fl-360x240.jpg|https://www.ascotgrp.com/wp-content/uploads/2020/11/Essex-2nd-fl-360x240.png'
            except Exception as e:
                SpecElevationImage = ''
                print(e)

            unique = str(SpecStreet1) + str(SpecCity)
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = PlanNumber
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = SpecState
            item['SpecZIP'] = "00000"
            item['SpecCountry'] = 'USA'
            item['SpecPrice'] =SpecPrice
            item['SpecSqft'] =SpecSqft
            item['SpecBaths'] =SpecBaths
            item['SpecHalfBaths'] =SpecHalfBaths
            item['SpecBedrooms'] =bad
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = SpecGarage
            item['SpecDescription'] =SpecDescription
            item['SpecElevationImage'] =SpecElevationImage
            item['SpecWebsite'] = response.url
            item['unique_number'] =int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            yield item


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl ascotgrp".split())



