# -*- coding: utf-8 -*-
import json
import re
import os
import hashlib

import requests
import scrapy
from lxml import html
from scrapy.http import HtmlResponse
from w3lib.html import remove_tags
import string

from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision

class BerkeyhomesSpider(scrapy.Spider):
    name = 'berkeyhomes'
    allowed_domains = ['berkeyhomes.com']
    #start_urls = ['https://www.berkeyhomes.com/']

    # start_urls = ['http://berkeyhomes.com/gallery/']
    start_urls = ['https://www.berkeycustomhomes.com/gallery/']
    builderNumber = '833105392354111898642569894497' #"58307"


    def parse(self, response):
        try:
            item = BdxCrawlingItem_subdivision()
            item['sub_Status'] = "Active"
            item['SubdivisionNumber'] = self.builderNumber
            item['BuilderNumber'] = self.builderNumber
            item['SubdivisionName'] = "No Sub Division"
            item['BuildOnYourLot'] = 0
            item['OutOfCommunity'] = 0
            item['Street1'] = '1768 Happy Valley Drive'
            item['City'] = 'Fairfield'
            item['State'] = 'OH'
            item['ZIP'] = '45014'
            item['AreaCode'] = '513'
            item['Prefix'] = "505"
            item['Suffix'] = "9995"
            item['Extension'] = ""
            item['Email'] = ""
            item['SubDescription'] = 'It has been said that “Family makes a house a home,” and BERKEY HOMES, LLC is committed to building the “perfect home” for every customer. Built on family tradition, Berkey Homes is owned and operated by brothers-in-law and long-time friends, Matt BERding and Kevin KEYes. Perfectly complementary to each other, Matt has a Bachelor’s degree in Business Management from Miami University and Kevin has a Bachelor’s degree in Construction Management from the University of Cincinnati. Before starting their own company, both Matt and Kevin gained experience and guidance from Paul Berding of Landmark Communities, Inc., a prominent and active builder in the Butler County area since 1978. Paul Berding is the father of Matt and father-in law of Kevin.  Stephanie Keyes, Matt’s sister and Kevin’s wife, has a degree from the University of Cincinnati in Architectural Engineering and is the designer and architect for Berkey Homes.  Her years of experience and love of family have armed her with the ability to help you design the home of your dreams.Sales representatives for Berkey Homes will guide you through the decision process of designing and building a home to meet your specific needs and desires.  Their professional experience is always available to ensure that you will be involved in the building process from beginning to end, so that you will receive the quality design and construction that you deserve.Berkey Homes builds custom homes on either your lot or one of our pre-owned lots in Butler, Warren, Hamilton, and Clermont counties.  From our family to yours, BERKEY HOMES proudly continues the tradition of building the “perfect home” for you and your family.  We promise to live up to our family tradition of insuring that the houses we build truly become the homes of our family of customers.'
            img = '|'.join(response.xpath('//*[@class="ngg-gallery-thumbnail"]/a/@href').extract())
            item['SubImage'] = img
            item['SubWebsite'] = 'http://berkeyhomes.com/'
            item['AmenityType'] = ''
            yield item
        except Exception as e:
            print(e)

        # planlink = 'http://berkeyhomes.com/home-plans/'
        url = "https://www.berkeycustomhomes.com/home-plans/"

        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'PHPSESSID=54a27a6t2mpe67spcjhvgi8v6af8e3qbmp2vb60ng8sg1ibout30',
            'referer': 'https://www.berkeycustomhomes.com/home-plans/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }

        r = requests.request("GET", url, headers=headers, data=payload)
        res3 = HtmlResponse(url=r.url, body=r.content)
        plan_urls = ['https://www.berkeycustomhomes.com/home-plans/ranches/','https://www.berkeycustomhomes.com/home-plans/1st-floor-master/','https://www.berkeycustomhomes.com/home-plans/2nd-floor-master/','https://www.berkeycustomhomes.com/union-village/']
        for purl in plan_urls:
            url = purl
            yield scrapy.Request(url=str(url), callback=self.plan_link, meta={'sbdn': self.builderNumber}, dont_filter=True)

    def plan_link(self,response):
        url = response.xpath('//div[@class="divSideMenu hidden-xs divCatSidemenu col-sm-3 col-md-3 col-lg-3"]/a/@href').extract()
        for i3 in url:
            url = i3
            yield scrapy.Request(url=str(url), callback=self.plans_details, meta={'sbdn': self.builderNumber}, dont_filter=True)


    def plans_details(self, response):

        # Plans == > available plans in that communities

        try:
            Type = 'SingleFamily'
        except Exception as e:
            print(e)

        try:
            PlanName = response.xpath('//h2/text()').get()
        except Exception as e:
            print(e)

        try:
            PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        except Exception as e:
            print(e)

        try:
            SubdivisionNumber = response.meta['sbdn']
        except Exception as e:
            print(e)

        try:
            PlanNotAvailable = 0
        except Exception as e:
            print(e)

        try:
            PlanTypeName = 'Single Family'
        except Exception as e:
            print(e)

        try:
            BasePrice = 0.00
        except Exception as e:
            print(e)

        try:
            BaseSqft1 = response.xpath('//*[contains(text(),"Square Feet: ")]//text()').get(default='')
            BaseSqft1 = response.xpath('//*[contains(text(),"Square Feet:")]//text()').get(default='')
            if '|' in BaseSqft1:
                BaseSqft1  = BaseSqft1.split('|')[-2].replace('Square Feet:','').strip()
                BaseSqft = re.findall(r'(\d+)', BaseSqft1)[0]
            BaseSqft = re.findall(r'(\d+)', BaseSqft1)[0]
        except Exception as e:
            BaseSqft = 0
            print(e)

        try:
            Bathroom = response.xpath('//*[contains(text(),"Bathrooms: ")]//text()').get()
            if '|' in Bathroom:
                Bathroom = Bathroom.split('|')[1].split('Bathrooms:')[1]
                tmp = re.findall(r"(\d+)", Bathroom)
                Baths = tmp[0]
                if len(tmp) > 1:
                    HalfBaths = 1
                else:
                    HalfBaths = 0

            tmp = re.findall(r"(\d+)", Bathroom)
            Baths = tmp[0]
            if len(tmp) > 1:
                HalfBaths = 1
            else:
                HalfBaths = 0
        except Exception as e:
            Baths = 0
            print(e)

        try:
            bed = response.xpath('//*[contains(text(),"Bedrooms: ")]//text()').get()
            if '|' in bed:
                bed = bed.split('|')[0].split('Bedrooms:')[1]
                Bedrooms = ''.join(re.findall(r'(\d+)', bed))
            Bedrooms = re.findall(r'(\d+)', bed)[0]
        except Exception as e:
            bed = 0
            print(e)

        try:
            Garage = 0
        except Exception as e:
            Garage = 0
            print(e)

        try:
            Description = 'It has been said that “Family makes a house a home,” and Berkey Custom Homes, LLC is committed to building the perfect home for every customer. Built on family tradition, Berkey Custom Homes is owned and operated by Kevin Keyes. Kevin has a Bachelor’s degree in Construction Management from the University of Cincinnati. Before starting his own company, Kevin gained experience and guidance from his father-in-law Paul Berding of Landmark Communities, Inc., a prominent and active builder in the Butler County area since 1978. In 2006 Kevin and his brother-in-law, Matt Berding, began Berkey Homes, LLC and successfully built homes for over 100 families.  In 2019 Matt made the decision to pursue his dream of owning and operating his own restaurant.  With Matt’s departure and Paul’s retirement, Kevin continues the family tradition of home building as Berkey Custom Homes, LLC.  His years of experience and love of family have armed him with the ability to help you create the home of your dreams.'
        except Exception as e:
            print(e)

        try:
            images1 = response.xpath('//*[@class="divMediaWrapper divMediaWrapper-below textholder-image col-xs-12 col-sm-12 fullWidth"]//img/@src').getall()
            images2 = response.xpath('//*[@class="divMediaWrapper divMediaWrapper-left textholder-image col-xs-12 col-sm-6"]//img/@src').getall()
            images3 = response.xpath('//*[@class="divMediaWrapper divMediaWrapper-left textholder-image col-xs-12 col-sm-6"]//img/@src').getall()
            for img in images2:
                images1.append(img)
            ElevationImage = "|".join(images1)
        except Exception as e:
            print(e)

        try:
            PlanWebsite = response.url #.replace('http://54.39.18.17:8050/render.html?wait=2.8&url=','')
            #PlanWebsite = response.url.replace('http://192.168.1.72:8050/render.html?url=', '')
        except Exception as e:
            print(e)

        # ----------------------- Don't change anything here --------------
        unique = str(PlanNumber) + str(SubdivisionNumber) + str(self.builderNumber) # < -------- Changes here
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
        item = BdxCrawlingItem_Plan()
        item['Type'] = Type
        item['PlanNumber'] = PlanNumber
        item['unique_number'] = unique_number  # < -------- Changes here
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanName'] = PlanName
        item['PlanNotAvailable'] = PlanNotAvailable
        item['PlanTypeName'] = PlanTypeName
        item['BasePrice'] = BasePrice
        item['BaseSqft'] = BaseSqft
        item['Baths'] = Baths
        item['HalfBaths'] = HalfBaths
        item['Bedrooms'] = Bedrooms
        item['Garage'] = Garage
        item['Description'] = Description
        item['ElevationImage'] = ElevationImage
        item['PlanWebsite'] = PlanWebsite
        yield item
        home_link = ['https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1I0mvUPPgWkiFBnOGOjVLmheG3Of0Aiuz5On1QOEOB%2Fc&KeyRid=1&SID=64a0f17d-80b4-48f8-823d-7f334b833896','https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1J70FA4uVeWomI1bWHDxPIMdC7rl3cpeBJ6xqtIAm5rS&KeyRid=1&SID=64a0f17d-80b4-48f8-823d-7f334b833896','https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1F3hcrDQ9elA0%2FO0lxdqjcsjtRlwGmJ49jh5Sh%2B%2B6baT&KeyRid=1&SID=40985949-347d-43bb-a598-e610f69e7d71','https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1LXm7sdaLtlfAf7nEEPtAgqPbqWy9hXcVgc7ti6I0N6i&KeyRid=1&SID=40985949-347d-43bb-a598-e610f69e7d71','https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2BR2ipB%2B146IOMX1nqn8ULPLeqAgRq7LmroyDuSAxFnma3SicPdkswdy7VcC5UxF%2F&KeyRid=1&SID=','https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1FSzVANdk2qyfm%2BSSJoJfOE%2FQJar1E0NMq84hAnkOCLD&KeyRid=1&SID=788622c9-5b54-499d-aca4-2c2f24e35f2c']
        for i4 in home_link:
            url = i4
            yield scrapy.Request(url=str(url), callback=self.plans_details, meta={'sbdn': self.builderNumber})

    def Home_details(self,response):
        unique = str("Plan Unknown") + str(self.builderNumber)  # < -------- Changes here
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
        item = BdxCrawlingItem_Plan()
        item['unique_number'] = unique_number
        item['Type'] = "SingleFamily"
        item['PlanNumber'] = self.builderNumber
        item['SubdivisionNumber'] = self.builderNumber
        item['PlanName'] = "Plan Unknown"
        item['PlanNotAvailable'] = 1
        item['PlanTypeName'] = 'Single Family'
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

        if response.url == 'https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1I0mvUPPgWkiFBnOGOjVLmheG3Of0Aiuz5On1QOEOB%2Fc&KeyRid=1&SID=64a0f17d-80b4-48f8-823d-7f334b833896':
            SpecStreet1 = '369 Allen St.'
            SpecCity ='Turtle Creek Twp'
            SpecState = 'OH'
            SpecZIP = '45036'

            unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = self.builderNumber
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = SpecState
            item['SpecZIP'] = SpecZIP
            item['SpecCountry'] = "USA"
            item['SpecPrice'] = 580000
            item['SpecSqft'] = 0
            item['SpecBaths'] =  2
            item['SpecHalfBaths'] = 1
            item['SpecBedrooms'] = 3
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item['SpecDescription'] = 'Berkey Custom Homes Cornell plan features over 1800 square ft. 3 Bedrooms. 2 story entry. 2nd floor laundry. Double bowl vanity & walk-in closet in master bedroom. Eat in kitchen with stainless appl. Luxury vinyl plank on 1st floor. Cul-de-sac. Cincinnati Home Builders warranty.'
            item['SpecElevationImage'] = 'https://www.berkeycustomhomes.com/media/available-homes/IMG_2166 2.jpg'
            item['SpecWebsite'] = 'https://www.berkeycustomhomes.com/available-homes/'
            yield item
        if response.url =='https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1J70FA4uVeWomI1bWHDxPIMdC7rl3cpeBJ6xqtIAm5rS&KeyRid=1&SID=64a0f17d-80b4-48f8-823d-7f334b833896':
            SpecStreet1 = ' 381 Allen St..'
            SpecCity = 'Turtle Creek Twp'
            SpecState = 'OH'
            SpecZIP = '45036'

            unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = self.builderNumber
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = SpecState
            item['SpecZIP'] = SpecZIP
            item['SpecCountry'] = "USA"
            item['SpecPrice'] = 523000
            item['SpecSqft'] = 0
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 1
            item['SpecBedrooms'] = 3
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item['SpecDescription'] = 'Berkey Custom Homes Cornell plan features over 1800 square ft. 3 Bedrooms. 2 story entry. 2nd floor laundry. Double bowl vanity & walk-in closet in master bedroom. Eat in kitchen with stainless appl. Luxury vinyl plank on 1st floor. Cul-de-sac. Cincinnati Home Builders warranty.'
            item['SpecElevationImage'] = 'https://www.berkeycustomhomes.com/media/available-homes/IMG_2166 2.jpg'
            item['SpecWebsite'] = 'https://www.berkeycustomhomes.com/available-homes/'
            yield item
        if response.url =='https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1F3hcrDQ9elA0%2FO0lxdqjcsjtRlwGmJ49jh5Sh%2B%2B6baT&KeyRid=1&SID=40985949-347d-43bb-a598-e610f69e7d71':
            SpecStreet1 = '2005 Apple Ridge Ct.'
            SpecCity = 'Monroe'
            SpecState = 'OH'
            SpecZIP = '45044'

            unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = self.builderNumber
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = SpecState
            item['SpecZIP'] = SpecZIP
            item['SpecCountry'] = "USA"
            item['SpecPrice'] = 580000
            item['SpecSqft'] = 0
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 1
            item['SpecBedrooms'] = 3
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item['SpecDescription'] = 'Berkey Custom Homes Cornell plan features over 1800 square ft. 3 Bedrooms. 2 story entry. 2nd floor laundry. Double bowl vanity & walk-in closet in master bedroom. Eat in kitchen with stainless appl. Luxury vinyl plank on 1st floor. Cul-de-sac. Cincinnati Home Builders warranty.'
            item['SpecElevationImage'] = 'https://www.berkeycustomhomes.com/media/available-homes/IMG_2166 2.jpg'
            item['SpecWebsite'] = 'https://www.berkeycustomhomes.com/available-homes/'
            yield item


        if response.url =='https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1LXm7sdaLtlfAf7nEEPtAgqPbqWy9hXcVgc7ti6I0N6i&KeyRid=1&SID=40985949-347d-43bb-a598-e610f69e7d71':
            SpecStreet1 = '4025 Andora Blvd.'
            SpecCity = 'Batavia Twp'
            SpecState = 'OH'
            SpecZIP = '45102'

            unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = self.builderNumber
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = SpecState
            item['SpecZIP'] = SpecZIP
            item['SpecCountry'] = "USA"
            item['SpecPrice'] = 295250
            item['SpecSqft'] = 2097
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 1
            item['SpecBedrooms'] = 4
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item['SpecDescription'] = 'Berkey Custom Homes - 2,097SF. 4 Bedroom. 2 Story with 2nd floor laundry room, 9ft ceilings, Large family room with fireplace, eat in kitchen with quartz countertops, 42 inch cabinets & peninsula. 3 car garage and full basement. Cincinnati Home Builders warranty.'
            item['SpecElevationImage'] = 'https://www.berkeycustomhomes.com/media/available-homes/IMG_2166 2.jpg'
            item['SpecWebsite'] = 'https://www.berkeycustomhomes.com/available-homes/'
            yield item


        if response.url == 'https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2BR2ipB%2B146IOMX1nqn8ULPLeqAgRq7LmroyDuSAxFnma3SicPdkswdy7VcC5UxF%2F&KeyRid=1&SID=':
            SpecStreet1 = '5505 Foxglove Dr.'
            SpecCity = 'Fairfield Twp'
            SpecState = 'OH'
            SpecZIP = '45011'

            unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = self.builderNumber
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = SpecState
            item['SpecZIP'] = SpecZIP
            item['SpecCountry'] = "USA"
            item['SpecPrice'] =405000
            item['SpecSqft'] = 2183
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 0
            item['SpecBedrooms'] = 3
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item['SpecDescription'] = 'Berkey Custom Homes 2183 Sq Ft 3 Bedroom Ranch with additional 1st floor study, 9ft ceilings with raised tray in family & dining room, 3 car garage. Open kitchen with 8ft island & breakfast nook with private backyard. Upgraded throughout. Immediate Occupancy'
            item['SpecElevationImage'] = 'https://www.berkeycustomhomes.com/media/available-homes/01-Exterior Front vs.jpg'
            item['SpecWebsite'] = 'https://www.berkeycustomhomes.com/available-homes/'
            yield item


        if response.url == 'https://cincy.rapmls.com/scripts/mgrqispi.dll?APPNAME=Cincynky&PRGNAME=MLSLogin&ARGUMENT=%2Fed2a85PExTLX6L7HCOW1FSzVANdk2qyfm%2BSSJoJfOE%2FQJar1E0NMq84hAnkOCLD&KeyRid=1&SID=788622c9-5b54-499d-aca4-2c2f24e35f2c':
            SpecStreet1 = '3862 Anderson St.'
            SpecCity = 'Turtle Creek Twp'
            SpecState = 'OH'
            SpecZIP = '45036'

            unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = self.builderNumber
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = SpecState
            item['SpecZIP'] = SpecZIP
            item['SpecCountry'] = "USA"
            item['SpecPrice'] =550000
            item['SpecSqft'] = 2183
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 1
            item['SpecBedrooms'] = 3
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item['SpecDescription'] = "The Georgia by Berkey Custom Homes in Union Village, a new urbanism, walkable neighborhood in Lebanon.  This classic ranch home features an open floor plan, large living room, gourmet kitchen w/island, pantry, 10' ceilings, study, 2 walk-in closets, front and side porch, & 2 car garage. To be built."
            item['SpecElevationImage'] = 'https://www.berkeycustomhomes.com/media/available-homes/Rendering.jpg'
            item['SpecWebsite'] = 'https://www.berkeycustomhomes.com/available-homes/'
            yield item



if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl berkeyhomes".split())