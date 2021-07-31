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
    name = 'Baldwin_Builders_LLC'
    builderNumber = '62860'

    def start_requests(self):
        url = 'http://baldwinbuildersllc.com/' #<<----- Community link
        yield scrapy.Request(url=url,callback=self.comm_details)

    def comm_details(self,response):
        try:
            print("---------- Not_Found_Community ---------")
            item = BdxCrawlingItem_subdivision()
            item['sub_Status'] = "Active"
            item['SubdivisionNumber'] = self.builderNumber
            item['BuilderNumber'] = self.builderNumber
            item['SubdivisionName'] = "No Sub Division"
            item['BuildOnYourLot'] = 0
            item['OutOfCommunity'] = 0
            item['Street1'] = '172A Industrial Dr'
            item['City'] = 'Clarksville'
            item['State'] = 'TN'
            item['ZIP'] = '37040'
            item['AreaCode'] = '931'
            item['Prefix'] = "378"
            item['Suffix'] = "0500"
            item['Extension'] = ""
            item['Email'] = "info@baldwinbuildersllc.com"
            item['SubDescription'] = 'The majority of our projects consist of custom homes for private clients. We work directly with clients from lot identification through move in. We pride ourselves on walking you through the process from beginning to completion and making it an enjoyable experience for everyone involved.'
            item['SubImage'] = 'http://baldwinbuildersllc.com/wp-content/uploads/2017/11/ClarksvilleCourt2-300x225.jpg|http://baldwinbuildersllc.com/wp-content/uploads/2017/11/pexels-photo-58457-300x200.jpeg'
            item['SubWebsite'] = 'http://baldwinbuildersllc.com/'
            item['AmenityType'] = ''
            yield item

            main_plan_url = 'http://baldwinbuildersllc.com/floor-plans/'
            response88 = requests.request("POST", main_plan_url)
            res33 = HtmlResponse(url=main_plan_url, body=response88.content, encoding='utf-8')
            sub_plan_url = res33.xpath('//*[@class="so-panel widget widget_sow-editor panel-first-child panel-last-child"]/div/div/h3/a[1]/@href').extract()
            for i in sub_plan_url:
                url = i
                yield scrapy.Request(url=url,callback=self.plan_details,meta={"SubdivisionNumber":item['SubdivisionNumber']})
        except Exception as e:
            print(e)

    def plan_details(self, response):
        SubdivisionNumber = response.meta['SubdivisionNumber']

        try:
            plan_name = response.xpath('//h3/text()').extract_first(default='')
        except Exception as e:
            plan_name = ''
            print(e)

        try:
            BasePrise = '0'
        except Exception as e:
            BasePrise = '0'
            print(e)
        try:
            BaseSqft = response.xpath('//*[contains(text(),"Square Footage Total:")]/../text()').extract_first(default='')
            if BaseSqft == '':
                BaseSqft  = response.xpath('//*[@class="so-panel widget widget_sow-features panel-first-child"]/div/div/div[1]/div[2]/h5/text()').extract_first(default='').replace('sq/ft*','').replace(',','')
        except Exception as e:
            BaseSqft = 0
            # BaseSqft = 0
            print(e)
        try:
            Baths = response.xpath('//*[@class="so-panel widget widget_sow-features panel-first-child"]/div/div/div[3]/div[2]/h5/text()').extract_first(default='')
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
            Badroom = response.xpath('//*[@class="so-panel widget widget_sow-features panel-first-child"]/div/div/div[2]/div[2]/h5/text()').extract_first(default='')
            if '-' in Badroom:
                Badroom = Badroom.split('-')[-1]
            Badroom = int(''.join(re.findall(r"(\d+)", Badroom)))
        except Exception as e:
            Badroom = 0
            print(e)

        try:
            if response.url =='http://baldwinbuildersllc.com/floor-plans/WADDELL/':
                description = 'A timeless combination of clapboard siding and brick make this home a welcomed addition to any neighborhood. Its unique foyer – with a corner coat closet, decorative columns, and art niche, make this design interesting from the start. A vaulted ceiling canopies the kitchen, dining room and family room enhancing the spaciousness of all three areas'
            elif response.url == 'http://baldwinbuildersllc.com/floor-plans/ALDRIDGE/':
                description = 'This plan combines a traditional, stately interior with an updated floor plan to create a house that will please the entire family. The heart of the plan is surely the wide-open living space consisting of the vaulted family room, breakfast area, and gourmet kitchen. Highlights here are a full-length fireplace, a French door to the rear yard, and an island cook top. The master suite has a tray ceiling and a vaulted master bath with a garden tub and walk-in closet. The family sleeping area on the upper level gives the option of two bedrooms and a loft overlooking the family room or three bedrooms.'
            elif response.url== 'http://baldwinbuildersllc.com/floor-plans/SACRAMENTO/':
                description = 'The beauty of this home lies in its simple yet efficient design and all its extras. Decorative touches include plant shelves, arched openings, and vaulted ceilings. The well-equipped kitchen enjoys a pass-through to the great room, very hand for social get-togethers. It also boasts a walk-in pantry. A tray ceiling, walk-in closet, resplendent bath with a separate glass shower and oval tub add splendor to the master suite. The two secondary bedrooms are secluded on the other side of the plan.'
            elif response.url == 'http://baldwinbuildersllc.com/floor-plans/SHERMAN-OAKS/':
                description = 'Tapered architectural columns, eave brackets, and cedar shake give this split-foyer design a fresh and innovative appeal. An ideal entry-level home, this home was designed to provide a spacious feel and functional elements in a moderate and affordable square footage'
            elif response.url =='http://baldwinbuildersllc.com/floor-plans/COURTRIDGE/':
                description ='This four-bedroom traditional home includes all the amenities a family could want in 2500 square feet. The appealing exterior features gorgeous Palladian windows and brick, along with a front-entry garage and metal-topped porch. Inside, the two-story foyer greets visitors in high style and the two-story ceiling continues into the great room'
            elif response.url =='http://baldwinbuildersllc.com/floor-plans/FOXCROFTE/':
                description = 'This home is quaint and charming with its gabled roofline and covered front porch. Vaulted ceilings give a roomy feeling inside in the foyer and great room. The staircase to the upper floor is tucked away near the back of the home, adding to this design’s spaciousness'
            elif response.url =='http://baldwinbuildersllc.com/floor-plans/SUMMERGROVE/':
                description ='A brick water table and clapboard siding are the materials of choice for this traditional design. The boxed bay window with its copper roofing and the double shed dormer complete the exterior'
            elif response.url =='http://baldwinbuildersllc.com/floor-plans/goldshire/':
                description = 'Gorgeous 4 bedroom 3 bath open concept home that features hardwood flooring and tile, granite countertops, tile backsplash, stainless steel appliances, covered deck, bonus room, formal dining room, storage building, mature landscaping.'
            elif response.url =='http://baldwinbuildersllc.com/floor-plans/brewster/':
                description ='Classic red brick and white stucco accents combine to make a stunning façade on the Brewster. Alternate design options give the homeowner plenty of choice on how they want their finished product to be'
            elif response.url =='http://baldwinbuildersllc.com/moultrie/':
                description ='Moultrie House Plan - Gabled rooflines, shutters and siding-all elements of a fine facade, and the floor plan inside equals this quality. The foyer opens directly into the vaulted great room, where a fireplace waits to warm cool winter evenings'
            # elif response.url == '':
            #     description =''
        except Exception as e:
            description = ''
            print(e)
        try:
            imges = '|'.join(response.xpath('//*[@class="so-panel widget widget_sow-slider panel-first-child"]/div/div/ul/li/img/@src|//*[@class="so-panel widget widget_sow-image panel-last-child"]/div/div/img/@src|//*[@id="gallery-1"]/dl/dt/a/img/@src').extract())
        except Exception as e:
            imges= ''
            print(e)


        unique = str(int(hashlib.md5(bytes(response.url + plan_name, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = plan_name
        item['PlanNumber'] = int(hashlib.md5(bytes(plan_name, "utf8")).hexdigest(), 16) % (10 ** 30)
        item['SubdivisionNumber'] = SubdivisionNumber
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = BasePrise
        item['BaseSqft'] = BaseSqft
        item['Baths'] = Baths
        item['HalfBaths'] = HalfBaths
        item['Bedrooms'] = Badroom
        item['Garage'] = 0
        item['Description'] = description
        item['ElevationImage'] = imges
        item['PlanWebsite'] = response.url
        item['unique_number'] = unique_number
        yield item

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl Baldwin_Builders_LLC".split())


