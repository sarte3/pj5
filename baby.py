import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='D2Coding-Ver1.3.2-20180524-all.ttc').get_name()
rc('font', family=fontname)

# d1880 = pd.read_csv('data/baby/yob1880.txt', names=['name', 'sex', 'births'])
# print(d1880)

temp = []
for year in range(1880, 2011):
    filename = 'data/baby/yob'+str(year)+'.txt'
    # print(filename)
    d1 = pd.read_csv(filename, names=['name', 'sex', 'births'])
    # print(d1)
    d1['year'] = year
    temp.append(d1)

data=pd.concat(temp, ignore_index=True)
# print(data)

# 연도와 성별에 따른 신생아 수
# s1 = data.groupby(['year', 'sex'])['births'].sum()
# print(s1)

# 과제
# 1. 연도, 성별에 따른 출생아 수를 피벗으로 출력
p1 = data.pivot_table(index='year', columns='sex', values='births', aggfunc=sum)
# p1 = pd.pivot_table(data, index='year', columns='sex', values='births', aggfunc=sum)
# print(p1)

# # 2. 1의 결과를 그래프로
# plt.plot(p1)
# # plt.legend(p1.columns)
# plt.legend(['여자', '남자'])
# plt.title('연도, 성별에 따른 출생아 수')
# plt.show()

# 3. 이름이 연도별, 성별별 출생수에서 차지하는 비율
def calrate(x):
    # print(x['births']/x['births'].sum())
    x['rate'] = x['births']/x['births'].sum()
    return x

def gettop2(x):
    return x.sort_values(by='births', ascending=False)[:2]

def gettop(x):
    return x.sort_values(by='births', ascending=False)[:1000]


g1 = data.groupby(['year', 'sex'])
data = g1.apply(calrate)
# print(data)

# 연도별 성별별 빈도수가 가장 높은 이름 2개 추출
top2 = g1.apply(gettop2)
# print(top2.head(10))

# 연도별 성별별 빈도수가 가장 높은 이름 1000개 추출
top1000 = g1.apply(gettop)
# print(top1000)

# # 4. 연도와 이름에 대한 전체 출생수를 피벗으로 출력 
# # p3 = pd.pivot_table(data, index='year', columns='name', values='births', aggfunc=sum)
# # print(p3)
# p2 = top1000.pivot_table(index='year', columns='name', values='births', aggfunc=sum)
# print(p2)
top1000 = top1000.drop(['year', 'sex'], axis=1)
# # top1000 = top1000.drop('year', axis=1)
# # top1000 = top1000.drop('sex', axis=1)

# print(top1000)
top1000 = top1000.reset_index()
top1000 = top1000.drop('level_2', axis=1)
# # print(top1000)
p2 = top1000.pivot_table(index='year', columns='name', values='births', aggfunc=sum)
print(p2)

# # 몇몇 이름의 추이
# d1 = p2[['Anna', 'Elizabeth', 'Sophia', 'Henry', 'Robert']]
# print(d1)
# plt.plot(d1)
# plt.legend(d1.columns)
# plt.show()