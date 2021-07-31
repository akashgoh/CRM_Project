# builder no : 63701
# main site : bussellbuildinginc.com

import scrapy
import re
import os
import hashlib
import scrapy
from pygments.lexer import default
from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse

class BussellBuildingInc(scrapy.Spider):
    name = 'BussellBuildingInc'
    builderNumber = '63701'

    def start_requests(self):
        url = 'https://bussellbuildinginc.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self, response):
            item = BdxCrawlingItem_subdivision()
            item['sub_Status'] = "Active"
            item['SubdivisionNumber'] = self.builderNumber
            item['BuilderNumber'] = self.builderNumber
            item['SubdivisionName'] = "No Sub Division"
            item['BuildOnYourLot'] = 0
            item['OutOfCommunity'] = 1
            item['Street1'] = '1979 S. Lullwood Ave.'
            item['City'] = 'Springfield'
            item['State'] = 'MO'
            item['ZIP'] = '65802'
            item['AreaCode'] = '417'
            item['Prefix'] = "879"
            item['Suffix'] = "7247"
            item['Extension'] = ""
            item['Email'] = "sales@bussellbuilding.com"
            item['SubDescription'] = "Bussell Building built my home approx 8 years ago. I had a few ideas when we met and they were incredible to work with! Very responsive, professional and eager to please"
            item['SubImage'] = 'https://s3.amazonaws.com/eap02files.easyagentpro.com/wp-content/uploads/sites/724/2020/04/15133407/Capture-4.jpg|https://cdn.photos.sparkplatform.com/somo/20200929213517991175000000-o.jpg'
            item['SubWebsite'] = response.url
            item['AmenityType'] = ''
            yield item


            mainurl = ['https://bussellbuildinginc.com/3-bedroom-floor-plans/',
                  'https://bussellbuildinginc.com/4-bedroom-floor-plans/',
                   'https://bussellbuildinginc.com/basement-floor-plans/',
                   'https://bussellbuildinginc.com/2-story-floor-plans/',
                   'https://bussellbuildinginc.com/split-floor-plan/'
                   ]
            for i in mainurl:
                response88 = requests.request("GET", i)
                res33 = HtmlResponse(url=i, body=response88.content, encoding='utf-8')
                url = res33.xpath('//*[@id="main"]/div//div/h2/a/@href').extract()
                final_url = ['https://bussellbuildinginc.com/emerson/', 'https://bussellbuildinginc.com/everett/',
                          'https://bussellbuildinginc.com/kylie/', 'https://bussellbuildinginc.com/laura/','https://bussellbuildinginc.com/ashley/','https://bussellbuildinginc.com/riley-basement/','https://bussellbuildinginc.com/brooks/','https://bussellbuildinginc.com/finley/','https://bussellbuildinginc.com/jozlyn/','https://bussellbuildinginc.com/porter/','https://bussellbuildinginc.com/olivia/','https://bussellbuildinginc.com/paige/']
                for i in url:
                    final_url.append(i)




                for i in final_url:
                    yield scrapy.Request(url=i, callback=self.plan_details,meta={"SubdivisionNumber": item['SubdivisionNumber']})

    def plan_details(self, response):
        SubdivisionNumber = response.meta['SubdivisionNumber']
        try:
            plan_name = response.xpath('//h1/text()').extract_first(default='').strip()
        except Exception as e:
            print(e)
            plan_name =''

        try:
            BasePrice = 0
        except Exception as e:
            BasePrice =0
            print(e)
        try:
            BaseSqft = response.xpath('//*[contains(text()," Sq")]//text()|//*[contains(text(),"Approx.")]//text()').extract_first(default='').replace('SqFt','').replace(',','').replace('Approx.','').replace('Approx.','').strip()
            if '-' in BaseSqft:
                BaseSqft = BaseSqft.split('-')[-1]
        except Exception as e:
            BaseSqft = 0
            print(e)
        try:
            Baths = response.xpath('//*[@id="singlePropertyPage"]//div[1]/div[3]/text()').extract_first(default='').replace('BA','').strip()
            tmp = re.findall(r"(\d+)", Baths)
            Baths = int(tmp[0])
            if len(tmp) > 1:
                HalfBaths = 1
            else:
                HalfBaths = 0

        except Exception as e:
            print(e)
            Baths = 0
            HalfBaths = 0

        try:
            Bedrooms= response.xpath('//*[@id="singlePropertyPage"]//div[1]/div[2]/text()').extract_first(default='').replace('BD','').strip()
            if response.url == 'https://bussellbuildinginc.com/dean/':
                Bedrooms = '4'
            if Bedrooms=='':
                Bedrooms = response.xpath('//*[@id="singlePropertyPage"]/section[2]//ul/li[1]/text()').extract_first(default='')
                Bedrooms = Bedrooms.split('Bedrooms /')[0]
            Bedrooms = ''.join(re.findall(r"(\d+)", Bedrooms))


        except Exception as e:
            Bedrooms= 0
            print(e)
        try:
            Garage= response.xpath('//*[contains(text(),"Car Garage")]/text()|//*[contains(text(),"Car Angled Garage")]//text()').extract_first(default='')
            if 'or' in Garage:
                Garage = Garage.split('or')[-1]
            Garage = float(''.join(re.findall(r"(\d+)", Garage)))
        except Exception as e:
            Garage = 0
            print(e)

        try:
            Description= 'Floor plan shown is intended to show a general layout of the home and could contain upgraded features. Please confirm standard features.'
        except Exception as e:
            Description=''
            print(e)
        try:
            ElevationImage = '|'.join(response.xpath('//div/div/img/@src|//*[@id="singlePropertyImageGallery"]/div/div/div[2]/div/div/a/div/img/@src').extract())
            if ElevationImage =='':
                ElevationImage = '|'.join(response.xpath('//div[@class="wp-block-image"]/figure/img/@src').extract())
            if ElevationImage =='':
                ElevationImage = '|'.join(response.xpath('//div//img/@src').extract())
        except Exception as e:
            ElevationImage= ''
            print(e)

        unique = str(int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
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
        item['Bedrooms'] = Bedrooms
        item['Garage'] = Garage
        item['Description'] = Description
        item['ElevationImage'] = ElevationImage
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

        home_url = [
                "https://bussellbuildinginc.com/homes-for-sale-details/6007-SOUTH-CRESCENT-ROAD-LOT-2-BATTLEFIELD-MO-65619/60173171/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/5916-SOUTH-CRESCENT-ROAD-LOT-47-BATTLEFIELD-MO-65619/60173176/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/6036-SOUTH-CRESCENT-ROAD-LOT-51-BATTLEFIELD-MO-65619/60173228/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/1964-SOUTH-SHAYLA-AVENUE-LOT-33-SPRINGFIELD-MO-65802/60176750/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/4245-WEST-ORCHARD-LANE-LOT-9-BATTLEFIELD-MO-65619/60178624/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/4249-WEST-ORCHARD-LANE-LOT-8-BATTLEFIELD-MO-65619/60178620/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/5917-SOUTH-CRESCENT-ROAD-LOT-5-BATTLEFIELD-MO-65619/60178780/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/5976-SOUTH-CRESCENT-ROAD-LOT-49-BATTLEFIELD-MO-65619/60179477/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/2816-EAST-AUBURN-HILLS-STREET-LOT-2-REPUBLIC-MO-65738/60181494/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/2804-EAST-AUBURN-HILLS-STREET-LOT-3-REPUBLIC-MO-65738/60181495/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/2750-EAST-AUBURN-HILLS-STREET-LOT-6-REPUBLIC-MO-65738/60182236/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/2726-EAST-AUBURN-HILLS-STREET-LOT-8-REPUBLIC-MO-65738/60182315/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/6126-SOUTH-CRESCENT-ROAD-LOT-54-BATTLEFIELD-MO-65619/60182517/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/6096-SOUTH-CRESCENT-ROAD-LOT-53-BATTLEFIELD-MO-65619/60182506/386/",
                "https://bussellbuildinginc.com/homes-for-sale-details/6031-SOUTH-BROOKSIDE-LANE-LOT-90-BATTLEFIELD-MO-65619/60187266/386/"]
        for i in home_url:
            yield scrapy.Request(url=i,callback=self.home_details,meta={'PlanNumber':item['PlanNumber'],'SubdivisionNumber':SubdivisionNumber})

    def home_details(self,response):

        SubdivisionNumber = response.meta['SubdivisionNumber']

        # --------------- fack plan =---------------------------------------------------------
        plan_name = 'Plan Unknown'
        unique1 = str(int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique1, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = self.builderNumber
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '0'
        item['Baths'] = 1
        item['HalfBaths'] = 1
        item['Bedrooms'] = 1
        item['Garage'] = 0.0
        item['Description'] = ''
        item['ElevationImage'] = 'https://www.americanhomestore.net/images/slidesized/caracelKitchen.jpg|https://www.americanhomestore.net/images/Cedar-Canyon-2074-interior-1.jpg'
        item['PlanWebsite'] = 'https://bussellbuildinginc.com/'
        item['unique_number'] = unique_number
        yield item
        # ------------------------------------------

        # ------------------------------------------1 ----------- home --
        if response.url == 'https://bussellbuildinginc.com/homes-for-sale-details/6007-SOUTH-CRESCENT-ROAD-LOT-2-BATTLEFIELD-MO-65619/60173171/386/':
            SpecStreet1 = '6007 South Crescent Road #Lot 2'
            SpecCity = 'Battlefield'
            unique = str(SpecStreet1) + str(SpecCity)
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = unique_number
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = 'MO'
            item['SpecZIP'] = "65619"
            item['SpecCountry'] = 'USA'
            item['SpecPrice'] = '325000'
            item['SpecSqft'] = '2064'
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 0
            item['SpecBedrooms'] = 4
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item[
                'SpecDescription'] = "This is the Bussell Built Dean floor plan! This home can feature a slab foundation, hardwood floors, granite countertops, custom built white kitchen cabinets with island"
            img = '|'.join(response.xpath('//img[@class="media-object ihf-center"]/@data-ihf-main-source').extract())
            item['SpecElevationImage'] = img
            item[
                'SpecWebsite'] = 'https://bussellbuildinginc.com/homes-for-sale-details/6007-SOUTH-CRESCENT-ROAD-LOT-2-BATTLEFIELD-MO-65619/60173171/386/'
            item['unique_number'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            yield item

        if response.url == 'https://bussellbuildinginc.com/homes-for-sale-details/5916-SOUTH-CRESCENT-ROAD-LOT-47-BATTLEFIELD-MO-65619/60173176/386/':
            SpecStreet1 = '5916 South Crescent Road #Lot 47'
            SpecCity = 'Battlefield'
            unique = str(SpecStreet1) + str(SpecCity)
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = unique_number
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = 'MO'
            item['SpecZIP'] = "65619"
            item['SpecCountry'] = 'USA'
            item['SpecPrice'] = '365000'
            item['SpecSqft'] = '2502'
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 0
            item['SpecBedrooms'] = 3
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3
            item[
                'SpecDescription'] = "This is the Bussell Built Indigo floor plan! This home can feature slab foundation, hardwood floors, granite countertops, custom built white kitchen cabinets with island, energy star/stainless steel appliances, tile shower, stone w cedar mantle gas fireplace"
            img = '|'.join(response.xpath('//img[@class="media-object ihf-center"]/@data-ihf-main-source').extract())
            # item['SpecElevationImage'] ='https://s3.amazonaws.com/eap02files.easyagentpro.com/wp-content/uploads/sites/724/2020/04/15133407/Capture-4.jpg|https://cdn.photos.sparkplatform.com/somo/202009292135179911750'
            item['SpecElevationImage'] = img
            item[
                'SpecWebsite'] = 'https://bussellbuildinginc.com/homes-for-sale-details/5916-SOUTH-CRESCENT-ROAD-LOT-47-BATTLEFIELD-MO-65619/60173176/386/'
            item['unique_number'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            yield item

        if response.url == 'https://bussellbuildinginc.com/homes-for-sale-details/4245-WEST-ORCHARD-LANE-LOT-9-BATTLEFIELD-MO-65619/60178624/386/':
            SpecStreet1 = '4245 West Orchard Lane #Lot 9'
            SpecCity = 'Battlefield'
            unique = str(SpecStreet1) + str(SpecCity)
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = unique_number
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = 'MO'
            item['SpecZIP'] = "65619"
            item['SpecCountry'] = 'USA'
            item['SpecPrice'] = '295000'
            item['SpecSqft'] = '1845'
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 0
            item['SpecBedrooms'] = 4
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item[
                'SpecDescription'] = "This is the Bussell Built Shelby floor plan with an angled garage! This home can feature a slab foundation, hardwood floors, tile shower, granite countertops, custom built white kitchen cabinets with island"
            item[
                'SpecElevationImage'] = 'https://s3.amazonaws.com/eap02files.easyagentpro.com/wp-content/uploads/sites/724/2020/04/15133407/Capture-4.jpg|https://cdn.photos.sparkplatform.com/somo/202009292135179911750'
            item[
                'SpecWebsite'] = 'https://bussellbuildinginc.com/homes-for-sale-details/4245-WEST-ORCHARD-LANE-LOT-9-BATTLEFIELD-MO-65619/60178624/386/'
            item['unique_number'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            yield item

        if response.url == 'https://bussellbuildinginc.com/homes-for-sale-details/4249-WEST-ORCHARD-LANE-LOT-8-BATTLEFIELD-MO-65619/60178620/386/':
            SpecStreet1 = '4249 West Orchard Lane #Lot 8'
            SpecCity = 'Battlefield'
            unique = str(SpecStreet1) + str(SpecCity)
            SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Spec()
            item['SpecNumber'] = SpecNumber
            item['PlanNumber'] = unique_number
            item['SpecStreet1'] = SpecStreet1
            item['SpecCity'] = SpecCity
            item['SpecState'] = 'MO'
            item['SpecZIP'] = "65619"
            item['SpecCountry'] = 'USA'
            item['SpecPrice'] = '325000'
            item['SpecSqft'] = '2158'
            item['SpecBaths'] = 2
            item['SpecHalfBaths'] = 0
            item['SpecBedrooms'] = 4
            item['MasterBedLocation'] = 'Down'
            item['SpecGarage'] = 3.0
            item[
                'SpecDescription'] = "This is the Bussell Built Ethan floor plan! This home can feature a slab foundation, hardwood floors, granite countertops, white custom built kitchen cabinets with island, energy star/stainless steel appliances, ship lap & cedar fireplace, tile shower"
            img = '|'.join(response.xpath('//img[@class="media-object ihf-center"]/@data-ihf-main-source').extract())
            # item['SpecElevationImage'] ='https://s3.amazonaws.com/eap02files.easyagentpro.com/wp-content/uploads/sites/724/2020/04/15133407/Capture-4.jpg|https://cdn.photos.sparkplatform.com/somo/202009292135179911750'
            item['SpecElevationImage'] = img
            item[
                'SpecWebsite'] = 'https://bussellbuildinginc.com/homes-for-sale-details/4249-WEST-ORCHARD-LANE-LOT-8-BATTLEFIELD-MO-65619/60178620/386/'
            item['unique_number'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            yield item


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl BussellBuildingInc".split())
