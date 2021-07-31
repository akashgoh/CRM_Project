# builder no:

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
    name = 'BaldwinPhillipsConstruction'
    builderNumber = '62864'

    def start_requests(self):
        url = 'https://baldwinlogandtimbercrafters.com/' #<<----- Community link
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
        item['Street1'] = '7213 Hwy. 74 East'
        item['City'] = 'Sylva'
        item['State'] = 'NC'
        item['ZIP'] = '28779'
        item['AreaCode'] = '828'
        item['Prefix'] = "734"
        item['Suffix'] = "0783"
        item['Extension'] = ""
        item['Email'] = "baldwinlogging@yahoo.com"
        item['SubDescription'] = ''
        item['SubImage'] = 'https://baldwinlogandtimbercrafters.com/wp-content/uploads/2017/03/IMG_3541_crop.jpg|https://baldwinlogandtimbercrafters.com/wp-content/uploads/2017/03/IMG_4200_crop.jpg'
        item['SubWebsite'] = 'https://baldwinlogandtimbercrafters.com/'
        item['AmenityType'] = ''
        yield item

        main_plan_url = 'https://baldwinlogandtimbercrafters.com/home-plans/'
        # response88 = requests.request("GET", main_plan_url)
        # res33 = HtmlResponse(url=main_plan_url, body=response88.content, encoding='utf-8')
        # sub_plan_url = res33.xpath('').extract()
        # for i in sub_plan_url:
        #     url = i
        yield scrapy.Request(url=main_plan_url, callback=self.plan_details,
                                 meta={"SubdivisionNumber": item['SubdivisionNumber']})
    def plan_details(self,response):
        SubdivisionNumber = response.meta['SubdivisionNumber']
        divas1 = response.xpath('//div[@class="entry-content"]//h2')
        divas = response.xpath('//*[@class="su-row"]')
        for j,i in zip(divas1,divas):
            try:
                plan_name = j.xpath('.//text()').extract_first(default='')
                print(plan_name)
            except Exception as e:
                plan_name= ''
                print(e)

            try:
                BasePrise= '0'
            except Exception as e:
                BasePrise = '0'
                print(e)

            main_divs = "".join(i.xpath(".//text()").getall()).strip()
            try:
                BaseSqft = ''.join(re.findall('Total:(.*?)SQ FT',main_divs)).replace(',','').replace('SQ FT','')
            except Exception as e:
                BaseSqft= 0
                print(e)
            try:
                Baths = ''.join(re.findall('Baths:(.*?)\n',main_divs)).strip()

                if '1/2' in Baths:
                    Baths = str(int(Baths.split('1/2')[0]))
                    HalfBaths = 1
                elif Baths == '' or Baths== []:
                    Baths = 0
                    HalfBaths=0
                else:
                    Baths=Baths.split()
                    if len(Baths) == 1:
                        Baths = Baths[0].strip()
                        HalfBaths = 0
                    elif len(Baths) > 1:
                        Baths = Baths[0].strip()
                        HalfBaths = 1
            except Exception as e:
                Baths = 0
                HalfBaths = 0
                print(e)

            if Baths:
                Baths = str(Baths)
            else: Baths= Baths

            try:
                Badroom = ''.join(re.findall('Bedroom:(.*?)\n',main_divs))
                Badroom = ''.join(re.findall('(\d+)', Badroom)).strip()
                if Badroom == '' or Badroom == []:
                    Badroom = 0
                else:Badroom = Badroom
            except Exception as e:
                Badroom = 0
                print(e)
            try:
                Garage =''.join(re.findall('Garage Bays:(.*?)\n',main_divs)).strip()
                if Garage == '':
                    Garage = 0
            except Exception as e:
                Garage= 0
                print(e)
            try:
                # imges =i.xpath('.//*[@class="su-column su-column-size-1-4"][1]/div/img/@src').extract_first(default='')
                imges = i.xpath(".//@src").getall()
                imges = imges[1]
                if imges == '':
                    imges= 'https://baldwinlogandtimbercrafters.com/wp-content/uploads/2017/03/gfx_plan_driver_rendering_lrg.gif'
            except Exception as e:
                imges = 'https://baldwinlogandtimbercrafters.com/wp-content/uploads/2017/03/gfx_plan_driver_rendering_lrg.gif'
                print(e)




            unique = str(int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
            # unique = str(PlanNumber)+str(BaseSqft)+str(Badroom)+str(Baths)

            # unique = str(PlanNumber)
            # unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] =  int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = BasePrise
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = Badroom
            item['Garage'] = Garage
            item['Description'] = 'Baldwin & Phillips Construction brings together 40+ years of construction experience. Our specialties are high end log, timber frame & craftsman style homes. Located in Sylva, North Carolina.'
            item['ElevationImage'] = imges
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl BaldwinPhillipsConstruction".split())
