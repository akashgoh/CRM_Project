# -*- coding: utf-8 -*-
import hashlib
import re, time
import requests
from scrapy.http import HtmlResponse
import scrapy
from scrapy.utils.response import open_in_browser
from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec

class WinhomesflSpider(scrapy.Spider):
    name = 'winhomesfl'
    allowed_domains = []
    start_urls = ['http://winhomesfl.com/']

    builderNumber = "897831289731096020172188757990"

    def parse(self, response):

        # IF you do not have Communities and you are creating the one
        # ------------------- If No communities found ------------------- #
        f = open("html/%s.html" % self.builderNumber, "wb")
        f.write(response.body)
        f.close()

        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = ''
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = "4640 West Price Blvd."
        item['City'] = "North Port"
        item['State'] = "FL"
        item['ZIP'] = "34286"
        item['AreaCode'] = "941"
        item['Prefix'] = "423"
        item['Suffix'] = "2055"
        item['Extension'] = ""
        item['Email'] = "windemermainofc@comcast.net"
        item['SubDescription'] = "New Homes and Residential Builder in North Port, Florida (Sarasota County) Also serving Nokomis, Osprey, Venice, Englewood, and Port Charlotte"
        item['SubImage'] = "http://winhomesfl.com/images2/AshwoodIFront2016.jpg|http://winhomesfl.com/images2/newfrontpool.JPG|http://winhomesfl.com/images2/RubyFront2016.jpg"
        item['SubWebsite'] = response.url
        item['AmenityType'] = ''
        yield item

        proxy = {
            'https': 'https://lum-customer-xbyte-zone-zone_us-country-us:0gi0pioy3oey@zproxy.lum-superproxy.io:22225',
            'http': 'http://lum-customer-xbyte-zone-zone_us-country-us:0gi0pioy3oey@zproxy.lum-superproxy.io:22225',
            }
        plan_page_links = ['http://www.winhomesfl.com/classicmodels', 'http://www.winhomesfl.com/frontiermodels']
        # plan_page_links = [ 'http://www.winhomesfl.com/frontiermodels']
        for link in plan_page_links:
            print(f"# --------------------{link}")
            head = {'Host': 'www.winhomesfl.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-GB,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate'}
            # time.sleep(2)
            yield scrapy.FormRequest(url=link,headers=head,dont_filter=True, callback=self.first_level)
    
    
    
    def first_level(self,response):
        plan_links = response.xpath('//a[@class="sqs-block-button-element--small sqs-block-button-element"]/@href').extract()
        for plan_link in plan_links:
            yield scrapy.FormRequest(url=f'http://winhomesfl.com{plan_link}', dont_filter=True, callback=self.parse_next, meta={'plan_link':plan_link})
            # yield scrapy.FormRequest(url=f'http://winhomesfl.com/emerald-i-b', dont_filter=True, callback=self.parse_next, meta={'plan_link':plan_link})

    def parse_next(self,response):
        try:
            Type = 'SingleFamily'
        except Exception as e:
            print(e)

        try:
            PlanNumber = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
        except Exception as e:
            print(e)

        try:
            PlanName = response.xpath('//h1/text()').extract_first(default='').strip()
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
            BasePrice = 0
        except Exception as e:
            print(e)

        try:
            Description = '\n'.join(response.xpath('//*[@class="sqs-block-content"]/p//text()').extract())
        except Exception as e:
            print(e)

        try:
            ElevationImage = '|'.join(re.findall('<noscript><img src="(.*?)"/></noscript>', response.text))
            ElevationImage = '|'.join(re.findall('<noscript><img src="(.*?)" /></noscript', response.text))
            if ElevationImage =='' or ElevationImage == None:
                ElevationImage = response.xpath('//*[@class="thumb-image loaded"]/@data-src').extract_first()
            if ElevationImage =='' or ElevationImage == None:
                ElevationImage = '|'.join(response.xpath('//img[@class="thumb-image loaded"]/@data-src').extract())
        except Exception as e:
            print(e)

        try:
            PlanWebsite = str(response.url)
        except Exception as e:
            print(e)

        try:
            data = '|'.join(response.xpath('//*[@class="sqs-block-content"]/h2//text()').extract())
            try:BaseSqft = re.findall('(\d+)\sSquare',data)[0].strip()
            except:BaseSqft = 0
            try:Bedrooms = re.findall('(\d+)\sBedrooms',data)[0].strip()
            except:Bedrooms=0
            try:
                Garage = re.findall('(\d+)\sCar',data)[0].strip()
            except:
                Garage = 0 if 'Garage' in data else 0
            try:
                temp = re.findall(',\s(.*?)\sBath',data)[0].strip()
                Baths = temp[0]
                if len(temp)>1:
                    HalfBaths = 1
                else:HalfBaths=0
            except:
                Baths = 1 if 'Bath' in data else 0
                HalfBaths = 1 if 'Half Bath' in data else 0
        except Exception as e:
            print(e)

            # ----------------------- Don't change anything here --------------
        try:
            unique = str(PlanName) + str(response.url) +response.meta['plan_link']+ str(self.builderNumber)  # < -------- Changes here
            unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
            item = BdxCrawlingItem_Plan()
            item['Type'] = Type
            item['PlanNumber'] = PlanNumber
            item['unique_number'] = unique_number  # < -------- Changes here
            item['SubdivisionNumber'] = self.builderNumber

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
        except Exception as e:
            print(e)    
            


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl winhomesfl".split())