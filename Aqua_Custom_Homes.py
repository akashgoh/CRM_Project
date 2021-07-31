# builder_no  : 62750
# main_site  : aquacustomhomes.com
import scrapy
import re
import os
import hashlib
import scrapy
from pygments.lexer import default
from twisted.spread.test.test_jelly import E

from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
import requests
from scrapy.http import HtmlResponse

# Plan Code = Pending

class aquacustomhomes(scrapy.Spider):
    name = 'aquacustomhomes'
    builderNumber = '62750'

    def start_requests(self):
        url = 'http://www.aquacustomhomes.com/'
        yield scrapy.Request(url=url,callback=self.community_details)

    def community_details(self,response):
        # No Community Founds
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = '421 W Elkcam Circle'
        item['City'] = 'Marco Island'
        item['State'] = 'FL'
        item['ZIP'] = '34145'
        item['AreaCode'] = '239'
        item['Prefix'] = "494"
        item['Suffix'] = "8108"
        item['Extension'] = ""
        item['Email'] = ""
        item['SubDescription'] = "AQUA Custom Homes is a full service construction company with 26 years in the industry. We’ve built more than 250,000 sq ft of commercial buildings and over 120 homes throughout the Midwest and south west Florida."
        img = '|'.join(response.xpath('//ul[@class="slides"]/li/img/@src').extract())
        item['SubImage'] = img
        item['SubWebsite'] = 'http://www.aquacustomhomes.com'
        item['AmenityType'] = ''
        yield item

        plan_url = 'http://www.aquacustomhomes.com/floorplans/'
        yield scrapy.Request(url=plan_url,callback=self.plan_details,meta={"SubdivisionNumber":item['SubdivisionNumber']})

    def plan_details(self,response):
        SubdivisionNumber = response.meta['SubdivisionNumber']

        divs1 = response.xpath('//div[@class="wpb_column vc_column_container vc_col-sm-4 sc_layouts_column_icons_position_left"]//div[@class="wpb_text_column wpb_content_element "]/div[@class="wpb_wrapper"]/p[2]').extract()
        divs2 = response.xpath('//div[@class="wpb_column vc_column_container vc_col-sm-4 sc_layouts_column_icons_position_left"]//div[@class="wpb_text_column wpb_content_element "]/div[@class="wpb_wrapper"]/p[1]//text()').extract()
        for divs1,divs2 in zip(divs1,divs2):
            second_div_data =divs1
            name_div_data =divs2
            if 'Bed' in divs1:
                try:
                    plan_name = name_div_data
                except Exception as e:
                    plan_name = ''
                    print(e)
                try:
                    baseprice = '0'
                except Exception as e:
                    baseprice = '0'
                    print(e)
                try:
                    Badroom =''.join(re.findall('<p style="text-align: center;">(.*?)<br>',second_div_data,re.DOTALL)).replace('Bed','').strip()
                    Badroom = int(Badroom)
                except Exception as e:
                    Badroom = 0
                    print(e)
                try:
                    if plan_name =='South Beach Plan':
                        BaseSqft = '6680'
                        Full_Bath = 4
                        Half_Bath = 2
                    elif plan_name=='Mustique Plan':
                        BaseSqft = '3881'
                        Full_Bath = 4
                        Half_Bath = 1
                    elif plan_name =='Salvadore Plan':
                        BaseSqft = '4923'
                        Full_Bath = 3
                        Half_Bath = 1
                    elif plan_name =='Snowberry Plan':
                        BaseSqft = '4045'
                        Full_Bath = 5
                        Half_Bath = 1
                except Exception as e:
                    print(e)
                try:
                    Garage = 0
                except Exception as e:
                    Garage = 0
                    print(e)
                try:
                    description = 'AQUA Custom Homes is a full service construction company with 26 years in the industry. We’ve built more than 250,000 sq ft of commercial buildings and over 120 homes throughout the Midwest and south west Florida.'
                except Exception as e:
                    description = 'AQUA Custom Homes is a full service construction company with 26 years in the industry. We’ve built more than 250,000 sq ft of commercial buildings and over 120 homes throughout the Midwest and south west Florida.'
                    print(e)
                try:
                    ElevationImage = 'http://www.aquacustomhomes.com/wp-content/uploads/2017/06/DSC7284.jpg|http://www.aquacustomhomes.com/wp-content/uploads/2017/06/DSC7408.jpg|http://www.aquacustomhomes.com/wp-content/uploads/2017/06/DSC7408.jpg'
                except Exception as e:
                    print(e)

                unique = str(int(hashlib.md5(bytes(response.url+plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
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
                item['Baths'] = Full_Bath
                item['HalfBaths'] = Half_Bath
                item['Bedrooms'] = Badroom
                item['Garage'] = Garage
                item['Description'] = description
                item['ElevationImage'] = ElevationImage
                item['PlanWebsite'] = response.url
                item['unique_number'] = unique_number
                yield item

            else:
                pass



if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl aquacustomhomes".split())