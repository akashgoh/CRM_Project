#
# import pandas as pd
# from pandas import ExcelWriter
# import pymysql
#
# host = "localhost"
# username = "root"
# passwd = "xbyte"
# db_name = "staples_crawl"
# db_table = "executive_business_cards"
#
# try:
#    con = pymysql.connect(host,username,passwd,db_name)
#    #sql = 'select ID,URL,City1,Project_Name,Builder_Name,Location,Project_id,Rera_Id,BHK,AREA,Property_Type,Possesion,Price_Range,Launched_Date,Availability,Amenities,Specification,BreadCrumb,PostedDate,PostedBy,Last_Update_date,Images,lat,longi,Timespan,Address  from '+db_table+ ' limit 0,200000'
#    sql = 'select * from '+db_table+ ' limit 0,200000'
#    df = pd.read_sql(sql,con)
#    # writer = ExcelWriter('PythonExport.xlsx')
#    # with open("test.xlsx" ,'w' , encoding='utf-8') as xl_file:
#    writer = pd.ExcelWriter(r'Staple_Executive_Business_Cards.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
#    df.to_excel(writer)
#    writer.close()
#    print('excel Generated...')
# except Exception as e:
#    print(e)
