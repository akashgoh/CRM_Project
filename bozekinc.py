# # -*- coding: utf-8 -*-
# import scrapy
# import re
# import os
# import hashlib
# import scrapy
# from BDX_Crawling.items import BdxCrawlingItem_Builder, BdxCrawlingItem_Corporation, BdxCrawlingItem_Plan, \
#     BdxCrawlingItem_Spec, BdxCrawlingItem_subdivision
# import requests
# from scrapy.http import HtmlResponse
#
#
# class bozekinc(scrapy.Spider):
#     name = 'bozekinc'
#     allowed_domains = []
#     start_urls = ['http://bozekinc.com/']
#     builderNumber = '12562'
#     counter = 0
#
#     def parse(self, response):
#         images = ''
#         image = re.findall('url(\(.*?)\)', response.text)[2:]
#         for i in image:
#             images = images + i + '|'
#         images = images.strip('|').replace('(','').replace(')','')
#         item2 = BdxCrawlingItem_subdivision()
#         item2['sub_Status'] = "Active"
#         item2['SubdivisionNumber'] = ''
#         item2['BuilderNumber'] = self.builderNumber
#         item2['SubdivisionName'] = "No Sub Division"
#         item2['BuildOnYourLot'] = 0
#         item2['OutOfCommunity'] = 0
#         item2['Street1'] = '358 Pennsylvania Ave'
#         item2['City'] = 'Centreville'
#         item2['State'] = 'MD'
#         item2['ZIP'] = '21617'
#         item2['AreaCode'] = '410'
#         item2['Prefix'] = "758"
#         item2['Suffix'] = "2929"
#         item2['Extension'] = ""
#         item2['Email'] = "info@bozekinc.com"
#         item2['SubDescription'] = "Offering luxurious custom homes and an elite building – or buying –  experience for all…no matter the scope of your budget or the demands of your project."
#         item2['SubImage'] = images
#         item2['SubWebsite'] = ''
#         item2['AmenityType']=''
#         yield item2
#
#         url = 'http://bozekinc.com/available-properties/'
#         yield scrapy.FormRequest(url=url, dont_filter=True, callback=self.all_home)
#
#     def all_home(self, response):
#         links = response.xpath('//*[contains(text(),"More Details")]//@href').getall()
#         links.append('http://bozekinc.com/portfolio/125-hawk-circle-drive-lot-20/')
#         for link in links:
#             link = link
#             yield scrapy.Request(url=link, callback=self.HomesDetails,meta={"link":link}, dont_filter=True)
#             # yield scrapy.Request(url='http://bozekinc.com/portfolio/227-hawk-circle-drive/', callback=self.HomesDetails,meta={"link":link}, dont_filter=True)
#
#     def HomesDetails(self, response):
#         unique = str("Plan Unknown") + str(self.builderNumber) # < -------- Changes here
#         unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
#         item = BdxCrawlingItem_Plan()
#         item['unique_number'] = unique_number
#         item['Type'] = "SingleFamily"
#         item['PlanNumber'] = "Plan Unknown"
#         item['SubdivisionNumber'] = self.builderNumber
#         item['PlanName'] = "Plan Unknown"
#         item['PlanNotAvailable'] = 1
#         item['PlanTypeName'] = 'Single Family'
#         item['BasePrice'] = 0
#         item['BaseSqft'] = 0
#         item['Baths'] = 0
#         item['HalfBaths'] = 0
#         item['Bedrooms'] = 0
#         item['Garage'] = 0
#         item['Description'] = ""
#         item['ElevationImage'] = ""
#         item['PlanWebsite'] = ""
#         yield item
#
#         if 'Sold' and 'Coming Soon!' not in response.text:
#             a = response.xpath('//div[@class="wpb_wrapper"]/h3//text()|//div[@class="col span_12 section-title no-date"]/h1/text()').extract_first(default='')
#             print(a)
#             # if a:
#             #     a = a.strip()
#             # if 'Ridgely' in a or 'Ridgley, ' in a:
#             #     try:
#             #         SpecStreet1 = a.split(',')[0].replace('Ridgley', '')
#             #         if SpecStreet1:
#             #             SpecStreet1 = SpecStreet1.strip().replace('\xa0','')
#             #     except Exception as e:
#             #         SpecStreet1 = ''
#             #         print(e)
#             #     try:
#             #         SpecCity = 'Ridgley'
#             #     except Exception as e:
#             #         SpecCity = ''
#             #         print(e)
#             #     try:
#             #         d = a.split(',')[1].strip()
#             #     except Exception as e:
#             #         d = ''
#             #         print(e)
#             #     try:
#             #         SpecState = d.split(' ')[0].strip()
#             #         if SpecState:
#             #             SpecState = SpecState.strip()
#             #     except Exception as e:
#             #         SpecState = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecZIP = d.split(' ')[1].strip()
#             #     except Exception as  e:
#             #         SpecZIP = ''
#             #         print(e)
#             # else:
#             try:
#                 SpecStreet1 = a.split(',')[0]
#                 if SpecStreet1:
#                     SpecStreet1 = SpecStreet1.replace('\xa0','')
#             except Exception as e:
#                 SpecStreet1 = ''
#                 print(e)
#
#
#             try:
#                 d = a.split(',')[2].strip()
#             except:
#                 try:
#                     d = a.split(',')[1].strip()
#                     print(d)
#                 except:
#                     d = 0
#             try:
#                 SpecState = d.split(' ')[0].strip()
#                 if SpecState =='' or SpecState == "Lot":
#                     SpecState = 'MD'
#                 if SpecState:
#                     SpecState = SpecState.strip()
#             except Exception as e:
#                 SpecState = ""
#                 print(e)
#
#             try:
#                 SpecZIP = d.split(' ')[1].strip()
#                 print(type(SpecZIP))
#                 print(SpecZIP)
#                 if SpecZIP =='':
#                     SpecZIP = '21617'
#                 elif len(SpecZIP)<5:
#                     SpecZIP = "00000"
#                 else:SpecZIP = SpecZIP
#             except Exception as e:
#                 SpecZIP = '00000'
#                 print(e)
#
#             try:
#                 SpecCity = a.split(',')[1]
#                 if SpecCity:
#                     SpecCity = SpecCity.strip()
#                     if SpecZIP == '00000':
#                         SpecZIP = ''.join(re.findall(r"(\d{5})", str(SpecCity))).strip()
#                         print(SpecZIP)
#                         if SpecZIP:
#                             SpecCity = SpecState.replace(SpecCity,'')
#                             print(SpecCity)
#                         else:SpecZIP="00000"
#             except:
#                 try:
#                     SpecCity = ''.join(response.xpath('//*[@id="sidebar-inner"]/p[1]/text()[4]').extract()).split(',')[0]
#                     SpecState = ''.join(response.xpath('//*[@id="sidebar-inner"]/p[1]/text()[4]').extract()).split(',')[1]
#                 except:
#                     try:
#                         SpecCity = ''.join(response.xpath('//*[@id="sidebar-inner"]/p[1]/text()[3]').extract()).split(',')[0]
#                         SpecState = ''.join(response.xpath('//*[@id="sidebar-inner"]/p[1]/text()[3]').extract()).split(',')[1]
#                     except:
#                         SpecCity = ''
#                         SpecState = ''
#
#             # if SpecCity == SpecState:
#             #     SpecCity = ''
#             try:
#                 if SpecCity == '' or SpecCity == "MD":
#                     SpecCity = ''
#                     SpecCity = ''.join(response.xpath('//*[@id="sidebar-inner"]/p[1]/text()[4]').extract()).split(',')[0]
#                     SpecState = ''.join(response.xpath('//*[@id="sidebar-inner"]/p[1]/text()[4]').extract()).split(',')[1]
#                 else: SpecCity = SpecCity
#             except Exception as e:
#                 SpecCity = ''
#                 print(e, "problem in SpecCity", response.url)
#
#             try:
#                 if "Ridgely" in SpecStreet1 or "Ridgley" in SpecStreet1:
#                     SpecStreet1 = SpecStreet1.replace('Ridgely','').strip().replace('Ridgley','').strip()
#                     SpecCity = "Ridgely"
#                 else: SpecStreet1 = SpecStreet1
#             except Exception as e:
#                 print(e)
#
#
#             try:
#                 PlanNumber =unique_number
#             except Exception as e:
#                 print(e)
#
#
#             unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             # unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             # SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             f = open("html/%s.html" % SpecNumber, "wb")
#             f.write(response.body)
#             f.close()
#             SpecCountry = 'USA'
#
#             try:
#                 SpecPrice = response.xpath('//div[@class="wpb_wrapper"]//h1//text()').extract_first().strip().replace('$', '').replace(',', '').replace('*', '')
#             except:
#                 try:
#                     SpecPrice = response.xpath('//*[@id="sidebar-inner"]//h2/text()').extract_first().strip().replace('$', '').replace(',', '').replace('*', '')
#                 except:
#                     try:
#                         SpecPrice = response.xpath('//div[@id="sidebar-inner"]//h3/text()').extract_first().strip().replace('$', '').replace(',', '').replace('*', '')
#                     except:
#                         SpecPrice = 0
#
#
#
#             try:
#                 SpecSqft = response.xpath('//*[contains(text(),"sqft")]//text()').get().strip().replace(',', '')
#                 SpecSqft = re.findall(r"(\d+)", SpecSqft)[0]
#
#             except Exception as e:
#                 SpecSqft = 0
#                 print(e)
#
#             try:
#                 SpecBaths = response.xpath('//*[contains(text(),"Bathrooms")]//text()|//*[contains(text(),"Bathrooms")]//text()|//*[contains(text(),"Bathrooms")]//text()').get().strip()
#                 print(SpecBaths)
#                 if '1/2' in SpecBaths:
#                     SpecBaths = SpecBaths.replace('Bathrooms','').strip().split()
#                     SpecBaths = max(SpecBaths)
#                     print(SpecBaths)
#                     SpecHalfBaths = 1
#                 else:
#                     # tmp = re.findall(r"[ ]*(\d+[ ]*[½]*)[ ]*[bB]ath", SpecBaths)[0]
#                     tmp = re.findall(r"(\d+)", SpecBaths)[0]
#                     print(tmp)
#                     SpecBaths = tmp[0]
#                     print(SpecBaths)
#                     if len(tmp.replace(' ', '')) > 1:
#                         SpecHalfBaths = 1
#                     else:
#                         SpecHalfBaths = 0
#             except:
#                 SpecBaths = 0
#                 SpecHalfBaths = 0
#
#
#             try:
#                 SpecBedrooms = response.xpath('//*[contains(text(),"Bedrooms")]//text()|//*[contains(text(),"Bedrooms")]//text()').get().strip()
#                 SpecBedrooms = re.findall(r'(\d+)', SpecBedrooms)[0]
#             except Exception as e:
#                 SpecBedrooms = 0
#                 print(e)
#
#             try:
#                 MasterBedLocation = "Down"
#             except Exception as e:
#                 print(e)
#
#             try:
#                 SpecGarage = response.xpath('//*[contains(text(),"Garage")]//text()|//*[contains(text(),"Garage")]//text()').get(default=0).strip()
#                 SpecGarage = re.findall(r'(\d+)', SpecGarage)[0]
#             except Exception as e:
#                 SpecGarage = 0
#                 print(e)
#
#
#             try:
#                 SpecDescription =response.xpath('//div[@class="wpb_text_column wpb_content_element "]//p[1]//text()').getall()[-1]
#             except Exception as e:
#                 SpecDescription = 'Explore our Quick Delivery Homes, To-Be-Built Homes, and Land below.  Click on the type of home you are looking for to sort your options, then click to “View Details” to find out more. You can always contact '
#                 print(e)
#
#             try:
#                 images = ''
#                 image = re.findall('url(\(.*?)\)', response.text)[1:]
#                 for i in image:
#                     if 'http://bozekinc.com/new/wp-content/uploads' in i:
#                         images = images + i + '|'
#                 images = images.strip('|').replace('(', '').replace(')', '').replace('\\', '').replace("'", '')
#                 SpecElevationImage = images
#             except Exception as e:
#                 SpecElevationImage = ''
#                 print(e)
#             try:
#                 coverimg = response.xpath('//div[@class="container main-content"]//div/img/@src').extract_first()
#                 if coverimg:
#                     SpecElevationImage = SpecElevationImage+"|"+coverimg
#                     SpecElevationImage = SpecElevationImage.strip("|")
#                 else: coverimg = ''
#             except Exception as e:
#                 print(e)
#
#             if SpecCity == "Lot 2 Parcel Second":
#                 SpecCity = ''
#             else:SpecCity = SpecCity
#
#             # if SpecZIP:
#             #     if len(SpecZIP)<5:
#             #         SpecZIP = '00000'
#             #     else: SpecZIP = SpecZIP
#
#             try:
#                 SpecWebsite = response.url
#             except Exception as e:
#                 print(e)
#             if SpecCity != '':
#                     # ----------------------- Don't change anything here ---------------- #
#                 item = BdxCrawlingItem_Spec()
#                 item['SpecNumber'] = SpecNumber
#                 item['PlanNumber'] = PlanNumber
#                 item['SpecStreet1'] = SpecStreet1
#                 item['SpecCity'] = SpecCity
#                 # item['SpecState'] = SpecState
#                 item['SpecState'] = "MD"
#                 item['SpecZIP'] = SpecZIP
#                 item['SpecCountry'] = SpecCountry
#                 item['SpecPrice'] = SpecPrice
#                 item['SpecSqft'] = SpecSqft
#                 item['SpecBaths'] = SpecBaths
#                 item['SpecHalfBaths'] = SpecHalfBaths
#                 item['SpecBedrooms'] = SpecBedrooms
#                 item['MasterBedLocation'] = MasterBedLocation
#                 item['SpecGarage'] = SpecGarage
#                 item['SpecDescription'] = SpecDescription
#                 item['SpecElevationImage'] = SpecElevationImage
#                 item['SpecWebsite'] = SpecWebsite
#                 print(item)
#                 yield item
#             else:
#                 pass
#
# if __name__ == '__main__':
#     from scrapy.cmdline import execute
#     execute("scrapy crawl bozekinc".split())
#
#
#             # ===============================================================================/
#             # if response.url =='http://bozekinc.com/portfolio/124-condor-court/':
#             #     try:
#             #         SpecStreet1 = '124 Condor Court Lot 11'
#             #     except Exception as e:
#             #         SpecStreet1 = ''
#             #         print(e)
#             #     try:
#             #         SpecCity = 'Eagle Manor'
#             #     except Exception as e:
#             #         SpecCity = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecState = 'MD'
#             #     except Exception as e:
#             #         SpecState = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecZIP = ''
#             #     except Exception as  e:
#             #         SpecZIP = ''
#             #         print(e)
#             #
#             #     try:
#             #         PlanNumber = unique_number
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         if SpecCity == '' or SpecState == '' or SpecZIP == '':
#             #             unique = SpecStreet1
#             #         else:
#             #             unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             #         SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             #         f = open("html/%s.html" % SpecNumber, "wb")
#             #         f.write(response.body)
#             #         f.close()
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     SpecCountry = 'USA'
#             #
#             #     try:
#             #         SpecPrice = '68000'
#             #     except Exception as e:
#             #         SpecPrice = 0.0
#             #         print(e)
#             #
#             #     try:
#             #         SpecSqft = response.xpath('//*[contains(text(),"sqft")]//text()').get().strip().replace(',', '')
#             #         SpecSqft = re.findall(r"(\d+)", SpecSqft)[0]
#             #
#             #     except Exception as e:
#             #         SpecSqft = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBaths = response.xpath(
#             #             '//*[contains(text(),"Bathrooms")]//text()|//*[contains(text(),"Bathrooms")]//text()').get().strip()
#             #         # if '1/2' in SpecBaths:
#             #         #     SpecHalfBaths = 1
#             #         tmp = re.findall(r"[ ]*(\d+[ ]*[½]*)[ ]*[bB]ath", SpecBaths)[0]
#             #         SpecBaths = tmp[0]
#             #         if len(tmp.replace(' ', '')) > 1:
#             #             SpecHalfBaths = 1
#             #         else:
#             #             SpecHalfBaths = 0
#             #
#             #     except Exception as e:
#             #         SpecBaths = 0
#             #         SpecHalfBaths = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBedrooms = response.xpath('//*[contains(text(),"Bedrooms")]//text()').get().strip()
#             #         SpecBedrooms = re.findall(r'(\d+)', SpecBedrooms)[0]
#             #     except Exception as e:
#             #         SpecBedrooms = 0
#             #         print(e)
#             #
#             #     try:
#             #         MasterBedLocation = "Down"
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         SpecGarage = response.xpath('//*[contains(text(),"Garage")]//text()').get(default=0).strip()
#             #         SpecGarage = re.findall(r'(\d+)', SpecGarage)[0]
#             #
#             #     except Exception as e:
#             #         print(e)
#             #         SpecGarage = 0
#             #
#             #     try:
#             #         SpecDescription = \
#             #         response.xpath('//div[@class="wpb_text_column wpb_content_element "]//p[1]//text()').getall()[-1]
#             #     except Exception as e:
#             #         SpecDescription = ''
#             #         print(e)
#             #
#             #     try:
#             #         images = ''
#             #         image = re.findall('url(\(.*?)\)', response.text)[1:]
#             #         for i in image:
#             #             if 'http://bozekinc.com/new/wp-content/uploads' in i:
#             #                 images = images + i + '|'
#             #         images = images.strip('|').replace('(', '').replace(')', '').replace('\\', '').replace("'", '')
#             #         SpecElevationImage = images
#             #     except Exception as e:
#             #         SpecElevationImage = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecWebsite = response.url
#             #     except Exception as e:
#             #         print(e)
#             #
#             #         # ----------------------- Don't change anything here ---------------- #
#             #     item = BdxCrawlingItem_Spec()
#             #     item['SpecNumber'] = SpecNumber
#             #     item['PlanNumber'] = PlanNumber
#             #     item['SpecStreet1'] = SpecStreet1
#             #     item['SpecCity'] = SpecCity
#             #     item['SpecState'] = SpecState
#             #     item['SpecZIP'] = SpecZIP
#             #     item['SpecCountry'] = SpecCountry
#             #     item['SpecPrice'] = SpecPrice
#             #     item['SpecSqft'] = SpecSqft
#             #     item['SpecBaths'] = SpecBaths
#             #     item['SpecHalfBaths'] = SpecHalfBaths
#             #     item['SpecBedrooms'] = SpecBedrooms
#             #     item['MasterBedLocation'] = MasterBedLocation
#             #     item['SpecGarage'] = SpecGarage
#             #     item['SpecDescription'] = SpecDescription
#             #     item['SpecElevationImage'] = SpecElevationImage
#             #     item['SpecWebsite'] = SpecWebsite
#             #     yield item
#             #
#             #
#             # if response.url == 'http://bozekinc.com/portfolio/118-condor-court-lot-12/':
#             #     try:
#             #         SpecStreet1 = '118 Condor Court Lot 12'
#             #     except Exception as e:
#             #         SpecStreet1 = ''
#             #         print(e)
#             #     try:
#             #         SpecCity = 'Eagle Manor'
#             #     except Exception as e:
#             #         SpecCity = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecState = 'MD'
#             #     except Exception as e:
#             #         SpecState = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecZIP = ''
#             #     except Exception as  e:
#             #         SpecZIP = ''
#             #         print(e)
#             #
#             #     try:
#             #         PlanNumber = unique_number
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         # self.counter +=1
#             #         # ifSpecCity == '' or SpecState == '' or SpecZIP == '':
#             #         #     unique = SpecStreet1
#             #         # else:
#             #         #     unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             #
#             #         unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             #         SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             #         # SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             #         f = open("html/%s.html" % SpecNumber, "wb")
#             #         f.write(response.body)
#             #         f.close()
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     SpecCountry = 'USA'
#             #
#             #     try:
#             #         SpecPrice = '68000'
#             #     except Exception as e:
#             #         SpecPrice = 0.0
#             #         print(e)
#             #
#             #     try:
#             #         SpecSqft = response.xpath('//*[contains(text(),"sqft")]//text()').get().strip().replace(',', '')
#             #         SpecSqft = re.findall(r"(\d+)", SpecSqft)[0]
#             #
#             #     except Exception as e:
#             #         SpecSqft = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBaths = response.xpath(
#             #             '//*[contains(text(),"Bathrooms")]//text()|//*[contains(text(),"Bathrooms")]//text()').get().strip()
#             #         # if '1/2' in SpecBaths:
#             #         #     SpecHalfBaths = 1
#             #         tmp = re.findall(r"[ ]*(\d+[ ]*[½]*)[ ]*[bB]ath", SpecBaths)[0]
#             #         SpecBaths = tmp[0]
#             #         if len(tmp.replace(' ', '')) > 1:
#             #             SpecHalfBaths = 1
#             #         else:
#             #             SpecHalfBaths = 0
#             #
#             #     except Exception as e:
#             #         SpecBaths = 0
#             #         SpecHalfBaths = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBedrooms = response.xpath('//*[contains(text(),"Bedrooms")]//text()').get().strip()
#             #         SpecBedrooms = re.findall(r'(\d+)', SpecBedrooms)[0]
#             #     except Exception as e:
#             #         SpecBedrooms = 0
#             #         print(e)
#             #
#             #     try:
#             #         MasterBedLocation = "Down"
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         SpecGarage = response.xpath('//*[contains(text(),"Garage")]//text()').get(default=0).strip()
#             #         SpecGarage = re.findall(r'(\d+)', SpecGarage)[0]
#             #
#             #     except Exception as e:
#             #         print(e)
#             #         SpecGarage = 0
#             #
#             #     try:
#             #         SpecDescription = \
#             #         response.xpath('//div[@class="wpb_text_column wpb_content_element "]//p[1]//text()').getall()[-1]
#             #     except Exception as e:
#             #         SpecDescription = ''
#             #         print(e)
#             #
#             #     try:
#             #         images = ''
#             #         image = re.findall('url(\(.*?)\)', response.text)[1:]
#             #         for i in image:
#             #             if 'http://bozekinc.com/new/wp-content/uploads' in i:
#             #                 images = images + i + '|'
#             #         images = images.strip('|').replace('(', '').replace(')', '').replace('\\', '').replace("'", '')
#             #         SpecElevationImage = images
#             #     except Exception as e:
#             #         SpecElevationImage = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecWebsite = response.url
#             #     except Exception as e:
#             #         print(e)
#             #
#             #         # ----------------------- Don't change anything here ---------------- #
#             #     item = BdxCrawlingItem_Spec()
#             #     item['SpecNumber'] = SpecNumber
#             #     item['PlanNumber'] = PlanNumber
#             #     item['SpecStreet1'] = SpecStreet1
#             #     item['SpecCity'] = SpecCity
#             #     item['SpecState'] = SpecState
#             #     item['SpecZIP'] = SpecZIP
#             #     item['SpecCountry'] = SpecCountry
#             #     item['SpecPrice'] = SpecPrice
#             #     item['SpecSqft'] = SpecSqft
#             #     item['SpecBaths'] = SpecBaths
#             #     item['SpecHalfBaths'] = SpecHalfBaths
#             #     item['SpecBedrooms'] = SpecBedrooms
#             #     item['MasterBedLocation'] = MasterBedLocation
#             #     item['SpecGarage'] = SpecGarage
#             #     item['SpecDescription'] = SpecDescription
#             #     item['SpecElevationImage'] = SpecElevationImage
#             #     item['SpecWebsite'] = SpecWebsite
#             #     yield item
#             #
#             #
#             #
#             #
#             #
#             #
#             # if response.url =='http://bozekinc.com/portfolio/125-hawk-circle-drive-lot-20/':
#             #     try:
#             #         SpecStreet1 = '125 Hawk Circle Drive Lot 20'
#             #     except Exception as e:
#             #         SpecStreet1 = ''
#             #         print(e)
#             #     try:
#             #         SpecCity = 'Eagle Manor'
#             #     except Exception as e:
#             #         SpecCity = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecState = 'MD'
#             #     except Exception as e:
#             #         SpecState = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecZIP = ''
#             #     except Exception as  e:
#             #         SpecZIP = ''
#             #         print(e)
#             #
#             #     try:
#             #         PlanNumber = unique_number
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         # self.counter +=1
#             #         if SpecCity == '' or SpecState == '' or SpecZIP == '':
#             #             unique = SpecStreet1
#             #         else:
#             #             unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             #         SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             #         f = open("html/%s.html" % SpecNumber, "wb")
#             #         f.write(response.body)
#             #         f.close()
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     SpecCountry = 'USA'
#             #
#             #     try:
#             #         SpecPrice = '68000'
#             #     except Exception as e:
#             #         SpecPrice = 0.0
#             #         print(e)
#             #
#             #     try:
#             #         SpecSqft = response.xpath('//*[contains(text(),"sqft")]//text()').get().strip().replace(',', '')
#             #         SpecSqft = re.findall(r"(\d+)", SpecSqft)[0]
#             #
#             #     except Exception as e:
#             #         SpecSqft = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBaths = response.xpath(
#             #             '//*[contains(text(),"Bathrooms")]//text()|//*[contains(text(),"Bathrooms")]//text()').get().strip()
#             #         # if '1/2' in SpecBaths:
#             #         #     SpecHalfBaths = 1
#             #         tmp = re.findall(r"[ ]*(\d+[ ]*[½]*)[ ]*[bB]ath", SpecBaths)[0]
#             #         SpecBaths = tmp[0]
#             #         if len(tmp.replace(' ', '')) > 1:
#             #             SpecHalfBaths = 1
#             #         else:
#             #             SpecHalfBaths = 0
#             #
#             #     except Exception as e:
#             #         SpecBaths = 0
#             #         SpecHalfBaths = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBedrooms = response.xpath('//*[contains(text(),"Bedrooms")]//text()').get().strip()
#             #         SpecBedrooms = re.findall(r'(\d+)', SpecBedrooms)[0]
#             #     except Exception as e:
#             #         SpecBedrooms = 0
#             #         print(e)
#             #
#             #     try:
#             #         MasterBedLocation = "Down"
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         SpecGarage = response.xpath('//*[contains(text(),"Garage")]//text()').get(default=0).strip()
#             #         SpecGarage = re.findall(r'(\d+)', SpecGarage)[0]
#             #
#             #     except Exception as e:
#             #         print(e)
#             #         SpecGarage = 0
#             #
#             #     try:
#             #         SpecDescription = \
#             #         response.xpath('//div[@class="wpb_text_column wpb_content_element "]//p[1]//text()').getall()[-1]
#             #     except Exception as e:
#             #         SpecDescription = ''
#             #         print(e)
#             #
#             #     try:
#             #         images = ''
#             #         image = re.findall('url(\(.*?)\)', response.text)[1:]
#             #         for i in image:
#             #             if 'http://bozekinc.com/new/wp-content/uploads' in i:
#             #                 images = images + i + '|'
#             #         images = images.strip('|').replace('(', '').replace(')', '').replace('\\', '').replace("'", '')
#             #         SpecElevationImage = images
#             #     except Exception as e:
#             #         SpecElevationImage = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecWebsite = response.url
#             #     except Exception as e:
#             #         print(e)
#             #
#             #         # ----------------------- Don't change anything here ---------------- #
#             #     item = BdxCrawlingItem_Spec()
#             #     item['SpecNumber'] = SpecNumber
#             #     item['PlanNumber'] = PlanNumber
#             #     item['SpecStreet1'] = SpecStreet1
#             #     item['SpecCity'] = SpecCity
#             #     item['SpecState'] = SpecState
#             #     item['SpecZIP'] = SpecZIP
#             #     item['SpecCountry'] = SpecCountry
#             #     item['SpecPrice'] = SpecPrice
#             #     item['SpecSqft'] = SpecSqft
#             #     item['SpecBaths'] = SpecBaths
#             #     item['SpecHalfBaths'] = SpecHalfBaths
#             #     item['SpecBedrooms'] = SpecBedrooms
#             #     item['MasterBedLocation'] = MasterBedLocation
#             #     item['SpecGarage'] = SpecGarage
#             #     item['SpecDescription'] = SpecDescription
#             #     item['SpecElevationImage'] = SpecElevationImage
#             #     item['SpecWebsite'] = SpecWebsite
#             #     yield item
#             #
#             # if response.url == 'http://bozekinc.com/portfolio/227-hawk-circle-drive-lot-27/':
#             #     try:
#             #         SpecStreet1 = '244 Hawk Circle Drive Lot 27'
#             #     except Exception as e:
#             #         SpecStreet1 = ''
#             #         print(e)
#             #     try:
#             #         SpecCity = 'Eagle Manor'
#             #     except Exception as e:
#             #         SpecCity = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecState = 'MD'
#             #     except Exception as e:
#             #         SpecState = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecZIP = ''
#             #     except Exception as  e:
#             #         SpecZIP = ''
#             #         print(e)
#             #
#             #     try:
#             #         PlanNumber = unique_number
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         # self.counter +=1
#             #         if SpecCity == '' or SpecState == '' or SpecZIP == '':
#             #             unique = SpecStreet1
#             #         else:
#             #             unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             #         SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             #         f = open("html/%s.html" % SpecNumber, "wb")
#             #         f.write(response.body)
#             #         f.close()
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     SpecCountry = 'USA'
#             #
#             #     try:
#             #         SpecPrice = '68000'
#             #     except Exception as e:
#             #         SpecPrice = 0.0
#             #         print(e)
#             #
#             #     try:
#             #         SpecSqft = response.xpath('//*[contains(text(),"sqft")]//text()').get().strip().replace(',', '')
#             #         SpecSqft = re.findall(r"(\d+)", SpecSqft)[0]
#             #
#             #     except Exception as e:
#             #         SpecSqft = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBaths = response.xpath(
#             #             '//*[contains(text(),"Bathrooms")]//text()|//*[contains(text(),"Bathrooms")]//text()').get().strip()
#             #         # if '1/2' in SpecBaths:
#             #         #     SpecHalfBaths = 1
#             #         tmp = re.findall(r"[ ]*(\d+[ ]*[½]*)[ ]*[bB]ath", SpecBaths)[0]
#             #         SpecBaths = tmp[0]
#             #         if len(tmp.replace(' ', '')) > 1:
#             #             SpecHalfBaths = 1
#             #         else:
#             #             SpecHalfBaths = 0
#             #
#             #     except Exception as e:
#             #         SpecBaths = 0
#             #         SpecHalfBaths = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBedrooms = response.xpath('//*[contains(text(),"Bedrooms")]//text()').get().strip()
#             #         SpecBedrooms = re.findall(r'(\d+)', SpecBedrooms)[0]
#             #     except Exception as e:
#             #         SpecBedrooms = 0
#             #         print(e)
#             #
#             #     try:
#             #         MasterBedLocation = "Down"
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         SpecGarage = response.xpath('//*[contains(text(),"Garage")]//text()').get(default=0).strip()
#             #         SpecGarage = re.findall(r'(\d+)', SpecGarage)[0]
#             #
#             #     except Exception as e:
#             #         print(e)
#             #         SpecGarage = 0
#             #
#             #     try:
#             #         SpecDescription = \
#             #         response.xpath('//div[@class="wpb_text_column wpb_content_element "]//p[1]//text()').getall()[-1]
#             #     except Exception as e:
#             #         SpecDescription = ''
#             #         print(e)
#             #
#             #     try:
#             #         images = ''
#             #         image = re.findall('url(\(.*?)\)', response.text)[1:]
#             #         for i in image:
#             #             if 'http://bozekinc.com/new/wp-content/uploads' in i:
#             #                 images = images + i + '|'
#             #         images = images.strip('|').replace('(', '').replace(')', '').replace('\\', '').replace("'", '')
#             #         SpecElevationImage = images
#             #     except Exception as e:
#             #         SpecElevationImage = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecWebsite = response.url
#             #     except Exception as e:
#             #         print(e)
#             #
#             #         # ----------------------- Don't change anything here ---------------- #
#             #     item = BdxCrawlingItem_Spec()
#             #     item['SpecNumber'] = SpecNumber
#             #     item['PlanNumber'] = PlanNumber
#             #     item['SpecStreet1'] = SpecStreet1
#             #     item['SpecCity'] = SpecCity
#             #     item['SpecState'] = SpecState
#             #     item['SpecZIP'] = SpecZIP
#             #     item['SpecCountry'] = SpecCountry
#             #     item['SpecPrice'] = SpecPrice
#             #     item['SpecSqft'] = SpecSqft
#             #     item['SpecBaths'] = SpecBaths
#             #     item['SpecHalfBaths'] = SpecHalfBaths
#             #     item['SpecBedrooms'] = SpecBedrooms
#             #     item['MasterBedLocation'] = MasterBedLocation
#             #     item['SpecGarage'] = SpecGarage
#             #     item['SpecDescription'] = SpecDescription
#             #     item['SpecElevationImage'] = SpecElevationImage
#             #     item['SpecWebsite'] = SpecWebsite
#             #     yield item
#             #
#             #
#             #
#             #
#             #
#             #
#             # # ==========================================================================================
#             # if response.url == 'http://bozekinc.com/portfolio/244-hawk-circle-drive/':
#             #     try:
#             #         SpecStreet1 = '244 Hawk Circle Drive'
#             #     except Exception as e:
#             #         SpecStreet1 = ''
#             #         print(e)
#             #     try:
#             #         SpecCity = 'Eagle Manor'
#             #     except Exception as e:
#             #         SpecCity = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecState = 'MD'
#             #     except Exception as e:
#             #         SpecState = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecZIP = ''
#             #     except Exception as  e:
#             #         SpecZIP = ''
#             #         print(e)
#             #
#             #     try:
#             #         PlanNumber = unique_number
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         # self.counter +=1
#             #         if SpecCity == '' or SpecState == '' or SpecZIP == '':
#             #             unique = SpecStreet1
#             #         else:
#             #             unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
#             #         SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
#             #         f = open("html/%s.html" % SpecNumber, "wb")
#             #         f.write(response.body)
#             #         f.close()
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     SpecCountry = 'USA'
#             #
#             #     try:
#             #         SpecPrice = '68000'
#             #     except Exception as e:
#             #         SpecPrice = 0.0
#             #         print(e)
#             #
#             #     try:
#             #         SpecSqft = response.xpath('//*[contains(text(),"sqft")]//text()').get().strip().replace(',', '')
#             #         SpecSqft = re.findall(r"(\d+)", SpecSqft)[0]
#             #
#             #     except Exception as e:
#             #         SpecSqft = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBaths = response.xpath(
#             #             '//*[contains(text(),"Bathrooms")]//text()|//*[contains(text(),"Bathrooms")]//text()').get().strip()
#             #         # if '1/2' in SpecBaths:
#             #         #     SpecHalfBaths = 1
#             #         tmp = re.findall(r"[ ]*(\d+[ ]*[½]*)[ ]*[bB]ath", SpecBaths)[0]
#             #         SpecBaths = tmp[0]
#             #         if len(tmp.replace(' ', '')) > 1:
#             #             SpecHalfBaths = 1
#             #         else:
#             #             SpecHalfBaths = 0
#             #
#             #     except Exception as e:
#             #         SpecBaths = 0
#             #         SpecHalfBaths = 0
#             #         print(e)
#             #
#             #     try:
#             #         SpecBedrooms = response.xpath('//*[contains(text(),"Bedrooms")]//text()').get().strip()
#             #         SpecBedrooms = re.findall(r'(\d+)', SpecBedrooms)[0]
#             #     except Exception as e:
#             #         SpecBedrooms = 0
#             #         print(e)
#             #
#             #     try:
#             #         MasterBedLocation = "Down"
#             #     except Exception as e:
#             #         print(e)
#             #
#             #     try:
#             #         SpecGarage = response.xpath('//*[contains(text(),"Garage")]//text()').get(default=0).strip()
#             #         SpecGarage = re.findall(r'(\d+)', SpecGarage)[0]
#             #
#             #     except Exception as e:
#             #         print(e)
#             #         SpecGarage = 0
#             #
#             #     try:
#             #         SpecDescription = response.xpath('//div[@class="wpb_text_column wpb_content_element "]//p[1]//text()').getall()[-1]
#             #     except Exception as e:
#             #         SpecDescription = ''
#             #         print(e)
#             #
#             #     try:
#             #         images = ''
#             #         image = re.findall('url(\(.*?)\)', response.text)[1:]
#             #         for i in image:
#             #             if 'http://bozekinc.com/new/wp-content/uploads' in i:
#             #                 images = images + i + '|'
#             #         images = images.strip('|').replace('(', '').replace(')', '').replace('\\', '').replace("'", '')
#             #         SpecElevationImage = images
#             #     except Exception as e:
#             #         SpecElevationImage = ''
#             #         print(e)
#             #
#             #     try:
#             #         SpecWebsite = response.url
#             #     except Exception as e:
#             #         print(e)
#             #
#             #         # ----------------------- Don't change anything here ---------------- #
#             #     item = BdxCrawlingItem_Spec()
#             #     item['SpecNumber'] = SpecNumber
#             #     item['PlanNumber'] = PlanNumber
#             #     item['SpecStreet1'] = SpecStreet1
#             #     item['SpecCity'] = SpecCity
#             #     item['SpecState'] = SpecState
#             #     item['SpecZIP'] = SpecZIP
#             #     item['SpecCountry'] = SpecCountry
#             #     item['SpecPrice'] = SpecPrice
#             #     item['SpecSqft'] = SpecSqft
#             #     item['SpecBaths'] = SpecBaths
#             #     item['SpecHalfBaths'] = SpecHalfBaths
#             #     item['SpecBedrooms'] = SpecBedrooms
#             #     item['MasterBedLocation'] = MasterBedLocation
#             #     item['SpecGarage'] = SpecGarage
#             #     item['SpecDescription'] = SpecDescription
#             #     item['SpecElevationImage'] = SpecElevationImage
#             #     item['SpecWebsite'] = SpecWebsite
#             #     yield item
#
#
#
#
#
