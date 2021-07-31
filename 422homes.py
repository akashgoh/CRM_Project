# -*- coding: utf-8 -*-
import scrapy
import re
import os
import hashlib
import scrapy
from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse



# New Site ====> 422homes
class fourhomes(scrapy.Spider):
    name = '422homessecnd'
    # allowed_domains = ['422homes.com']
    # start_urls = ['https://422homes.com/']
    builderNumber = '62157'
    def start_requests(self):
        url =  ['https://422homes.com/indiana-inventory/','https://422homes.com/butler-inventory/','https://422homes.com/delmont-inventory/','https://422homes.com/previously-owned-homes/']
        for i in url:
            yield scrapy.Request(url= i,callback=self.community,dont_filter=True)

    def community(self,response):
        try:
            suvdivname = response.xpath('//h1/text()').extract_first(default='')
        except Exception as e:
            suvdivname =''
            print(e)
        try:
            street1 = response.xpath('//div/div/div[2]/div/div/div/div/ul/li[1]/span[2]/text()[1]').extract_first(default='')
        except Exception as e:
            street1 = ''
            print(e)

        maintr= response.xpath('//div/div/div[2]/div/div/div/div/ul/li[1]/span[2]/text()[2]').extract_first(default='')
        try:
            city = maintr.split(',')[0]
        except Exception as e:
            print(e)
            city = ''
        try:
            state =maintr.split(',')[1].split(" ")[1]
        except Exception as e:
            state = ''
            print(e)
        try:
            zip_Code = maintr.split(',')[-1].split(' ')[-1]
        except Exception as e:
            zip_Code  = ''
            print(e)
        try:
            phone = response.xpath('//*[contains(text(),"Phone")]/../text()').extract_first(default='')
            if phone =='':
                phone = response.xpath('//div/div/div[2]/div/div/div/div/ul/li[3]/span[2]/text()').extract_first(default='')
            AreaCode = phone.split('-')[0].strip()
            if ': ' in AreaCode:
                AreaCode=AreaCode.replace(': ','')
            Prefix = phone.split('-')[1].strip()

            Suffix = phone.split('-')[-1].strip()

        except Exception as e:
            phone = ''
            AreaCode =''
            Prefix= ''
            Suffix =''
            print(e)

        subdiv = int(hashlib.md5(bytes(str(suvdivname)+str(response.url), "utf8")).hexdigest(), 16) % (10 ** 30)
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = subdiv
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = suvdivname
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = street1
        item['City'] = city
        item['State'] = state
        item['ZIP'] = zip_Code
        item['AreaCode'] = AreaCode
        item['Prefix'] = Prefix
        item['Suffix'] = Suffix
        item['Extension'] = ""
        item['Email'] = "info@422homes.com"
        item['SubDescription'] = '422 HOMES is one of the largest manufactured / modular home retailer in the Northeast United States. Our three full service custom home sales centers are located in Indiana, Butler, and Delmont, PA. We are a full service company equipped for: sales, site preparation, foundation construction, delivery, installation, service, 24 hour emergency service, financing and insurance. 422 HOMES has been meeting the needs of families in Western Pennsylvania and adjoining states since 1974. We are proud of the outstanding achievement awards that we received over the past 40 years from several home manufacturers and communities represented by our company.'
        item['SubImage'] = 'https://422homes.com/wp-content/uploads/2020/08/cropped-422_homes_new_logo-1-192x192.png|https://422homes.com/wp-content/uploads/2020/07/energy-and-persistence-conquer-all-things.jpg|https://422homes.com//wp-content//uploads//2020//07//energy-and-persistence-conquer-all-things.jpg'
        item['SubWebsite'] = response.url
        item['AmenityType'] = ''
        yield item


        main_plan_url1 = response.url
        # yield scrapy.Request(url=main_plan_url1, callback=self.sub_plan_details,
        #                          meta={'sbdn': subdiv})
        response88 = requests.request("GET", main_plan_url1)
        res33 = HtmlResponse(url=main_plan_url1, body=response88.content, encoding='utf-8')
        divs = res33.xpath('//*[@class="swiper-wrapper"]//ancestor::div[@class="elementor-widget-wrap"]/section')
        for i in divs:
            try:
                plan_name = i.xpath('.//h3/text()').extract_first(default='')
            except Exception as e:
                plan_name = ''
                print(e)

            unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

            try:
                baseprice = '0'
            except Exception as e:
                baseprice = '0'
                print(e)

            try:
                BaseSqft = '0'
            except Exception as e:
                BaseSqft = 0
                print(e)
            try:
                Baths = i.xpath('.//div/p/text()').getall()[-1]
                print(Baths)
                # Baths1 =i.xpath('.//div/p/text()').getall()
                if '|' in Baths:
                    bad = Baths.split('BD')[0]
                    Baths = Baths.split(' | ')[-1].split(' ')[0]

                    if Baths != '':
                        tmp = re.findall(r"(\d+)", Baths)
                        Baths = tmp[0]
                        if len(tmp) > 1:
                            HalfBaths = 1
                        else:
                            HalfBaths = 0
                    else:
                        Baths = 0
                        HalfBaths = 0
            except Exception as e:
                Baths = i.xpath(
                    '//*[@class="swiper-wrapper"]//ancestor::div[@class="elementor-widget-wrap"]/section//h4/text()').extract_first()
                if Baths:
                    if '|' in Baths:
                        Baths = Baths.split(' | ')[-1].split(' ')[0]
                        bad = Baths.split(' | ')[0].split(' ')[0]
                        if Baths != '':
                            tmp = re.findall(r"(\d+)", Baths)
                            Baths = tmp[0]
                            if len(tmp) > 1:
                                HalfBaths = 1
                            else:
                                HalfBaths = 0
                        else:
                            Baths = 0
                            HalfBaths = 0
                else:
                    Baths = 0
                    bad = 0
                    HalfBaths = 0
                    print(e)
            try:
                ElevationImage = '|'.join(i.xpath('./..//div[@class="swiper-wrapper"]/div/a/@href').extract())
                if ElevationImage == '':
                    ElevationImage = 'https://422homes.com/wp-content/uploads/2020/08/Aspen_Indiana-5-scaled.jpg|https://422homes.com/wp-content/uploads/2020/08/Aspen_Indiana-10-scaled.jpg|https://422homes.com/wp-content/uploads/2020/08/Aspen_Indiana-1-scaled.jpg'
            except Exception as e:
                ElevationImage = ''
                print(e)

            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanName'] = plan_name
            item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['SubdivisionNumber'] = subdiv
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = baseprice
            item['BaseSqft'] = BaseSqft
            item['Baths'] = Baths
            item['HalfBaths'] = HalfBaths
            item['Bedrooms'] = bad
            item['Garage'] = 0
            item[
                'Description'] = 'Our purpose is to help as many people into a new home as possible. Our entire staff has been carefully selected and trained to be the absolute best our industry has to offer. We are committed to providing you with service of excellence and will do everything in our power to turn your dream of home ownership into a reality. Above all, we understand that serving our customers is indeed…A TRUE PRIVILEGE.  NMLS #:  201098'
            item['ElevationImage'] = ElevationImage
            item['PlanWebsite'] = response.url
            item['unique_number'] = unique_number
            yield item


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl 422homessecnd".split())