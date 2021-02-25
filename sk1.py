# from sklearn.svm import LinearSVC
# from sklearn.metrics import accuracy_score
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC

# trainx = [[0, 0], [0, 1], [1, 0], [1, 1]]
# trainy = [0, 0, 0, 1]
#
# # 모델 생성
# model = LinearSVC()
#
# # 학습
# model.fit(trainx, trainy)
#
# # 예측
# testx = [[0, 0], [0, 1], [1, 0], [1, 1]]
# pred = model.predict(testx)
#
# # 평가
# print('정확도 =', accuracy_score([0, 0, 0, 1], pred))

# data = pd.read_csv('data/iris.csv')
# print(data)
#
# # 데이터와 정답으로 분리
# x = data.loc[:, ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']]
# y = data.loc[:, 'Species']
# print(y)
# print(x)

# 70% 데이터로 훈련, 30% 데이터로 검증
# trainx, testx, trainy, testy = train_test_split(x, y, train_size=0.7, shuffle=True)
#
# # 모델 생성
# model = SVC()
#
# # 훈련
# model.fit(trainx, trainy)
#
# # 평가
# pred = model.predict(testx)
# print('정확도 =', accuracy_score(testy, pred))

from sklearn import linear_model

# x = np.random.rand(100, 1)
# print(x)
#
# # -2 <= x <= 2
# x = x * 4 - 2
# y = 3 * x - 2+np.random.randn(100, 1)
# # plt.plot(x, y, 'o')
# # plt.show()
#
# # 모델 생성
# model = linear_model.LinearRegression()
#
# # 훈련
# model.fit(x, y)
# print('기울기 =', model.coef_)
# print('절편 =', model.intercept_)
#
# # 예측
# pred = model.predict(x)
# plt.plot(x, y, 'o')
# plt.plot(x, pred)
# plt.show()

# data = pd.read_csv('data/cars.csv')
# # print(data)
#
# # print(list(data['speed']))
# x = []
# y = []
# for i in range(data.shape[0]):
#     print(list(data['speed'])[i])
#     x.append([list(data['speed'])[i]])
#     y.append([list(data['dist'])[i]])
#
# print(x)
# print(y)
# model = linear_model.LinearRegression()
# model.fit(x, y)
# print('기울기 =', model.coef_)
# print('절편 =', model.intercept_)
#
# plt.plot(x, y, 'o') # 실제데이터
# plt.plot(x, model.predict(x)) # 모델
# plt.show()

# print(ord('a'))
# print(ord('A'))
# print(chr(65))
# print(sum([1, 2, 3, 4, 5]))
# a = [1, 2, 3, 4, 5]
# total = sum(a)
# print(list(map(lambda i:i/total, a)))
# map(함수, 반복가능 객체)

import glob
import os
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# def make_data(file):
#     with open(file, encoding='utf-8') as f:
#         text = f.read()
#         text = text.lower()
#         # print(text)
#         cnt = [0 for i in range(26)]
#         # print(cnt)
#         # str = 'alice!^^ css3'
#         for c in text:
#             n = ord(c)
#             if ord('a')<=n<=ord('z'):
#                 cnt[n-ord('a')] = cnt[n-ord('a')]+1
#         # print(cnt)
#         total = sum(cnt)
#         data = list(map(lambda i: i / total, cnt))
#         # print(data)
#         return data
#
#
# def load_files(path):
#     label = []
#     data = []
#     # print(glob.glob(path))
#     filelist = glob.glob(path)
#     for file in filelist:
#         # print(os.path.dirname(file))
#         # print(os.path.basename(file))  # 파일명
#         # print(os.path.basename(file)[:2])
#         d = make_data(file)
#         label.append(os.path.basename(file)[:2])  # 정답 추출
#         data.append(d)
#     # print(label)
#     # print(data)
#     return data, label
#
#
# trainx, trainy = load_files('data/lang/train/*.txt')
# # print(trainx)
# # print(trainy)
# testx, testy = load_files('data/lang/test/*.txt')
# model = SVC()
# model.fit(trainx, trainy)
# pred = model.predict(testx)
#
# print('정확도=', accuracy_score(testy, pred))
#

import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data/water.csv')
x = []
y = []
old = list(data['old'])
new = list(data['new'])
astime = list(data['as_time'])
for i in range(data.shape[0]):
    x.append([old[i], new[i]])
    y.append([astime[i]])
# print(x)
# print(y)
model = LinearRegression()
model.fit(x, y)
print(model.coef_)
print(model.intercept_)

print('예측 as시간 :', model.predict([[70000, 230000]]))

