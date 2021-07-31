# buider no :62712
# site : americanhomestore.net


# https://www.americanhomestore.net/Cedarcanyon.html == Plan pending che

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
    name = 'americanhomestore'
    builderNumber = '62712'

    def start_requests(self):
        url = 'https://americanhomestore.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self, response):
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = ''
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 1
        item['Street1'] = '4955 Yellowstone Ave'
        item['City'] = 'Chubbuck'
        item['State'] = 'Tx'
        item['ZIP'] = '83202'
        item['AreaCode'] = '208'
        item['Prefix'] = "238"
        item['Suffix'] = "3644"
        item['Extension'] = ""
        item['Email'] = "sales@americanhomestore.net"
        item['SubDescription'] = "American Home Store, Your premier provider of off site built Champion and Kit Custom Homes with a combination of over 50 years in the housing industry, serving individuals and developers with precision quality and performance"
        item['SubImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['SubWebsite'] = response.url
        item['AmenityType'] =''
        yield item

        # url = ['https://www.americanhomestore.net/Single_LS.html','https://www.americanhomestore.net/Cedarcanyon.html','https://www.americanhomestore.net/Pinehurst.html','https://www.americanhomestore.net/grandmanor.html']
        url = ['https://www.americanhomestore.net/Single_LS.html']
        for i in  url:
            # response88 = requests.request("GET", i)
            # res33 = HtmlResponse(url=i, body=response88.content, encoding='utf-8')

            yield scrapy.Request(url=i, callback=self.plan_details,
                                     meta={"SubdivisionNumber": item['SubdivisionNumber']})

    def plan_details(self, response):
        SubdivisionNumber =self.builderNumber

        plan_name = 'ls1001'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '532'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 1
        item['Garage'] = 0
        item['Description'] =''
        item['ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cottage or LS 1002'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '660'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2022'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '587'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 1
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2023'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '747'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2025'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1178'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2039'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1157'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2051'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1178'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2052'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1178'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2053'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1157'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2054'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1178'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2056'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '880'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2058'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '800'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2070'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '532'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 1
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2071'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '660'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2078'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '836'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2079'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '787'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 1
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2080'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '905'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'LS 2081'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1062'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item




        plan_name = 'LS 2082'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '984'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cottage 1001'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '532'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 1
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cottage 1002'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '660'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2501'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2502'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2503'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2504'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1494'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2505'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1867'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2506'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2006'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2507'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1867'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2508'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1867'
        item['Baths'] = 4
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2509'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1867'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2510'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1867'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Pinehurst 2511'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1813'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6001'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1654'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6002'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1760'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6003'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1933'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6004'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2271'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6005'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2405'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6006'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2735'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6007'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2735'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6008'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2735'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6009'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1998'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6010'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2079'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6011'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1770'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6012'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2323'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Grand Manor 6013'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2756'
        item['Baths'] = 2
        item['HalfBaths'] = 1
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item


        plan_name = 'Cedar Canyon / LS 2001'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1014'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2002'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1067'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2003'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1067'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item


        plan_name = 'Cedar Canyon / LS 2002'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1067'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2004'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item


        plan_name = 'Cedar Canyon / LS 2005'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2006'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1494'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2007'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2008'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2085'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2009'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1867'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2010'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1947'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2011'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2012'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1173'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2015'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2016'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2018'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1494'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2020'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1534'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2026'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '984'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item




        plan_name = 'Cedar Canyon / LS 2021'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '984'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2027'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1023'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2028'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1215'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2029'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1420'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2030'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2032'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2034'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1888'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2042'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2242'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2043'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1961'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2044'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2085'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2046'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1652'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2048'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1173'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2055'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '960'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2057'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1770'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2059'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1778'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2060'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1778'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2061'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2242'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2062'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2667'
        item['Baths'] = 2
        item['HalfBaths'] = 1
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2063'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2085'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2064'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2006'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2065'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item['Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item


        plan_name = 'Cedar Canyon / LS 2066'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2242'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2067'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2065'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2068'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2160'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2072'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1173'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2073'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1920'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2074'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2242'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2075'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1760'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2076'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2321'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2077'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2242'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2083'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1067'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'Cedar Canyon / LS 2086'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1067'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-1602B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '800'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-1662B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '880'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-1663B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '880'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-1663B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '880'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-2683B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1003'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-2763B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1153'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'DW NB-5443'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1027'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-5483D'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1120'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4403'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1066'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4483B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4483C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4483D'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4483X'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4523B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4563B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1493'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4603B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4603F'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4603L'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4663B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1760'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-6764M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2306'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'NB-4683X'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1814'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 4483P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1280'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 4523P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1387'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 4563P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1494'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 4604P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item[
            'ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/strictly-manufactured-homes-red-bluff-champion-09-PF-3403B-500x333.jpg|https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg|https://www.americanhomestore.net/Champ%20Photos/New%20Begginings/333333.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 6483P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1456'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item['Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 6523P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1587'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 6563P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1699'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 6604P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1820'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 6604P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1820'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'HC 4604P'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1820'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '4623M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1654'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '4663M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1760'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '4704M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1867'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '4764M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2027'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '6623M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1887'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '6663M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2002'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '6704M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2024'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '6764M'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2306'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 4442C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 4482C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 4523C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 4563C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 4603C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 43
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 4644C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 6442C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 6482C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 6523C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 6563C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 6603C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1494'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'CB 6644C'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1494'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = 'DW-4483B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1200'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '4563B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1500'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '4603F'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1600'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        plan_name = '4663B'
        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1760'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/Champ%20Photos/stacked%20windows%20ext.jpg'
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl americanhomestore".split())