# import pandas as pd
# colors = [['red', 'green', 'blue', 'orange'], ['pink', 'ivory', 'purple', 'tomato']]
# data = pd.DataFrame(colors, columns = ['a', 'b', 'c', 'd'])
# print(data)
# for d in data:
#     print(d) #열이름
# for k, v in data.iteritems():
#     print('k = ', k) #열이름
#     print('v = \n', v) #행번호, 값
# for k,v in data.iterrows():
#     print('k = ', k)   # 행인덱스
#     print('v = \n', v)  # 값
# for t in data.itertuples():
#     print(t)   #행인덱스와 값이 튜플로
#     print(t[0],'***')  #행인덱스

# import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# from sklearn.ensemble import RandomForestClassifier
# mr = pd.read_csv('data\\mushroom.csv', header=None)
# # print(mr)
# data = []
# label = []
# for k, v in mr.iterrows():
#     # print('k = ', k) #행인덱스
#     # print('v = \n', v)
#     label.append(v[0])
#     temp = []
#     for i in v.iloc[1:]:
#         temp.append(ord(i))
#     data.append(temp)
# # print(label)
# # print(data)

# # 75%학습, 25%검증
# trainx, testx, trainy, testy = train_test_split(data, label, train_size = 0.75)
# model = RandomForestClassifier()
# model.fit(trainx, trainy)
# pred = model.predict(testx)
# print('정확도 = ', accuracy_score(pred, testy))

# 교차검증
# from sklearn.svm import SVC
# def split_x_y(data):
#     x = []
#     y = []
#     for d in data:
#         x.append(d[:4])
#         y.append(d[4])
#     return x, y

# data = open('data\\iris.csv').read().split()
# # print(data)
# del data[0]
# # print(data)
# csv = []
# for line in data:
#     temp = []
#     line = line.split(',')
#     # print(line) # ['5.1', '3.5', '1.4', '0.2', 'setosa']
#     temp.append(float(line[0]))
#     temp.append(float(line[1]))
#     temp.append(float(line[2]))
#     temp.append(float(line[3]))
#     temp.append(line[4])
#     # print(temp)
#     csv.append(temp)
# print(csv)

# # 데이터 분할
# k = 5
# # [[], [], [], [], []]
# csvk = [[] for i in range(k)]
# # print(csvk)
# for i in range(len(csv)): # i = 0, 1, ... 149
#     csvk[i % k].append(csv[i])
# # print(csvk)
# # print(len(csvk)) #5
# # print(len(csvk[0])) #30
# scores = []
# for testdata in csvk:
#     print('검증용 데이터 = ', testdata) # 2차원
#     traindata = []
#     for i in csvk:
#         if i != testdata:
#             traindata = traindata + i
#     print('훈련용 데이터 = ', traindata) # 2차원
#     testx, testy = split_x_y(testdata)
#     trainx, trainy = split_x_y(traindata)
#     # print('testx = ', testx)
#     # print('testy = ', testy)

#     # 모델생성
#     model = SVC()
#     model.fit(trainx, trainy)
#     pred = model.predict(testx)
#     # print('정확도 = ', accuracy_score(pred, testy))
#     scores.append(accuracy_score(pred, testy))
# print('정확도 = ', scores)
# print('전체정확도 = ', sum(scores) / len(scores))

from wordcloud import WordCloud
import matplotlib.pyplot as plt
# data = open('data\\alice.txt').read()
# print(data)
# # wc = WordCloud().generate(data)
# wc = WordCloud(background_color='white', max_words=2000).generate(data)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
# 마스크 적용
from PIL import Image
from wordcloud import STOPWORDS 
import numpy as np
print(STOPWORDS) #빼야될 글자
sw = STOPWORDS
print(len(sw))
sw.add('said')
print(len(sw))
img = Image.open('img\\one.png')
mask = np.array(img)
print(mask)
data = open('data\\alice.txt').read().lower()
wc = WordCloud(mask = mask, stopwords = sw, background_color = 'ivory').generate(data)
plt.imshow(wc)
plt.axis('off')
plt.show()