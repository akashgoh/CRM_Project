# -*- coding: utf-8 -*-
import hashlib
import re
import scrapy
from scrapy.utils.response import open_in_browser
import requests
from scrapy.http import HtmlResponse
from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec

class ScoutconstructionllcSpider(scrapy.Spider):
    name = 'scoutconstructionllc'
    allowed_domains = []
    start_urls = ['https://scoutconstructionllc.net/properties/?filter_sort_by=published&filter_order=DESC','https://scoutconstructionllc.net/properties/page/2/?filter_sort_by=published&filter_order=DESC']

    builderNumber = "117603512729514558080849843539"

    def parse(self, response):

        links_f = [self.start_urls]
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
        item['Street1'] = "PO Box 288"
        item['City'] = "Watkinsville"
        item['State'] = "GA"
        item['ZIP'] = "30677"
        item['AreaCode'] = "706"
        item['Prefix'] = "310"
        item['Suffix'] = "4245"
        item['Extension'] = ""
        item['Email'] = "info@scoutconstructionllc.net"
        item['SubDescription'] = "Welcome to Scout Construction, expert home builders, offering new homes for sale in Oconee County. Whether you are looking for a new home in Oconee County or if you interested in building a dream home on your lot, Scout Construction has the experience and a custom floor plan for you. We build homes exclusively in Oconee County, Georgia including Watkinsville, Bogart and Bishop.  If you are searching for Real Estate and Homes for Sale contact us today and get more information. Did you know that Scout Construction builds new homes ideal for families affiliated with or interested in attending the Oconee County School District. Grades pre-school to twelve with six elementary schools, two middle schools, and two high schools. The Oconee County School District has 361 full-time teachers and over 5,615 students. We also have higher education including Gainesville State College, which operates a satellite campus near Watkinsville after merging with North Georgia College and State University in 2012 to become The University of North Georgia. Finally our proximity to the University of Georgia draws families looking for new homes for sale in our communities with custom built homes.  We’ve created this web site to help answer your search questions, please browse our listings of homes for sale or search by new home communities, below: We build beautiful homes in Oconee County and surrounding areas. Please click on one of our newest home communities to learn more about the area and properties that are currently available.Enjoy the best in Georgia living with a new home in Oconee County. Builder Jud Shiver with Scout Construction, LLC carefully crafts individual new homes in Whitlow Creek, Morningside, Coldwater Creek and Pecan Bluff, and more to come.New Homes in Oconee County are located off Highway 78, east of Atlanta, nestled between Monroe and Athens. This 'agri-suburban' community with beautiful landscapes and friendly people is the perfect place to raise a family, retire, or get away from city living."[:2000]
        item['SubImage'] = "https://scoutconstructionllc.net/wp-content/uploads/2013/09/scout-construction-blue-print-slider.jpg|https://scoutconstructionllc.net/wp-content/uploads/2013/09/scout-construction-rendering-slider.jpg|https://scoutconstructionllc.net/wp-content/uploads/2013/09/scout-construction-blue-print-slider.png"
        item['SubWebsite'] = "https://scoutconstructionllc.net/"
        item['AmenityType'] = ''
        yield item

        # next_page=True
        # while next_page==True:
        plan_links = response.xpath('//div[contains(@class,"property ")]//h2/a/@href').extract()
        for link in plan_links:
            print(link)
            head = {'Host': 'scoutconstructionllc.net','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-GB,en;q=0.5','Accept-Encoding': 'gzip, deflate, br'}
            # if link == 'https://scoutconstructionllc.net/properties/the-neyland/':
            #     print()
            res_p = requests.get(link,headers=head)#,headers=head)
            response_p = HtmlResponse(url = res_p.url,body=res_p.content)

            f = open("html/%s_%s.html" % (self.builderNumber,link.split('/')[-2]), "wb")
            f.write(response_p.body)
            f.close()

            try:
                Type = 'SingleFamily'
            except Exception as e:
                print(e)

            try:
                PlanName = response_p.xpath('//h1/text()').extract_first(default='').strip()
                print(PlanName)
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
                Description = '|'.join(response_p.xpath('//li[@class="plain"]/text()').extract())
            except Exception as e:
                print(e)

            try:
                # ---------------- bedrooms
                bed = response_p.xpath('//th[contains(text(),"Bed")]/following-sibling::td/text()').extract_first(default='').strip()
                if bed != '':
                    Bedrooms = re.findall('(\d+)',bed)[0]
                else:
                    Bedrooms = 0
                # ---------------- bathrooms
                bath_raw = response_p.xpath('//th[contains(text(),"Bath")]/following-sibling::td/text()').extract_first(default='').strip()
                if bath_raw!='':
                    tmp = re.findall(r"(\d+)", bath_raw)
                    Baths = tmp[0]
                    if len(tmp) > 1:
                        HalfBaths = 1
                    else:
                        HalfBaths = 0
                else:
                    Baths = 0
                    HalfBaths = 0
                # ------------------ sqft
                BaseSqft = 0
                # ------------------ garage
                Garage = 0
            except Exception as e:
                print(e)

            try:
                image ={'https://scoutconstructionllc.net/properties/the-neyland/':'https://scoutconstructionllc.net/wp-content/uploads/2013/09/Neyland-Elevation.png',
                        'https://scoutconstructionllc.net/properties/the-breyerton/':'https://scoutconstructionllc.net/wp-content/uploads/2013/09/Breyerton-Elevation.png',
                        'https://scoutconstructionllc.net/properties/the-mackinaw-b':'https://scoutconstructionllc.net/wp-content/uploads/2013/09/Mackinaw-B-Elevation.png',
                        'https://scoutconstructionllc.net/properties/the-harrison/':'https://scoutconstructionllc.net/wp-content/uploads/2013/09/Harrison-Plan-Elevation.jpg',
                        'https://scoutconstructionllc.net/properties/the-roswell':'https://scoutconstructionllc.net/wp-content/uploads/2013/09/Roswell-Plan-Elevation.png',
                        'https://scoutconstructionllc.net/properties/the-ardsley':'https://scoutconstructionllc.net/wp-content/uploads/2013/09/Ardsley-Elevation.jpg',
                        'https://scoutconstructionllc.net/properties/the-georgian/':'https://scoutconstructionllc.net/wp-content/uploads/2013/09/Georgian-elevation.png'
                        }
                if link not in str(image):
                    ElevationImage = '|'.join(response_p.xpath('//*[@class="caroufredsel_wrapper"]//img/@src').extract())
                    ElevationImage = '|'.join(response_p.xpath('//*[@class="preview"]//img/@src').extract())

                else:
                    ElevationImage = image.get(link)
            except Exception as e:
                print(e)

            try:
                PlanWebsite = str(response_p.url)
                # print(PlanWebsite)
            except Exception as e:
                print(e)

            # try:
                # if response_p.url =='https://scoutconstructionllc.net/properties/the-neyland/':
                #     PlanNumber =int(hashlib.md5(bytes(response_p.url+ElevationImage,"utf8")).hexdigest(), 16) % (10 ** 30)
                # PlanNumber = int(hashlib.md5(bytes(plan,"utf8")).hexdigest(), 16) % (10 ** 30)
            # except Exception as e:
            #     print(e)

            # ----------------------- Don't change anything here --------------
            try:
                # if PlanName=='The Neyland' or :
                #     unique = str(PlanName) + str(self.builderNumber)  # < -------- Changes here
                #     unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest()

                unique = str(PlanName)   # < -------- Changes here
                unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
                PlanNumber = unique_number
                item = BdxCrawlingItem_Plan()
                item['Type'] = Type
                item['PlanNumber'] = PlanNumber
                item['unique_number'] = unique_number  # < -------- Changes here
                item['SubdivisionNumber'] = self.builderNumber
                # item['PlanName'] = PlanName[:30]
                item['PlanName'] = PlanName[:30]
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

                # unique = str("Plan Unknown")
                # unique_number1 = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
                # item = BdxCrawlingItem_Plan()
                # item['unique_number'] = unique_number1
                # item['Type'] = "SingleFamily"
                # item['PlanNumber'] = "Plan Unknown"
                # item['SubdivisionNumber'] = self.builderNumber
                # item['PlanName'] = "Plan Unknown"
                # item['PlanNotAvailable'] = 1
                # item['PlanTypeName'] = "Single Family"
                # item['BasePrice'] = 0
                # item['BaseSqft'] = 0
                # item['Baths'] = 0
                # item['HalfBaths'] = 0
                # item['Bedrooms'] = 0
                # item['Garage'] = 0
                # item['Description'] = ""
                # item['ElevationImage'] = ""
                # item['PlanWebsite'] = ""
                # yield item
                #
                #
                #
                #
                # # =============== spec ===========================
                # item = BdxCrawlingItem_Spec()
                # SpecStreet1 = 'Oconee County New Construction'
                # SpecCity = 'Bogart'
                # SpecState = 'GA'
                # SpecZIP = '30622'
                # unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
                # # unique = int(hashlib.md5(bytes(response_p.url+ElevationImage,"utf8")).hexdigest(), 16) % (10 ** 30)
                # SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)
                #
                # item['SpecNumber'] = SpecNumber
                # item['PlanNumber'] = unique_number1
                # item['SpecStreet1'] = SpecStreet1
                # item['SpecCity'] = SpecCity
                # item['SpecState'] = SpecState
                # item['SpecZIP'] = SpecZIP
                # item['SpecCountry'] = 'USA'
                # item['SpecPrice'] = 0
                # item['SpecSqft'] = 0
                # item['SpecBaths'] = 4
                # item['SpecHalfBaths'] = 0
                # item['SpecBedrooms'] = 4
                # item['MasterBedLocation'] = 'Down'
                # item['SpecGarage'] = 0.0
                # item['SpecDescription'] = 'THE NEYLAND PLAN has 4 bedrooms and 4 baths, a large open kitchen with breakfast area, dining room, great room, and guest suite/office on the main floor. The other bedrooms, baths and an optional media room is on the second floor, plus this home has an optional bonus room/bath.'
                # item['SpecElevationImage'] = ''
                # item['SpecWebsite'] = 'https://scoutconstructionllc.net/properties/3825-morningside-drive-bogart-ga-30622/'
                # yield item

                # unique = int(hashlib.md5(str(response_p.url+ElevationImage,"utf8")).hexdigest(), 16) % (10 ** 30)
                # unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)  # < -------- Changes here
                item = BdxCrawlingItem_Spec()
                SpecStreet1 = '3825 Morningside Drive'
                SpecCity = 'Bogart'
                SpecState ='GA'
                SpecZIP= '30622'
                unique = SpecStreet1 + SpecCity + SpecState + SpecZIP
                # unique = int(hashlib.md5(bytes(response_p.url+ElevationImage,"utf8")).hexdigest(), 16) % (10 ** 30)
                SpecNumber = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)


                item['SpecNumber'] = SpecNumber
                item['PlanNumber'] = int(hashlib.md5(bytes('The Neyland', "utf8")).hexdigest(), 16) % (10 ** 30)
                item['SpecStreet1'] = SpecStreet1
                item['SpecCity'] = SpecCity
                item['SpecState'] = SpecState
                item['SpecZIP'] = SpecZIP
                item['SpecCountry'] = 'USA'
                item['SpecPrice'] = 0
                item['SpecSqft'] = 0
                item['SpecBaths'] = 4
                item['SpecHalfBaths'] = 0
                item['SpecBedrooms'] = 4
                item['MasterBedLocation'] = 'Down'
                item['SpecGarage'] = 0.0
                item['SpecDescription'] = 'THE NEYLAND PLAN has 4 bedrooms and 4 baths, a large open kitchen with breakfast area, dining room, great room, and guest suite/office on the main floor. The other bedrooms, baths and an optional media room is on the second floor, plus this home has an optional bonus room/bath.'
                item['SpecElevationImage'] = ''
                item['SpecWebsite'] = 'https://scoutconstructionllc.net/properties/3825-morningside-drive-bogart-ga-30622/'
                yield item

            except Exception as e:
                print(e)

            # next_page_link = response.xpath('//div[contains(@class,"pagination")]//li/a[@class="inactive"]/@href').extract_first(default='').strip()
            # if next_page_link not in links_f:
            #     links_f.append(next_page_link)
            #     if next_page_link=='':
            #         next_page=False
            #     else:
            #         res = requests.get(next_page_link)
            #         header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
            #         response = HtmlResponse(url=res.url,body=res.content,headers=header)
            #         next_page=True
            # else:
            #     next_page=False

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl scoutconstructionllc".split())
