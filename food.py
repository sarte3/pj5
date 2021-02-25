from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='D2Coding-Ver1.3.2-20180524-all.ttc').get_name()
rc('font', family=fontname)

import json

# data = {'k1':['a', 'b', 'b', 'c', 'c'],
#     'k2':['v', 'w', 'w', 'x', 'y'],
#     'data': [1, 2, 3, 4, 5]}

# df = pd.DataFrame(data)
# print(df)

# # # 중복데이터 확인
# # print(df.duplicated('k1'))
# # print(df.duplicated(['k1', 'k2']))

# # 중복데이터 제거
# # print(df.drop_duplicates(['k1']))
# # print(df.drop_duplicates(['k1'], keep='last'))


# data = {'k1':['a', 'b', 'b', 'c', 'c'],
#     'k2':['v', 'w', 'w', 'x', 'y'],
#     'data': [1, 2, 2, 2, 2]}

# df = pd.DataFrame(data)
# print(df)

#  # 완벽하게 동일한 것만 삭제
# print(df.drop_duplicates())

food = json.load(open('data\\food.json'))
# print(food)
# print(type(food))
# print(len(food))
# # print(food[0])
# print(food[0].keys())
# # print(food[0]['nutrients'])
# n1 = pd.DataFrame(food[0]['nutrients'])
# print(n1)

info = pd.DataFrame(food, columns=['id', 'group', 'description'])
# print(info)
# print(info.columns)
temp = []

for dic in food:
    nut = pd.DataFrame(dic['nutrients'])
    nut['id'] = dic['id']
    # print(nut)
    temp.append(nut)

data = pd.concat(temp, ignore_index=True)
# print(data)
data = data.drop_duplicates()
# print(data.shape)
# 컬럼 이름 변경 
# 1) 전체 수정
# info.columns = ['foodid', 'foodgroup', 'foodname']
# print(info)
# 2) 부분 수정
info = info.rename(columns={'description': 'foodname', 'group': 'foodgroup'})
# print(info)
df = info.merge(data, on='id')
# df.info()
print(df.groupby(['foodgroup', 'group'])['value'].min())