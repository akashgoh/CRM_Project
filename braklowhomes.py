# -*- coding: utf-8 -*-
import hashlib
import re
import json
import requests
from scrapy.http import HtmlResponse
import scrapy
from scrapy.utils.response import open_in_browser
from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec
from lxml import html
import datetime
import html2text



class braklowhomes(scrapy.Spider):
    name = 'braklowhomes'
    allowed_domains = ['www.braklowhomes.com']
    start_urls = ['https://braklowhomes.com/community/']

    builderNumber = "49261"

    def parse(self, response):
        link = 'https://braklowhomes.com/community/'
        yield scrapy.Request(url=str(link), callback=self.all_comm, dont_filter=True)

    def all_comm(self,response):
        a = re.findall('{"thumbnail":"h(.*?)lng":"-94.69339276184076"}}]', response.text)[0]
        b = re.findall(',"address":(.*?),"lat_long', a)
        b = list(b)
        links = response.xpath('//div[@class="container"]/a/@href').getall()

        for links,b in zip(links,b):
            link = links
            print(links)
            # links = 'https://braklowhomes.com/community/mills-farm/'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                # 'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
            }
            response45 = requests.request("GET", link,headers=headers)
            res1 = HtmlResponse(url=links, body=response45.content)

            if res1.url=='https://braklowhomes.com/community/mills-farm/':
                state = 'Ks'
                images = ''
                image = re.findall('url(\(.*?)\)', res1.text)
                for i in image:
                    images = images + i + '|'
                images = images.strip('|').replace('(', '').replace(')', '')

                subdivisonNumber = int(hashlib.md5(bytes(str('Mills Farm') + str(self.builderNumber), "utf8")).hexdigest(), 16) % ( 10 ** 30)
                item2 = BdxCrawlingItem_subdivision()
                item2['sub_Status'] = "Active"
                item2['SubdivisionName'] = 'Mills Farm'
                item2['SubdivisionNumber'] = subdivisonNumber
                item2['BuilderNumber'] = self.builderNumber
                item2['BuildOnYourLot'] = 0
                item2['OutOfCommunity'] = 1
                item2['Street1'] = 'Overland Park'
                item2['City'] = ''
                item2['State'] = state
                item2['ZIP'] = '66213'
                item2['AreaCode'] = '913'
                item2['Prefix'] = '375'
                item2['Suffix'] = '5531'
                item2['Extension'] = ""
                item2['Email'] = 'lisa@braklowhomes.com'
                item2['SubDescription'] = ''.join(res1.xpath('//div[@class="ll-features-content__container"]//text()').getall())
                item2['SubImage'] = images
                item2['SubWebsite'] = res1.url
                a = []
                try:
                    aminity = ''.join(res1.xpath('//*[@class="ll-features-content__half right col-md-1of2"]/ul[1]/li/text()|//*[@class="ll-features-content__container"]//ul/li//text()|//*[@class="ll-features-content__half left col-md-1of2"]//p/text()').extract())
                except Exception as e:
                    aminity = ''
                    print(e)

                amenity_list = ["Pool", "Playground", "GolfCourse", "Tennis", "Soccer", "Volleyball","Basketball","Baseball", "Views", "Lake", "Pond", "Marina", "Beach", "WaterfrontLots","Park","Trails", "Greenbelt", "Clubhouse", "CommunityCenter"]
                for i in amenity_list:
                    if i in aminity:
                        a.append(i)
                av = '|'.join(a)
                if av != '':
                    item2['AmenityType'] = av
                else:
                    item2['AmenityType'] = ''
                yield item2

                link = 'https://braklowhomes.com/floorplan/'
                yield scrapy.FormRequest(url=str(link), callback=self.all_plan, dont_filter=True)

                # ============================No Manully========================================



            street_add =res1.xpath('//*[contains(text(),"Location")]/../address/span[1]/text()').extract_first(default='')
            if street_add =='':
                street_add = res1.xpath('//*[contains(text(),"Location")]/../address/span[2]/text()').extract_first(default='')


            if street_add:
                d = res1.xpath('//*[contains(text(),"Location")]/../address/span[2]/text()').extract()
                dd = int(len(d))
                if dd==1:
                    city_state = d[0]
                    city =city_state.split(', ')[0]
                    if city=='':
                        city = city_state.split(',')[0]
                    state = 'ks'


                    zip1 = res1.xpath('//*[contains(text(),"Location")]/../address/span[3]/text()').extract_first(default='')
                    if zip1 == "":
                        zip1 = 00000

                    images = ''
                    image = re.findall('url(\(.*?)\)', res1.text)
                    for i in image:
                        images = images + i + '|'
                    images = images.strip('|').replace('(', '').replace(')', '')

                    find_json = re.findall('<script type="application/ld\+json">(.*?)</script>', response.text)[0]
                    body = json.loads(find_json)
                    subdivisonName = res1.xpath('//h1[@class="ll-hero-banner__small-heading heading heading--small text-white"]//text()').get()
                    comm_id = res1.url
                    Street1 = street_add

                    subdivisonNumber = int(hashlib.md5(bytes(str(subdivisonName) + str(self.builderNumber), "utf8")).hexdigest(), 16) % (10 ** 30)
                    item2 = BdxCrawlingItem_subdivision()
                    item2['sub_Status'] = "Active"
                    item2['SubdivisionName'] = subdivisonName
                    item2['SubdivisionNumber'] = subdivisonNumber
                    item2['BuilderNumber'] = self.builderNumber
                    item2['BuildOnYourLot'] = 0
                    item2['OutOfCommunity'] = 1
                    item2['Street1'] = Street1
                    item2['City'] = city
                    item2['State'] =state
                    item2['ZIP'] = zip1
                    item2['AreaCode'] = '913'
                    item2['Prefix'] = '375'
                    item2['Suffix'] = '5531'
                    item2['Extension'] = ""
                    item2['Email'] = 'lisa@braklowhomes.com'
                    item2['SubDescription'] = ''.join(res1.xpath('//div[@class="ll-features-content__container"]//text()').getall())
                    item2['SubImage'] = images
                    item2['SubWebsite'] = res1.url
                    a = []
                    try:
                        aminity = ''.join(res1.xpath('//*[@class="ll-features-content__half right col-md-1of2"]/ul[1]/li/text()|//*[@class="ll-features-content__container"]//ul/li//text()|//*[@class="ll-features-content__half left col-md-1of2"]//p/text()').extract())
                    except Exception as e:
                        aminity = ''
                        print(e)

                    amenity_list = ["Pool", "Playground", "GolfCourse", "Tennis", "Soccer", "Volleyball",
                                    "Basketball",
                                    "Baseball", "Views", "Lake", "Pond", "Marina", "Beach", "WaterfrontLots",
                                    "Park",
                                    "Trails", "Greenbelt", "Clubhouse", "CommunityCenter"]
                    for i in amenity_list:
                        if i in aminity:
                            a.append(i)
                    av = '|'.join(a)
                    if av != '':
                        item2['AmenityType'] = av
                    else:
                        item2['AmenityType'] = ''

                    yield item2

                    link = 'https://braklowhomes.com/floorplan/'
                    yield scrapy.FormRequest(url=str(link), callback=self.all_plan, dont_filter=True)
            else:
                print('No address: ',links)



    def all_plan(self,response):
        # images = ''
        # image = response.xpath('//*[contains(@src,"wixstatic")]/@src').extract()
        # for i in image:
        #     images = images + self.start_urls[0] + i + '|'
        # images = images.strip('|')

        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = ''
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = "6950 W. 152nd Terr"
        item['City'] = "Overland Park"
        item['State'] = "KS"
        item['ZIP'] = "66223"
        item['AreaCode'] = "913"
        item['Prefix'] = "375"
        item['Suffix'] = "5531"
        item['Extension'] = ""
        item['Email'] = "lisa@braklowhomes.com"
        item['SubDescription'] = "At Braklow Custom Homes, we realize our reputation is only as good as the last deal. That's why we have spent countless hours training our production staff to ensure the entire building process runs smoothly; which begins at our initial meeting to the final walk-thru. Our staff is fully committed to open and clear communication throughout the building process. Whether you're looking for a 1.5 story, 2 story, or reverse 1.5 story home, feel free to give us a call and we can set up a free home consultation to discuss any questions you may have."
        item['SubImage'] = 'https://braklowhomes.com/wp-content/uploads/2018/08/logo-color.png'
        item['SubWebsite'] = ""

        a = []
        # aminity = ''.join(response.xpath('//*[@class="ll-features-content__half right col-md-1of2"]/ul[1]/li/text()').extract())
        try:
            aminity = ''.join(response.xpath('//*[@class="ll-features-content__half right col-md-1of2"]/ul[1]/li/text()|//*[@class="ll-features-content__container"]//ul/li//text()|//*[@class="ll-features-content__half left col-md-1of2"]//p/text()').extract())
        except Exception as e:
            print(e)

        amenity_list = ["Pool", "Playground", "GolfCourse", "Tennis", "Soccer", "Volleyball", "Basketball",
                        "Baseball", "Views", "Lake", "Pond", "Marina", "Beach", "WaterfrontLots", "Park",
                        "Trails", "Greenbelt", "Clubhouse", "CommunityCenter"]
        for i in amenity_list:
            if i in aminity:
                a.append(i)
        ab = '|'.join(a)
        item['AmenityType'] = ab
        yield item

        links = response.xpath('//div[@class="container row"]/a/@href').getall()
        for link in links:
            link=link
            yield scrapy.FormRequest(url=str(link), callback=self.process_plan,dont_filter=True,meta={'subdivisonNumber':self.builderNumber})


    def process_plan(self, response):
        try:
            SubdivisionNumber = response.meta['subdivisonNumber']
            item = BdxCrawlingItem_Plan()
            try:
                PlanName = response.xpath('//h1[@class="ll-hero-banner__large-heading heading heading--hero text-white"]/text()').get()
            except Exception as e:
                PlanName =''
            a = response.xpath('//div[@class="ll-features-content__spec-flex row"]//text()').getall()

            try:
                BaseSqft = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][1]//span[2]/text()').get()
            except Exception as e:
                BaseSqft = 0

            try:
                Baths = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][5]//span[2]/text()').get()
                tmp = re.findall(r"(\d+)", Baths)
                Baths = tmp[0]
                if len(tmp) > 1:
                    HalfBaths = 1
                else:
                    HalfBaths = 0
            except Exception as e:
                print(e)
                Baths = ''
                HalfBaths = ''

            try:
                Bedrooms = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][4]//span[2]/text()').get()
            except Exception as e:
                Bedrooms = 0

            try:
                Garage = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][6]//span[2]/text()').get()
            except Exception as e:
                Garage = 0

            try:
                Description = "At Braklow Custom Homes, we realize our reputation is only as good as the last deal. That's why we have spent countless hours training our production staff to ensure the entire building process runs smoothly; which begins at our initial meeting to the final walk-thru. Our staff is fully committed to open and clear communication throughout the building process. Whether you're looking for a 1.5 story, 2 story, or reverse 1.5 story home, feel free to give us a call and we can set up a free home consultation to discuss any questions you may have. We also provide free lot evaluations. If you already own land, or are in the process of selecting a lot for your new home, please contact us to arrange a free lot evaluation of your property to determine the best possible building site and design for your new home."
            except Exception as e:
                Description=''
            try:
                BasePrice = response.xpath('//*[contains(text(),"Price:")]/../span[2]/text()').extract_first(default=0).replace(',','').replace('+','')
            except Exception as e:
                BasePrice = 0
                print(e)

            try:
                ElevationImage2 = re.findall('url(\(.*?)\)',response.text)
                ElevationImage2 = '|'.join(ElevationImage2).replace(')','').replace('(','')
                ElevationImage2 = ElevationImage2.strip('|')
            except Exception as e:
                ElevationImage2 = ""


            PlanNumber = int(hashlib.md5(bytes(str(PlanName), "utf8")).hexdigest(), 16) % (10 ** 30)
            unique = str(PlanNumber) + str(SubdivisionNumber)
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
            item = BdxCrawlingItem_Plan()
            item['Type'] = "SingleFamily"
            item['PlanNumber'] = PlanNumber
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = PlanName
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Bedrooms
            item['Garage'] = Garage
            item['Description'] = Description
            item['ElevationImage'] = ElevationImage2
            item['PlanWebsite'] = response.url
            yield item

            link = 'https://braklowhomes.com/available/'
            yield scrapy.FormRequest(url=str(link), callback=self.all_home, dont_filter=True,
                                     meta={'PN': unique_number})
        except Exception as e:
                print("process_plan",e,response.url)

    def all_home(self, response):
        PN = response.meta['PN']
        a = ''.join(re.findall('{"thumbnail":"h(.*?)lng":"-94.72086176878662"}',response.text))
        b = re.findall(',"address":(.*?),"lat_long', a)
        b = list(b)
        links = response.xpath('//div[@class="container row"]/a/@href').getall()
        for links,b in zip(links,b):
            links = links
            b = b
            data = json.loads(b)
            street_add = data['street_address']
            city = data['city']
            state = data['state']
            zip1 = data['zip']
            yield scrapy.Request(url=str(links), callback=self.process_home, dont_filter=True, meta={'PN': PN,'street_add':street_add,'city':city,'state':state,'zip1':zip1})


    def process_home(self, response):
        unique = str("Plan Unknown") + str(self.builderNumber)  # < -------- Changes here
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # <-------- Changes here
        item = BdxCrawlingItem_Plan()
        item['unique_number'] = unique_number
        item['Type'] = "SingleFamily"
        item['PlanNumber'] = "Plan Unknown"
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
        try:
            if 'SOLD' not in response.text:
                a = re.findall('title" content="(.*?)"',response.text)[0]

                SpecStreet1 = response.meta['street_add']

                SpecCity = response.meta['city']

                SpecState = response.meta['state']

                SpecZIP = response.meta['zip1']

                unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
                SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

                SpecCountry = "USA"

                try:
                    SpecPrice = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][3]//span[2]/text()').get().replace('$','').replace(',','').replace('Million','').strip().replace('Low','')

                    if '.' in SpecPrice:
                        SpecPrice = float(SpecPrice)
                        SpecPrice *= float(1000000.00)
                        SpecPrice = str(SpecPrice)

                    if 'k' in SpecPrice:
                        SpecPrice = SpecPrice.replace('k','')
                        SpecPrice = int(SpecPrice)
                        SpecPrice = SpecPrice * 1000
                        SpecPrice = str(SpecPrice)
                    SpecPrice = re.findall(r"(\d+)", SpecPrice)[0]

                except Exception as e:
                    print(e)
                    SpecPrice = 0

                try:
                    SpecSqft = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][1]//span[2]/text()').get()
                except Exception as e:
                    SpecSqft = 0

                try:
                    SpecBaths = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][5]//span[2]/text()').get()
                    tmp = re.findall(r"(\d+)", SpecBaths)
                    SpecBaths = tmp[0]
                    if len(tmp) > 1:
                        SpecHalfBaths = 1
                    else:
                        SpecHalfBaths = 0
                except Exception as e:
                    print(e)
                    SpecBaths = ''
                    SpecHalfBaths = ''

                try:
                    SpecBedrooms =response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][4]//span[2]/text()').get()
                except Exception as e:
                    SpecBedrooms = 0

                try:
                    MasterBedLocation = "Down"
                except Exception as e:
                    print(e)

                try:
                    SpecGarage = response.xpath('//div[@class="ll-features-content__spec-section col-xs-1of3"][6]//span[2]/text()').get()
                except Exception as e:
                    SpecGarage = 0

                try:
                    SpecDescription = "At Braklow Custom Homes, we realize our reputation is only as good as the last deal. That's why we have spent countless hours training our production staff to ensure the entire building process runs smoothly; which begins at our initial meeting to the final walk-thru. Our staff is fully committed to open and clear communication throughout the building process. Whether you're looking for a 1.5 story, 2 story, or reverse 1.5 story home, feel free to give us a call and we can set up a free home consultation to discuss any questions you may have. We also provide free lot evaluations. If you already own land, or are in the process of selecting a lot for your new home, please contact us to arrange a free lot evaluation of your property to determine the best possible building site and design for your new home."
                except Exception as e:
                    SpecDescription= ''

                try:
                    SpecElevationImage = re.findall('url(\(.*?)\)', response.text)
                    SpecElevationImage = '|'.join(SpecElevationImage).replace(')', '').replace('(', '')
                    SpecElevationImage = SpecElevationImage.strip('|')
                except Exception as e:
                    SpecElevationImage = ""

                try:
                    SpecWebsite = response.url
                except Exception as e:
                    print(e)

                try:
                    item = BdxCrawlingItem_Spec()
                    item['SpecNumber'] = SpecNumber
                    item['PlanNumber'] = unique_number
                    item['SpecStreet1'] = SpecStreet1
                    item['SpecCity'] = SpecCity
                    item['SpecState'] = SpecState
                    item['SpecZIP'] = SpecZIP
                    item['SpecCountry'] = SpecCountry
                    item['SpecPrice'] = SpecPrice
                    item['SpecSqft'] = SpecSqft
                    item['SpecBaths'] = SpecBaths
                    item['SpecHalfBaths'] = SpecHalfBaths
                    item['SpecBedrooms'] = SpecBedrooms
                    item['MasterBedLocation'] = MasterBedLocation
                    item['SpecGarage'] = SpecGarage
                    item['SpecDescription'] = SpecDescription
                    item['SpecElevationImage'] = SpecElevationImage
                    item['SpecWebsite'] = SpecWebsite
                    yield item
                except:
                    print("commm")
        except Exception as e:
            print("process_home",e,response.url)
             # --------------------------------------------------------------------- #
if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl braklowhomes".split())


