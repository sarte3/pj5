from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

import json
import os
import sys
import urllib.request
client_id = "twrhEE4LU8HoKxIrMwzM"
client_secret = "hsPSocfNRK"
encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/book.json?display=100&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

dic = json.loads(result)
# print(dic)


# 1) 네이버 개발자 센터에서 파이썬 책을 검색하여
# 책 제목, 출판사, 가격, isbn열을 데이터프레임 df로 생성하세요.
items = dic['items']
df=pd.DataFrame(items)
df = df[['title', 'publisher', 'price', 'isbn']]
print(df)

# 2) 출판사별 가격의 평균을 출력하세요
df['price']=pd.to_numeric(df['price'])
g1 = df.groupby('publisher')['price'].mean()

print(g1)