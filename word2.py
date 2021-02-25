# konlpy
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
# JPype1‑1.2.0‑cp36‑cp36m‑win_amd64.whl python 버전에 맞추어 다운로드
# pip install JPype1‑1.2.0‑cp36‑cp36m‑win_amd64.whl
# pip install konlpy

str = '잠겨 죽어도 좋으니 너는 물처럼 내게 밀려오랗ㅎㅎ'

from konlpy.tag import Hannanum
h = Hannanum()
# print(h.pos(str))
# print(h.nouns(str)) # 명사 추출
# print('='*30)

from konlpy.tag import Okt
o = Okt()
# print(o.pos(str))
# print(o.pos(str, norm=True)) # 문장정규화
# print(o.pos(str, norm=True, stem=True)) # 문장정규화 + 원형추출
# print(o.nouns(str)) # 명사 추출
# print('='*30)

# 네이버 뉴스 검색 API
import os
import sys
import json
import urllib.request

# client_id = "twrhEE4LU8HoKxIrMwzM"
# client_secret = "hsPSocfNRK"
# encText = urllib.parse.quote("코로나")
# url = "https://openapi.naver.com/v1/search/news.json?start=1&display=100&query=" + encText # json 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     # print(response_body.decode('utf-8'))
#     result = response_body.decode('utf-8') # json
# else:
#     print("Error Code:" + rescode)
# dic = json.loads(result)
# # print(dic)
# with open('data/news.csv', 'a', encoding='utf-8') as f:
#     for d in dic['items']:
#         desc = d['description']
#         desc = desc.replace('<b>코로나</b>', '코로나')
#         desc = desc.replace('...', ' ')
#         # print(desc)
#         f.write(desc+'\n')


# import os
# import sys
# import json
# import urllib.request
#
# client_id = "twrhEE4LU8HoKxIrMwzM"
# client_secret = "hsPSocfNRK"
# encText = urllib.parse.quote("코로나")
# url = "https://openapi.naver.com/v1/search/news.json?start={}&display=100&query=" + encText # json 결과
# for s in range(1, 501, 100):
#     request = urllib.request.Request(url.format(s))
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request)
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         # print(response_body.decode('utf-8'))
#         result = response_body.decode('utf-8') # json
#     else:
#         print("Error Code:" + rescode)
#     dic = json.loads(result)
#     with open('data/news.csv', 'a', encoding='utf-8') as f:
#         for d in dic['items']:
#             desc = d['description']
#             desc = desc.replace('<b>코로나</b>', '코로나')
#             desc = desc.replace('...', ' ')
#             # print(desc)
#             f.write(desc+'\n')
#

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
img = Image.open('img/heart.jpg')
mask = np.array(img)


# with open('data/news.csv', encoding='utf-8') as f:
#     text = f.read()
#     # print(text)
# okt = Okt()
# lines = text.split('\n')
# # print(len(lines))
# worddic = {}
# for line in lines:
#     mal = okt.pos(line, norm=True, stem=True)
#     for m in mal:
#         if len(m[0]) > 1:
#             if m[1] =='Noun' or m[1] == 'Verb' or m[1] == 'Adjective':
#                 if not(m[0] in worddic):
#                     worddic[m[0]] = 0
#                 worddic[m[0]] = worddic[m[0]] + 1
# # print(worddic)
# # print(sorted(worddic.items(), key=lambda x: x[1], reverse=True))
# dic = dict(sorted(worddic.items(), key=lambda x: x[1], reverse=True)[:100])
# print(dic)
# wc = WordCloud(font_path='malgun.ttf', mask=mask, background_color='white').generate_from_frequencies(dic)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
img = Image.open('img/images.png')
mask = np.array(img)
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 1:
            mask[i][j] = 255

with open('data/news.csv', encoding='utf-8') as f:
    text = f.read()
    # print(text)
okt = Okt()
lines = text.split('\n')
# print(len(lines))
worddic = {}
stopwords = ['있다', '위해', '최근']
for line in lines:
    mal = okt.pos(line, norm=True, stem=True)
    for m in mal:
        if len(m[0]) > 1 and m[1] == 'Noun' and m[0] not in stopwords:
            # if m[1] =='Noun' or m[1] == 'Verb' or m[1] == 'Adjective':
                if not(m[0] in worddic):
                    worddic[m[0]] = 0
                worddic[m[0]] = worddic[m[0]] + 1
# print(worddic)
# print(sorted(worddic.items(), key=lambda x: x[1], reverse=True))
dic = dict(sorted(worddic.items(), key=lambda x: x[1], reverse=True)[:100])
print(dic)
wc = WordCloud(font_path='malgun.ttf', mask=mask, background_color='white').generate_from_frequencies(dic)
plt.imshow(wc)
plt.axis('off')
plt.show()



# a = [3, 1, 2]
# print(sorted(a))
# print(sorted(a, reverse=True))
# b = {'one': 100, 'four': 4, 'three': 33}
# print(sorted(b))
# for i in b:
#     print(i)
# for i in b.items():
#     print(i)
# print(sorted(b.items()))
# print(sorted(b.items(), key=lambda x: x[1]))