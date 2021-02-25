from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

data = pd.read_excel('data/시도별 전출입 인구수.xlsx')
# print(data.head(10))
data = data.fillna(method='ffill')
# print(data.head(10))
# print(data.shape)

# 서울에서 다른 지방으로 이사한 데이터만 선그래프로
d1 = data[(data['전출지별']=='서울특별시') & (data['전입지별']!='서울특별시')]
# print(d1.head(10))
# print(d1.shape)
d1 = d1.drop('전출지별', axis=1)
# print(d1)
d1 = d1.rename(columns={'전입지별':'전입지'})
# print(d1)
d1 = d1.set_index('전입지')
# print(d1) # 서울에서 타지역으로 이사한 데이터
dk = d1.loc['경기도']
# print(dk)
# plt.style.use('ggplot') # 스타일 지정
# plt.figure(figsize=(15, 5))
# # plt.plot(dk) # 선 그래프
# # plt.plot(dk, 'o') # 점 그래프
# plt.plot(dk, marker='o', markersize=10, markerfacecolor='green', color='red', linewidth=2)
# # 마커 모양 , o, +, *, .
# plt.title('서울 -> 경기 이동', size = 20)
# plt.xlabel('연도')
# plt.ylabel('이동 수')
# plt.xticks(size = 7, rotation = 70)
# plt.legend(['서울 -> 경기'], fontsize = 7)
# plt.annotate('인구 이동 증가', xy=(10, 500000), fontsize=15, ha='center', rotation=30)
# # xy, 텍스트 기준점, ha=가로정렬(left, center, right), va=세로정렬(top, center, bottom)
# plt.annotate('', xy=(19, 550000), xytext=(4, 300000), arrowprops=dict(arrowstyle='->', color='skyblue', lw=5))
# xy=(화살표 머리부분), xytext=(화살표 꼬리 부분)
# plt.show()
# print('스타일 종류', plt.style.available)
# print('matplotlib에서 사용할 수 있는 색의 종류')
# import matplotlib
# temp = {}
# for n, h in matplotlib.colors.cnames.items():
#     temp[n] = h
# print(temp)

d2 = d1.loc[['부산광역시', '광주광역시', '제주특별자치도'],:]
# print(d2)
d2 = d2.transpose() # 행열 전환
# print(d2)
d2['광주광역시'] = pd.to_numeric(d2['광주광역시'], errors='coerce')
# print(d2)
d2['광주광역시'] = d2['광주광역시'].fillna(0)
print(d2)
# dp = d1.loc['부산광역시']
# dg = d1.loc['광주광역시']
# print(dg)
# print(dp)
# plt.style.use('ggplot') # 스타일 지정
# plt.figure(figsize=(15, 5))
# # plt.plot(dk) # 선 그래프
# # plt.plot(dk, 'o') # 점 그래프
# plt.plot(dk)
# plt.plot(d2['부산광역시'])
# plt.plot(d2['광주광역시'])
# plt.plot(d2['제주특별자치도'])
# # plt.plot(d1.loc['제주특별자치도'])
# # plt.plot(d1.loc['광주광역시'])
# plt.title('서울 -> 타지역 이동', size = 20)
# plt.xlabel('연도')
# plt.ylabel('이동 수')
# plt.xticks(size = 7, rotation = 70)
# plt.legend(['서울 -> 경기', '서울 -> 부산', '서울 -> 광주', '서울 -> 제주'])
# plt.show()

# 과제
# 서울에서 경기, 부산, 광주, 제주로 이사한 데이터를 한 화면에 선 그래프로 각각 그리세요

fig = plt.figure()
a1 = fig.add_subplot(2, 2, 1) 
a2 = fig.add_subplot(2, 2, 2) 
a3 = fig.add_subplot(2, 2, 3)
a4 = fig.add_subplot(2, 2, 4)

a1.plot(dk)
a2.plot(d2['부산광역시'], 'r')
a3.plot(d2['광주광역시'], 'g')
a4.plot(d2['제주특별자치도'], 'y')

a1.set_title('서울 -> 경기')
a2.set_title('서울 -> 부산')
a3.set_title('서울 -> 광주')
a4.set_title('서울 -> 제주')

fig.suptitle('서울 -> 타지역 이동')
fig.tight_layout()
plt.show()
