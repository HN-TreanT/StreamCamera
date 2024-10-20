from django.db import connection
from rest_framework import pagination
from datetime import date
# create funtion get dict object in database
def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def getDictFromQuery(query_String:str,param:list,page:str=None,size:str=None):  
    with connection.cursor() as cursor:
        if page is not None:
            query_String=query_String+" LIMIT %s OFFSET %s"
            if size is not None:
                param =param + [int(size), (int(page)-1)*int(size)]
            else:
                param =param + [pagination.PageNumberPagination.page_size, int(page)*pagination.PageNumberPagination.page_size]           
        cursor.execute(query_String,param)
        obj = dictfetchall(cursor)
    return obj
   

def getNextCode(nameTable:str,nameCode:str): 
    today = date.today()
    today=today.strftime("%Y%m%d")

    with connection.cursor() as cursor:
        query_string = f"SELECT {nameCode} " \
                        f"FROM {nameTable} " \
                        f"WHERE SUBSTRING({nameCode},1,8)= '{today}' " \
                        f"ORDER BY {nameCode} DESC " \
                        f"LIMIT 1 "                  
        cursor.execute(query_string)
        obj = dictfetchall(cursor)
    if obj is  None or len(obj)==0:
        return today+'0'*11+'1'
    previousCode=obj[0]["CODE"]
    print("previousCode:",previousCode)
    currentSTT=format(int(previousCode[8:])+1,'012d')
    currendCode=today+currentSTT
    print("currendCode",currendCode)
    return currendCode
   