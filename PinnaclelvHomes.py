# -*- coding: utf-8 -*-
import hashlib
import re
import scrapy
from scrapy.utils.response import open_in_browser

from BDX_Crawling.items import BdxCrawlingItem_subdivision, BdxCrawlingItem_Plan, BdxCrawlingItem_Spec


class blueribbonokSpider(scrapy.Spider):
    name = 'pinnaclelv'
    allowed_domains = ['pinnaclelv.com']
    start_urls = ['https://www.pinnaclelv.com/']
    builderNumber = "210244839610620539019063276387"


    def parse(self, response):

        links = response.xpath('//li[@id="menu-item-1286"]//li/a/@href').extract()
        for l in links:
            yield scrapy.Request(l,self.Communities)


    # ----------------------------------------------------------------------------- If communities found ------------------------------------------------------------------------------------------------ #
    #                                                        # ------------------- Creating Communities ---------------------- #
    def Communities(self,response):
        subdivisonName = response.xpath('//h1[@class="entry-title"]/text()').get() or response.xpath('//div[@class="textwidget custom-html-widget"]//p/strong/text()').get()
        subdivisonNumber = int(hashlib.md5(bytes(subdivisonName,"utf8")).hexdigest(), 16) % (10 ** 30)
        f = open("html/%s.html" % subdivisonNumber, "wb")
        f.write(response.body)
        f.close()

        try:
            if response.url =='https://pinnaclelv.com/communities/park-meadows':
                Street1 = '5725 N. Conquistador Street'
                City = 'Las Vegas'
                State = 'NV'
                ZIP = '89149'
                AreaCode = '702'
                Prefix = '341'
                Suffix = '1588'
                Email = ''
                SubDescription = 'Park Meadows offers three floor plans from 3,638 SF to 4,022 SF with Mid-Century Modern, Modern Prairie and Desert Contemporary architectural styles in an ungated cul-de-sac in Northwest Las Vegas'
                # SubImage = "https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_A-CROP-669x272.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Prism-3685_A-CROP-669x272.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Element-4022_A-CROP-669x272.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/Casita-B-669x272.jpg|https://pinnaclelv.com/wp-content/uploads/2019/01/RV-B-cropped.jpg"

            tmp = response.xpath('//*[contains(text(),"Sales Center Location:")]/../../p[6]/text()').extract()
            if tmp == []:
                tmp = response.xpath('//*[contains(text(),"Sales Office Location:")]/text()').extract()
            if tmp !=[]:
                Street1 = ', '.join(tmp[1:-1])
                Street1 = re.sub('\n','',Street1).strip()
                City = tmp[-1].split(',')[0].strip()
                SZ = tmp[-1].split(',')[1]
                State = re.findall('([A-Z]{2,2})',SZ)[0].strip()
                ZIP = re.findall('(\d+)',SZ)[0].strip()
                tmpCont = response.xpath('//p[contains(text(),"Phone")]/text()').get()
                if response.url=='https://pinnaclelv.com/communities/ascent':
                    tmpCont = '702-341-1588'

                if tmpCont:
                    Contact = tmpCont.replace('Phone:','').strip()
                    Contact = Contact.split('-')
                    AreaCode = Contact[0]
                    Prefix = Contact[1]
                    Suffix = Contact[2]
                else:
                    AreaCode = ''
                    Prefix = ''
                    Suffix = ''
                Email = response.xpath('//p[contains(text(),"Email")]/a/text()').extract()
                if Email:
                    Email = Email[0]
                else:
                    Email = ''
                SubDescription = ''.join(response.xpath('//div[@class="sidebars"]/p/text()|//*[@class="textwidget"]/p/text()').extract())
        except Exception as e:
            print('Communities',e,response.url)

        links = []
        try:
            if "Desert Trace" in subdivisonName:
                links.append('https://www.pinnaclelv.com/4023-desert-trace-ct')

            if "Elk" in subdivisonName:
                links.append('https://www.pinnaclelv.com/8478-wolf-mountain-ct')
        except Exception as e:
            print("Comm",e)
        try:
            SubImage = '|'.join(response.xpath('//ul[@class="slides"]/li//img/@src').extract())
        except Exception as e:
            SubImage = ''
            print(e)

        item2 = BdxCrawlingItem_subdivision()
        item2['sub_Status'] = "Active"
        item2['SubdivisionName'] = subdivisonName
        item2['SubdivisionNumber'] = subdivisonNumber
        item2['BuilderNumber'] = self.builderNumber
        item2['BuildOnYourLot'] = 0
        item2['OutOfCommunity'] = 1
        item2['Street1'] = Street1
        item2['City'] = City
        item2['State'] = State
        item2['ZIP'] = ZIP
        item2['AreaCode'] = AreaCode
        item2['Prefix'] = Prefix
        item2['Suffix'] = Suffix
        item2['Extension'] = ""
        item2['Email'] = Email
        item2['SubDescription'] = SubDescription
        item2['SubImage'] = SubImage
        item2['SubWebsite'] = response.url
        item2['AmenityType'] = ''
        yield item2

        links.extend(response.xpath('//h2[@class="blog-shortcode-post-title entry-title"]/a/@href|//h2[@class="blog-shortcode-post-title entry-title fusion-responsive-typography-calculated"]/a/@href').extract())
        print(links)
        for i in links:
            url1= i
            yield scrapy.Request(url1,self.Plan,meta={'SN':subdivisonNumber})

    def Plan(self,response):
        SubdivisionNumber = response.meta['SN']

        PlanNumber = int(hashlib.md5(bytes(response.url,"utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(PlanNumber) + str(SubdivisionNumber)  # < -------- Changes here
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        if response.url =='https://pinnaclelv.com/ascend':
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'Ascend'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 400
            item['BaseSqft'] = 2346
            item['Baths'] = 2
            item['HalfBaths'] = 1
            item['Bedrooms'] =3
            item['Garage'] = 2
            item['Description'] = "Ascent offers three single-story floor plans from 2,346 SF to 2,828 SF within a 20-lot non-gated community located at the northwest corner of Pioneer Way and Hickam Street in Northwest Las Vegas."
            item['ElevationImage'] ='https://pinnaclelv.com/wp-content/uploads/2020/07/2346A-cropped-300x140.jpg|https://pinnaclelv.com/wp-content/uploads/2020/07/2346C-cropped-300x132.jpg|https://pinnaclelv.com/wp-content/uploads/2020/07/2346C-cropped-300x132.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/summit":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'Summit'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 500
            item['BaseSqft'] = 2679
            item['Baths'] = 2
            item['HalfBaths'] = 1
            item['Bedrooms'] = 1
            item['Garage'] = 2
            item['Description'] = "Ascent offers three single-story floor plans from 2,346 SF to 2,828 SF within a 20-lot non-gated community located at the northwest corner of Pioneer Way and Hickam Street in Northwest Las Vegas"
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/2020/07/2346A-cropped-300x140.jpg|https://pinnaclelv.com/wp-content/uploads/2020/07/2346C-cropped-300x132.jpg|https://pinnaclelv.com/wp-content/uploads/2020/07/2346C-cropped-300x132.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/peak":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'Summit'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 500
            item['BaseSqft'] = 2828
            item['Baths'] = 2
            item['HalfBaths'] = 1
            item['Bedrooms'] = 3
            item['Garage'] = 3
            item['Description'] = "Ascent offers three single-story floor plans from 2,346 SF to 2,828 SF within a 20-lot non-gated community located at the northwest corner of Pioneer Way and Hickam Street in Northwest Las Vegas"
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/2020/07/2346A-cropped-300x140.jpg|https://pinnaclelv.com/wp-content/uploads/2020/07/2346C-cropped-300x132.jpg|https://pinnaclelv.com/wp-content/uploads/2020/07/2346C-cropped-300x132.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/axis-at-calypso":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'Axis at Calypso'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 800
            item['BaseSqft'] = 3638
            item['Baths'] = 2
            item['HalfBaths'] = 1
            item['Bedrooms'] = 3
            item['Garage'] = 3
            item['Description'] = ""
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/Axis-3638B2-300x102.jpg|https://pinnaclelv.com/wp-content/uploads/2021/01/Axis-3638A2-300x122.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/prism-2":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'prism at Calypso'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 800
            item['BaseSqft'] = 3685
            item['Baths'] = 3
            item['HalfBaths'] = 1
            item['Bedrooms'] = 4
            item['Garage'] = 3
            item['Description'] = ""
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/Prism-3685A2-300x99.jpg|https://pinnaclelv.com/wp-content/uploads/Prism-3685B2-300x101.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/elk-ridge-plan-4090":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'Apogee at Calypso'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 800
            item['BaseSqft'] = 4090
            item['Baths'] = 3
            item['HalfBaths'] = 1
            item['Bedrooms'] = 4
            item['Garage'] = 3
            item['Description'] = ""
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/2021/01/Apogee-4090A-scaled.jpg|https://pinnaclelv.com/wp-content/uploads/2019/10/Apogee-4090B-FNL-300x194.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/aspect-at-calypso":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'aspect-at-calypso'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 800
            item['BaseSqft'] = 4190
            item['Baths'] = 3
            item['HalfBaths'] = 1
            item['Bedrooms'] = 4
            item['Garage'] = 5
            item['Description'] = ""
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/2019/11/Aspect-4190A-FNL-scaled.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/contour-at-altitude":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'contour-at-altitude'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 800
            item['BaseSqft'] = 4260
            item['Baths'] = 3
            item['HalfBaths'] = 1
            item['Bedrooms'] = 4
            item['Garage'] = 3
            item['Description'] = ""
            item['ElevationImage'] = 'https://www.pinnaclelv.com/wp-content/uploads/2019/10/Contour-4260B-FNL.jpg|https://www.pinnaclelv.com/wp-content/uploads/2019/10/Contour-4260A-FNL.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/axis":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'AXIS'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 0
            item['BaseSqft'] = 3638
            item['Baths'] = 2
            item['HalfBaths'] = 1
            item['Bedrooms'] = 3
            item['Garage'] = 3.0
            item['Description'] = ""
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_A-CROP-300x132.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_B-CROP-300x134.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_B-CROP-300x134.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/prism":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'PRISM'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 0
            item['BaseSqft'] = 3685
            item['Baths'] = 3
            item['HalfBaths'] = 1
            item['Bedrooms'] = 4
            item['Garage'] = 3.0
            item['Description'] = ""
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_A-CROP-300x132.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_B-CROP-300x134.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_B-CROP-300x134.jpg'
            item['PlanWebsite'] = response.url
            yield item
        if response.url =="https://pinnaclelv.com/element":
            item = BdxCrawlingItem_Plan()
            item['Type'] = 'SingleFamily'
            item['PlanNumber'] = int(hashlib.md5(bytes(response.url, "utf8")).hexdigest(), 16) % (10 ** 30)
            item['unique_number'] = unique_number
            item['SubdivisionNumber'] = SubdivisionNumber
            item['PlanName'] = 'element'
            item['PlanNotAvailable'] = 0
            item['PlanTypeName'] = 'Single Family'
            item['BasePrice'] = 0
            item['BaseSqft'] = 4022
            item['Baths'] = 3
            item['HalfBaths'] = 1
            item['Bedrooms'] = 4
            item['Garage'] = 3.0
            item['Description'] = ""
            item['ElevationImage'] = 'https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_A-CROP-300x132.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_B-CROP-300x134.jpg|https://pinnaclelv.com/wp-content/uploads/2019/11/ElkRidge-Axis-3638_B-CROP-300x134.jpg'
            item['PlanWebsite'] = response.url
            yield item


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl pinnaclelv".split())