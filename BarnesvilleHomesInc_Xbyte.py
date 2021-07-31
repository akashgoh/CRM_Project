# main_site : barnesville-homesinc.com
# Builder no: 62870

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


class arisehomes(scrapy.Spider):
    name = 'barnesville'
    builderNumber = '62870'

    def start_requests(self):
        # url = 'https://arise-homes.com'
        url = 'http://www.barnesville-homesinc.com/'
        yield scrapy.Request(url=url,callback=self.cmmunity_details)

    def cmmunity_details(self,response):
        print("---------- Not_Found_Community ---------")
        item = BdxCrawlingItem_subdivision()
        item['sub_Status'] = "Active"
        item['SubdivisionNumber'] = self.builderNumber
        item['BuilderNumber'] = self.builderNumber
        item['SubdivisionName'] = "No Sub Division"
        item['BuildOnYourLot'] = 0
        item['OutOfCommunity'] = 0
        item['Street1'] = '1400 4th Ave Northeast PO Box 340'
        item['City'] = 'Barnesville '
        item['State'] = 'MN'
        item['ZIP'] = '56514'
        item['AreaCode'] = '877'
        item['Prefix'] = "354"
        item['Suffix'] = "7531"
        item['Extension'] = ""
        item['Email'] = "bvillehomes@bvillemn.net"
        item['SubDescription'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['SubImage'] = 'http://www.barnesville-homesinc.com/bvillenewbillboard_op_640x227.jpg|http://www.barnesville-homesinc.com/Cambridge_op_640x480.jpg|http://www.barnesville-homesinc.com/carrolton_op_640x480.jpg|http://www.barnesville-homesinc.com/IMG_0155_op_640x426.jpg'
        item['SubWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['AmenityType'] = ''
        yield item


        url =['http://www.barnesville-homesinc.com/Floor-Plans-1.html','http://www.barnesville-homesinc.com/Floor-Plan-2.html','http://www.barnesville-homesinc.com/Floor-Plans-3.html','http://www.barnesville-homesinc.com/Floor-Plans-4.html','http://www.barnesville-homesinc.com/Floor-Plans-5.html','http://www.barnesville-homesinc.com/floor-plan.html','http://www.barnesville-homesinc.com/Floor-Plan-8.html']
        for i in url:
           yield scrapy.Request(url=str(i), callback=self.plan_datails, meta={'sbdn': self.builderNumber}, dont_filter=True)


    def plan_datails(self,response):
        sbdn = response.meta['sbdn']



        PlanName  ='2100 Springdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] =PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1680'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item['Description'] ='Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] ='http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] ='http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item


        PlanName = '2101 Springdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1736'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2225 Brookdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1568'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2235 Brookdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1344'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2251 Brookdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1578'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2277 Brookdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1344'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2305 Brookdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1568'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2310 Brookdale'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1680'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3631 Spectrum'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1821'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3640 Spectrum'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1886'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3676 Spectrum'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2017'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3680 Spectrum'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1940'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4810 Westport'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2016'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4820 Westport'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2575'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4830 Westport'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2856'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3570 Telmark'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1344'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3580 Telmark'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1344'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3590 Telmark'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1400'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3010 Mapleton'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1521'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] =4
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/brookdale_op_640x480.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3020 Mapleton'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2355'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/mapleton.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '3030 Mapleton'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2131'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/mapleton.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1910 Northwoods'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1040'
        item['Baths'] =2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item['Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/northwoodsjpeg.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1916 Northwoods'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1248'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/northwoodsjpeg.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2000 Lakewood'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1680'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/northwoodsjpeg.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2025 Lakewood'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1400'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/northwoodsjpeg.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2030 Lakewood'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2377'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 1
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/northwoodsjpeg.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '2060 Lakewood'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2099'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/carrolton.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4910 Carrollton'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '993'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/carrolton.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4715 Loft'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1697'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/BigLoft.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4750 Loft'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '3764'
        item['Baths'] = 4
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/BigLoft.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4760 Loft'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2542'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/loftinside.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '4765 Loft'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '2613'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/loftinside.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1610 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1586'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1611 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1680'
        item['Baths'] = 3
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1615 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1904'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1617 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1974'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1618 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1792'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1620 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1904'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1636 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1456'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '1660 Cambridge'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1344'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/Cambridgecrop.JPG'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '5010 Cavalier'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1344'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/insidecavalier.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '5020 Cavalier'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1344'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/insidecavalier.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '5035 Cavalier'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1456'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 3
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/insidecavalier.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '5040 Cavalier'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1120'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/insidecavalier.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '5045 Cavalier'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1120'
        item['Baths'] = 1
        item['HalfBaths'] = 0
        item['Bedrooms'] = 2
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/insidecavalier.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '5050 Cavalier'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1419'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/insidecavalier.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item

        PlanName = '5055 Cavalier'
        PlanNumber = int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30)
        unique = str(int(hashlib.md5(bytes(PlanName, "utf8")).hexdigest(), 16) % (10 ** 30))
        unique_number = int(hashlib.md5(bytes(unique, "utf8")).hexdigest(), 16) % (10 ** 30)

        item = BdxCrawlingItem_Plan()
        item['Type'] = 'SingleFamily'
        item['PlanName'] = PlanName
        item['PlanNumber'] = PlanNumber
        item['SubdivisionNumber'] = sbdn
        item['PlanNotAvailable'] = 0
        item['PlanTypeName'] = 'Single Family'
        item['BasePrice'] = '0'
        item['BaseSqft'] = '1317'
        item['Baths'] = 2
        item['HalfBaths'] = 0
        item['Bedrooms'] = 4
        item['Garage'] = 0
        item[
            'Description'] = 'Wisconson Homes Inc. specializes in the construction of modular homes only and prides itself in building the highest quality homes in the entire upper Midwest.  All homes are Energy Star rated.'
        item['ElevationImage'] = 'http://www.barnesville-homesinc.com/insidecavalier.jpg'
        item['PlanWebsite'] = 'http://www.barnesville-homesinc.com/'
        item['unique_number'] = unique_number
        yield item
        
        
        
        
        
        




















    # divs = response.xpath('//*[contains(text(),"bath")]//ancestor::div[contains(@id,"element")]')
        # for i in divs:
        #     print(i)
        #     main_divs = "".join(i.xpath(".//text()").getall())
        #     print("Main_divs:",main_divs)










if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute("scrapy crawl barnesville".split())


