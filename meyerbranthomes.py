# -*- coding: utf-8 -*-
import hashlib
import re

import scrapy

from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec


class ComfortHomesSpider(scrapy.Spider):
    name = 'meyerbranthomes'
    allowed_domains = []
    start_urls = ['http://www.meyerbranthomes.com/']

    builderNumber = "511930153231946923549710181693"

    def parse(self, response):

        # fake communities
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
        item['Street1'] = '259 E Torrey St'
        item['City'] = 'New Braunfels'
        item['State'] = 'TX'
        item['ZIP'] = '78130'
        item['AreaCode'] = '830'
        item['Prefix'] = '515'
        item['Suffix'] = '3010'
        item['Extension'] = ""
        item['Email'] = "office@meyerbranthomes.com"
        item['SubDescription'] = ''.join(response.xpath('//div[@class="wpb_wrapper"]/p/text()').extract())
        item['SubImage'] = "https://www.meyerbranthomes.com/wp-content/uploads/2021/03/custom-home-builder-located-in-new-braunfels-tx.jpg|https://www.meyerbranthomes.com/wp-content/uploads/2021/03/604-hannahs.jpg"
        item['SubWebsite'] = ""
        item['AmenityType']=''
        yield item

    #
    #     planpage_link = response.xpath('//div[@class="col-md-6 col-lg-8 col-sm-6 col-xs-12 topNav"]//li[@id="menu-item-1066"]/a/@href').extract_first().strip()
    #     print(planpage_link)
    #     yield scrapy.Request(url=planpage_link, callback=self.planspage, meta={'sbdn': item['BuilderNumber']})
    #
    # def planspage(self, response):
    #     SubdivisionNumber = response.meta['sbdn']
    #     plan_links = response.xpath('//div[@class="col-md-3 col-lg-3 sidebar"]/ul/li/a/@href').extract()
    #     plan_links.remove(plan_links[-1])
    #     plan_links.remove(plan_links[-1])
    #     for links in plan_links:
    #         yield scrapy.Request(url=links, callback=self.plandetails, meta={'sbdn': SubdivisionNumber})
    #
    #
    # def plandetails(self, response):
    #     site_text = response.text
    #     site_text = re.sub(r'\<.*?.\>', '', site_text)
    #     regex = ''.join(re.findall(r'\$(\d+,\d+)', site_text))
    #     plans = response.url
    #     if plans != "http://www.meyerbranthomes.com/available-lots-homes/680-acorn-drive/":
    #         if regex == '':
    #             site_text = response.text
    #             try:
    #                 Type = 'SingleFamily'
    #             except Exception as e:
    #                 print(e)
    #
    #             try:
    #                 PlanNumber = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
    #             except Exception as e:
    #                 print(e)
    #
    #             try:
    #                 SubdivisionNumber = response.meta['sbdn']
    #             except Exception as e:
    #                 print(str(e))
    #
    #             try:
    #                 PlanNotAvailable = 0
    #             except Exception as e:
    #                 print(e)
    #
    #             try:
    #                 PlanTypeName = 'Single Family'
    #             except Exception as e:
    #                 print(e)
    #
    #             try:
    #                 BasePrice = 0.00
    #             except Exception as e:
    #                 print(e)
    #
    #             try:
    #                 PlanWebsite = response.url
    #             except Exception as e:
    #                 print(e)
    #
    #             try:
    #                 PlanName = plans.split('/')[-2].strip()
    #             except Exception as e:
    #                 print(e)
    #
    #             try:
    #                 Bedrooms = re.findall(r'(\d+) BEDROOMS', site_text)[0].strip()
    #                 Baths = re.findall(r'(\d+) BATHROOM', site_text)[0].strip()
    #                 Garage = re.findall(r'(\d+) CAR OVER SIZED GARAGE', site_text)[0].strip()
    #                 BaseSqft = 0
    #             except Exception as e:
    #                 print(str(e))
    #
    #             try:
    #                 ElevationImage = response.xpath('//div[@class="vc_row wpb_row row"]//figure//img/@src').extract()
    #             except Exception as e:
    #                 print(str(e))
    #
    #             unique = str(PlanNumber) + str(SubdivisionNumber)  # < -------- Changes here
    #             unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
    #             item = BdxCrawlingItem_Plan()
    #             item['Type'] = Type
    #             item['PlanNumber'] = PlanNumber
    #             item['unique_number'] = unique_number  # < -------- Changes here
    #             item['SubdivisionNumber'] = SubdivisionNumber
    #             item['PlanName'] = PlanName
    #             item['PlanNotAvailable'] = PlanNotAvailable
    #             item['PlanTypeName'] = PlanTypeName
    #             item['BasePrice'] = BasePrice
    #             item['BaseSqft'] = BaseSqft
    #             item['Baths'] = Baths
    #             item['HalfBaths'] = 0
    #             item['Bedrooms'] = Bedrooms
    #             item['Garage'] = Garage
    #             item['Description'] = ''
    #             item['ElevationImage'] = '|'.join(ElevationImage)
    #             item['PlanWebsite'] = PlanWebsite
    #             yield item
    #
    #     try:
    #         homepage_link = 'http://www.meyerbranthomes.com/available-lots-homes/'
    #         yield scrapy.Request(url=homepage_link, callback=self.homespage, dont_filter=True)
    #     except Exception as e:
    #         print(str(e))
    #
    # def homespage(self, response):
    #     home_links111 = response.xpath('//div[@class="col-md-3 col-lg-3 sidebar"]/ul/li/a/@href').extract()
    #     home_links = response.xpath('//div[@class="col-md-3 col-lg-3 sidebar"]/ul/li/a/@href').extract()
    #     home_links.remove(home_links[-1])
    #     home_links.remove(home_links[-1])
    #     home_links.remove(home_links[-1])
    #     home_links.remove(home_links[-2])
    #
    #     for links in home_links:
    #         try:
    #             unique = str("Plan Unknown") + str(self.builderNumber)
    #             unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
    #             item = BdxCrawlingItem_Plan()
    #             item['unique_number'] = unique_number
    #             item['Type'] = "SingleFamily"
    #             item['PlanNumber'] = "Plan Unknown"
    #             item['SubdivisionNumber'] = self.builderNumber
    #             item['PlanName'] = "Plan Unknown"
    #             item['PlanNotAvailable'] = 1
    #             item['PlanTypeName'] = "Single Family"
    #             item['BasePrice'] = 0
    #             item['BaseSqft'] = 0
    #             item['Baths'] = 0
    #             item['HalfBaths'] = 0
    #             item['Bedrooms'] = 0
    #             item['Garage'] = 0
    #             item['Description'] = ""
    #             item['ElevationImage'] = ""
    #             item['PlanWebsite'] = ""
    #             yield item
    #         except Exception as e:
    #             print(str(e))
    #         Homes =  ['http://www.meyerbranthomes.com/available-lots-homes/684-acorn-drive/','http://www.meyerbranthomes.com/available-lots-homes/688-acorn-drive/','http://www.meyerbranthomes.com/available-lots-homes/672-acorn-drive/']
    #         for ho in Homes:
    #             yield scrapy.Request(url=ho, callback=self.homedetails, dont_filter=True, meta={'PN': unique_number})
    #
    #
    #
    # def homedetails(self, response):
    #     if response.url == 'http://www.meyerbranthomes.com/available-lots-homes/672-acorn-drive/':
    #         print("problem is ")
    #
    #
    #     site_text = response.text
    #     site_text = re.sub(r'\<.*?.\>', '', site_text)
    #     address = response.url
    #
    #     SpecStreet1 = address.split('/')[-2].strip()
    #     SpecCity = 'New Braunfels'
    #     SpecState = 'TX'
    #     SpecZIP = '78130'
    #
    #     unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
    #     SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
    #
    #     f = open("html/%s.html" % SpecNumber, "wb")
    #     f.write(response.body)
    #     f.close()
    #
    #     try:
    #         PlanNumber = response.meta['PN']
    #     except Exception as e:
    #         print(e)
    #
    #     try:
    #         SpecPrice1 = re.findall(r'\$(\d+,\d+)', site_text)[0]
    #         SpecPrice = SpecPrice1.replace('$', '')
    #         SpecPrice = re.sub(',', '', SpecPrice)
    #         SpecPrice = SpecPrice.strip()
    #     except Exception as e:
    #         SpecPrice = 0.00
    #
    #     try:
    #         Bedrooms = re.findall(r'(\d+) Bedrooms|(\d+) bedroom|(\d+) BEDROOMS', site_text)[0]
    #         SpecBedrooms = ''.join(Bedrooms)
    #     except Exception as e:
    #         SpecBedrooms = 0
    #         print(str(e))
    #
    #     try:
    #         Baths = re.findall(r'(\d+) Bathrooms|(\d+) bathrooms|(\d+) BATHROOM', site_text)[0]
    #         SpecBaths = ''.join(Baths)
    #     except Exception as e:
    #         SpecBaths = 0
    #         print(str(e))
    #
    #     try:
    #         Garage = re.findall(r'(\d+) Car over sized Garage|(\d+) car garage|(\d+) CAR OVER SIZED GARAGE', site_text)[0]
    #         SpecGarage = ''.join(Garage)
    #     except Exception as e:
    #         print(str(e))
    #
    #     try:
    #         SpecSqft1= ''.join(response.xpath('//div[@class="wpb_wrapper"]/p/text()').extract())
    #         SpecSqft = re.findall(r'(\d+,\d+)\sAC', SpecSqft1)[0]
    #         SpecSqft = SpecSqft.replace(',', '')
    #     except Exception as e:
    #         SpecSqft = 0
    #
    #
    #     try:
    #         MasterBedLocation = "Down"
    #     except Exception as e:
    #         print(e)
    #
    #     try:
    #         ElevationImage = response.xpath('//div[@class="vc_row wpb_row row"]//div[@class="wpb_column vc_column_container vc_col-sm-4"]//img/@src|//div[@class="vc_single_image-wrapper   vc_box_border_grey"]/img/@src|//div[@class="wpb_single_image wpb_content_element vc_align_left"]//a/@href').extract()
    #         # ElevationImage = ElevationImage1.replace('.jpg','.jpg|').replace(", ", "|")
    #         # etc = ElevationImage.split("|")
    #         # for i in etc:
    #         #     if 'http' not in i:
    #         #         etc.remove(i)
    #     except Exception as e:
    #         ElevationImage = ''
    #         print(str(e))
    #
    #     try:
    #         SpecWebsite = response.url
    #     except Exception as e:
    #         print(e)
    #
    #     # ----------------------- Don't change anything here ---------------- #
    #     try:
    #         item = BdxCrawlingItem_Spec()
    #         item['SpecNumber'] = SpecNumber
    #         item['PlanNumber'] = PlanNumber
    #         item['SpecStreet1'] = SpecStreet1
    #         item['SpecCity'] = SpecCity
    #         item['SpecState'] = SpecState
    #         item['SpecZIP'] = SpecZIP
    #         item['SpecCountry'] = "USA"
    #         item['SpecPrice'] = SpecPrice
    #         item['SpecSqft'] = SpecSqft
    #         item['SpecBaths'] = SpecBaths
    #         item['SpecHalfBaths'] = 0
    #         item['SpecBedrooms'] = SpecBedrooms
    #         item['MasterBedLocation'] = MasterBedLocation
    #         item['SpecGarage'] = SpecGarage
    #         item['SpecDescription'] = ''
    #         item['SpecElevationImage'] = '|'.join(ElevationImage)
    #         item['SpecWebsite'] = SpecWebsite
    #         yield item
    #     except Exception as e:
    #         print(str(e))



if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl meyerbranthomes".split())
