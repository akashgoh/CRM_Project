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
    name = 'Baird_Homes_Corporation'
    builderNumber = '62852'

    def start_requests(self):
        url = 'https://bairdhomes.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self,response):
        print(" ------------- Not Found Community -------------- ")
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = '3495 US Highway 441/27'
        item['City'] = 'Fruitland Park'
        item['State'] = 'FL'
        item['ZIP'] = '34731'
        item['AreaCode'] = '352'
        item['Prefix'] = "787"
        item['Suffix'] = "2500"
        item['Extension'] = ""
        item['Email'] = "contact@bairdcorp.com"
        item['SubDescription'] = 'Baird Homes our team of home sales professionals have worked with clients just like you for more than 70 years. The core of our mission statement centers around integrity and it continues today so that we can help home buyers purchase their dream home with the confidence of knowing they have been given the facts Baird Homes believes in customer satisfaction to its core. With the help of a variety of award-winning manufacturers, Baird Homes has continually offered top of the line manufactured housing at an affordable cost to our customers. In addition to our friendly and knowledgeable staff.'
        item['SubImage'] = 'https://bairdhomes.com/wp-content/uploads/2019/08/baird-homes-kitchen-banner.jpg|https://bairdhomes.com/wp-content/uploads/2019/11/Seymour.jpg|https://bairdhomes.com/wp-content/uploads/2019/11/Vincennes.jpg'
        item['SubWebsite'] = 'https://bairdhomes.com/'
        item['AmenityType'] = ''
        yield item

        plan_link = response.xpath('//*[@class="menu-main-menu-container"]/ul/li[3]/ul[@class="sub-menu"]/li/a/@href').extract()[0:4]
        for i in plan_link:
            url = i
            # url = 'https://bairdhomes.com/manufactured-and-modular-homes-madison/'
            yield scrapy.Request(url=url,callback=self.sub_plan_link,meta={'sbd':item['SubdivisionNumber']})

    def sub_plan_link(self,response):
        sbd = response.meta['sbd']
        link = response.xpath('//*[@class="inventory row"]/div//a/@href|//*[@class="button-default btn-secondary"]/@href').extract()
        links = ['https://bairdhomes.com/inventory/commodore-2lm2201_distinction/',"https://bairdhomes.com/inventory/adventure-manufactured-2844-1/"]
        for i2 in link:
            links.append(i2)


        for i in links:
            url = i
            yield scrapy.Request(url=url,callback=self.sub_plan_details,meta={'sbd':sbd })

    def sub_plan_details(self,response):
        # if response.url == 'https://bairdhomes.com/inventory/fleetwood-manufactured-32603g-distinction/' or response.url=='https://bairdhomes.com/inventory/commodore-2lm2201_distinction/'or response.url=='https://bairdhomes.com/inventory/fleetwood-manufactured-28483h-distinction/' or response.url=='https://bairdhomes.com/inventory/fleetwood-manufactured-24442p/' or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-6562n/'  or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-6562n/' or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-6562n/' or response.url =='https://bairdhomes.com/inventory/manufactured-champion-2852213/' or response.url =='https://bairdhomes.com/inventory/fleetwood-manufactured-32663l-madison/' or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-2856-1-madison/' or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-2844-1/' :
        if response.url == 'https://bairdhomes.com/inventory/fleetwood-manufactured-32603g-distinction/' or response.url=='https://bairdhomes.com/inventory/fleetwood-manufactured-28483h-distinction/' or response.url=='https://bairdhomes.com/inventory/fleetwood-manufactured-24442p/' or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-6562n/'  or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-6562n/' or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-6562n/' or response.url =='https://bairdhomes.com/inventory/manufactured-champion-2852213/'  or response.url =='https://bairdhomes.com/inventory/adventure-manufactured-2856-1-madison/':
            pass

        else:
            if 'sold' not in response.text:
                try:
                    plan_name =response.xpath(' //h1/text()').extract_first(default='')
                except Exception as e:
                    plan_name = ''
                    print(e)
                try:
                    BaseSqft = response.xpath('//div[@class="sqft spec"]/div[@class="value"]/text()').extract_first(default='').replace(' SQFT','').replace('SQFT','')
                    BaseSqft = int(BaseSqft)
                except Exception as e:
                    BaseSqft =0
                    print(e)
                try:
                    Baths  = response.xpath('//div[@class="bathroom spec"]/div[@class="value"]/text()').extract_first(default=0)
                    # Bathroom = Baths.split('|')[1].split('Bathrooms:')[1]
                    tmp = re.findall(r"(\d+)", Baths)
                    Baths = tmp[0]
                    if len(tmp) > 1:
                        HalfBaths = 1
                    else:
                        HalfBaths = 0
                except Exception as e:
                    Baths = 0
                    HalfBaths = 0
                    print(e)

                try:
                    Badroom  = response.xpath('//div[@class="bedroom spec"]/div[@class="value"]/text()').extract_first(default=0).replace('Bedrooms','')
                    Badroom  = int(Badroom)
                except Exception as e:
                    Badroom = 0
                    print(e)

                try:
                    description ='|'.join(response.xpath('//*[@id="property-description"]/div/div/p/text()').extract())
                    if description == '':
                        description = 'Fortune Homes, a reputable builder around since 1953 has produced over 1,700,000 factory-built manufactured and modular homes. Check out this compact manufactured house available at your Salem, Indiana location today!'
                except Exception as e:
                    print(e)
                try:
                    img = 'https://bairdhomes.com/wp-content/uploads/2019/11/Vincennes.jpg|https://bairdhomes.com/wp-content/uploads/2019/11/Madison.jpg|https://bairdhomes.com/wp-content/uploads/2019/11/Seymour.jpg|https://bairdhomes.com/wp-content/uploads/2019/11/Salem.jpg|https://bairdhomes.com/wp-content/uploads/2019/10/20191011_110410-1024x768.jpg'
                except Exception as e:
                    img = ''
                    print(e)

                unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
                unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

                item = BdxCrawlingItem_Plan()
                item['Type'] = 'SingleFamily'
                item['PlanName'] = plan_name
                item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
                item['SubdivisionNumber'] = sbd = response.meta['sbd']
                item['PlanNotAvailable'] = 0
                item['PlanTypeName'] = 'Single Family'
                item['BasePrice'] = '0'
                item['BaseSqft'] = BaseSqft
                item['Baths'] = Baths
                item['HalfBaths'] = HalfBaths
                item['Bedrooms'] = Badroom
                item['Garage'] = 0
                item['Description'] = description
                item['ElevationImage'] = img
                item['PlanWebsite'] = response.url
                item['unique_number'] = unique_number
                yield item

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl Baird_Homes_Corporation".split())

