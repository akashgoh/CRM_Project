# builder n : 63696

import scrapy
import re
import os
import hashlib
import scrapy
from pygments.lexer import default
from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse


class SummitHomeBuilders(scrapy.Spider):
    name = 'SummitHomeBuilders'
    builderNumber = '63696'

    def start_requests(self):
        url = 'https://buildwithsummit.com/' #<<----- Community link
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
        item['Street1'] = '2255 Simpson Ave'
        item['City'] = ' North Port'
        item['State'] = 'FL'
        item['ZIP'] = '34286'
        item['AreaCode'] = '941'
        item['Prefix'] = "504"
        item['Suffix'] = "7309"
        item['Extension'] = ""
        item['Email'] = "SummitHomesFL@Gmail.com"
        item['SubDescription'] = 'It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
        item['SubImage'] = 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/040efe56-853c-4f11-ae05-e0934d64525c.jpg/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/Logo2018Big.png/:/rs=w:529,h:200,cg:true,m/cr=w:529,h:200/qt=q:95'
        item['SubWebsite'] = 'https://buildwithsummit.com/'
        item['AmenityType'] = ''
        yield item


        main_plan_url = 'https://buildwithsummit.com/floor-plans-2'
        response88 = requests.request("GET", main_plan_url)
        res33 = HtmlResponse(url=main_plan_url, body=response88.content, encoding='utf-8')
        plan_url = res33.xpath('//*[contains(text(),"See Plan Details")]/..//@href').extract()
        plan_url1=['https://buildwithsummit.com/the-siesta']
        for i in plan_url:
            url = "https://buildwithsummit.com"+i
            plan_url1.append(url)
            for i1 in plan_url1:
                url1 = i1
                yield scrapy.Request(url=str(url1),callback=self.plan_details,meta={"SubdivisionNumber":item['SubdivisionNumber']})

    def plan_details(self, response):
        SubdivisionNumber = response.meta['SubdivisionNumber']

        if response.url == 'https://buildwithsummit.com/the-maria':
            plan_name ='The Maria'
            BasePrice='260000'
            BaseSqft = 2444
            Baths=2
            HalfBaths=0
            Badroom = 3
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            # imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'
            imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item


        if response.url == 'https://buildwithsummit.com/the-elena':
            plan_name ='The Elena'
            BasePrice='279900'
            BaseSqft =2434
            Baths=2
            HalfBaths=0
            Badroom = 3
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            # imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'
            imges = 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item

        if response.url == 'https://buildwithsummit.com/the-foxtail-1':
            plan_name ='The Foxtail'
            BasePrice='240000'
            BaseSqft =2212
            Baths=2
            HalfBaths=0
            Badroom = 3
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            imges = 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item
        if response.url == 'https://buildwithsummit.com/the-cascade':
            plan_name ='The cascade'
            BasePrice='261000'
            BaseSqft =2276
            Baths=2
            HalfBaths=0
            Badroom = 3
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            imges = 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item

        if response.url == 'https://buildwithsummit.com/the-siesta':
            plan_name ='The SiestaMajor'
            BasePrice='520000'
            BaseSqft =4445
            Baths=4
            HalfBaths=0
            Badroom = 3
            garage =3
            description ='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item

        if response.url == 'https://buildwithsummit.com/the-winchester':
            plan_name ='The Winchester'
            BasePrice='272000'
            BaseSqft =2300
            Baths=2
            HalfBaths=0
            Badroom = 3
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item

        if response.url == 'https://buildwithsummit.com/the-magnolia':
            plan_name ='The Magnolia'
            BasePrice='322000'
            BaseSqft =2794
            Baths=2
            HalfBaths=1
            Badroom = 3
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item

        if response.url == 'https://buildwithsummit.com/the-royal':
            plan_name ='The-royal'
            BasePrice='379000'
            BaseSqft =3227
            Baths=2
            HalfBaths=1
            Badroom = 3
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item

        if response.url == 'https://buildwithsummit.com/the-palmetto':
            plan_name ='The palmetto'
            BasePrice='258900'
            BaseSqft =2247
            Baths=2
            HalfBaths=0
            Badroom = 2
            garage =2
            description='It would be our pleasure to see you in person! Contact us and we can set up an appointment and meet! Meet the Home builder. We can talk over any questions you may have and show you in more detail what we can offer you! We can meet you where ever you are. Either in Sarasota North Port or Venice. Or in one of our model homes!'
            imges= 'https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1209.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1187.jpg/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/blob-0001.png/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/IMG_1171.JPG/:/rs=w:370,cg:true,m|https://img1.wsimg.com/isteam/ip/51527139-0db6-4341-a38c-765e468eb0e5/D40A4E49-FA6E-4918-88E9-7F7D484DE295.JPEG/:/rs=w:370,cg:true,m'

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = garage
            item['Description'] = description
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item



if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl SummitHomeBuilders".split())