# -*- coding: utf-8 -*-
import scrapy
import re
import os
import hashlib
import scrapy
from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse



# New Site ====> https://affinityhomesllc.com/
class fourhomes(scrapy.Spider):
    name = 'affinityhomesllc'
    # allowed_domains = ['422homes.com']
    # start_urls = ['https://affinityhomesllc.com/']
    builderNumber = '62134'

    def start_requests(self):
        url = 'https://affinityhomesllc.com/'
        yield scrapy.Request(url=url,callback=self.community)

    def community(self,response):
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = '1111 Main St. STE 109'
        item['City'] = 'Vancouver'
        item['State'] = 'WA'
        item['ZIP'] = '98660'
        item['AreaCode'] = '360'
        item['Prefix'] = "989"
        item['Suffix'] = "6316"
        item['Extension'] = ""
        item['Email'] = "john@affinityhomesllc.com"
        item['SubDescription'] = "Our philosophy is to build homes tailored to fit the way our clients live. It’s the groundwork for creating the personalized designs of our custom homes.READY TO BUILD YOUR LUXURY HOME?Whether you come in with a custom floor plan or need it drawn from the ground up, our goal is to include everything you want in your custom luxury home design."
        item['SubImage'] = 'https://affinityhomesllc.com/wp-content/uploads/POH_Master-Suite-.png|https://affinityhomesllc.com/wp-content/uploads/4425-NW-Paddock-LN-199.jpg'
        item['SubWebsite'] = 'https://affinityhomesllc.com/'
        item['AmenityType'] = ''
        yield item

        main_plan_url = 'https://affinityhomesllc.com/projects/'
        response88 = requests.request("GET", main_plan_url)
        res1 = HtmlResponse(url=main_plan_url, body=response88.content, encoding='utf-8')

        sub_plan_link = res1.xpath('//div[2]/div/div/section[2]/div/div/div//div/div//a/@href|//div[2]/div/div/section[3]/div/div/div//div/div//a/@href|//div[2]/div/div/section[4]/div/div/div//div/div//a/@href').extract()
        for i in sub_plan_link:
            sub_plan_link = i
            yield scrapy.Request(url=sub_plan_link,callback=self.sub_pan_details,meta={"SubdivisionNumber":item['SubdivisionNumber']})

    def sub_pan_details(self,response):
        SubdivisionNumber= response.meta['SubdivisionNumber']
        try:
            plan_name = response.xpath('//h1/text()').extract_first(default='')
        except Exception as e:
            plan_name = ''
            print(e)
        try:
            baseprice ='0'
        except Exception as e:
            baseprice = '0'
            print(e)
        try:
            BaseSqft =response.xpath('//*[contains(text(),"Square Feet:")]/text()').extract_first(default='').replace('Square Feet:',"").replace(',','').strip()
            BaseSqft = int(BaseSqft)
        except Exception as e:
            BaseSqft = 0
            print(e)
        try:
            Baths = response.xpath('//*[contains(text(),"Bathrooms:")]/text()').extract_first(default='').strip()
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
            Badroom =response.xpath('//*[contains(text(),"Bedrooms:")]/text()').extract_first(default=0).replace('Bedrooms:','')

            if 'or' in Badroom:
                Badroom = Badroom.split(' or ')[-1]

            Badroom = int(''.join((re.findall(r"(\d+)", Badroom))))
        except Exception as e:
            Badroom = 0
            print(e)
        try:
            Garage = response.xpath('//*[contains(text(),"Garage:")]/text()').extract_first(default=0).replace('-Car','').strip()
            Garage = int(''.join(re.findall(r"(\d+)", Garage)))
        except Exception as e:
            Garage =0
            print(e)

        try:
            description = str('This stunning 2-story Pacific Northwest Modern home takes you back to a time of low-profile mid-century interior design and modern technology. It captures every detail of modern home architecture, from asymmetrical rooflines to geometric patterns in its interior finishes.This home’s exterior is finished with mixed cladding.').strip()
        except Exception as e:
            description = ''
            print(e)
        try:
            ElevationImage= '|'.join(response.xpath('//*[@class="gallery-item"]//img/@src|//div[@class="elementor-gallery__container e-gallery-container e-gallery-grid e-gallery--ltr e-gallery--lazyload"]//a/@href|//div[@class="elementor-widget-container"]/div[@class="elementor-image"]/img/@src').extract())
        except Exception as e:
            ElevationImage =''
            print(e)

        unique = str(int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
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


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl affinityhomesllc".split())



