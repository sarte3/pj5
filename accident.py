import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)


data = pd.read_csv('data/accidentdata.csv')
# print(data)

# 과제) 요일별 교통사고 사상자수(단, 사상자수가 3명 이상인 데이터) 상자그림으로
# print(data.columns)
d1 = data[data['사상자수']>=3]
# print(d1)
# 1) 일요일 사상자수의 최대값과 최소값을 출력
print(d1[d1['요일']=='일']['사상자수'].max())
print(d1[d1['요일']=='일']['사상자수'].min())

# 2) 일요일의 교통사고 사상자수 분포를 상자그림으로 나타내세요
plt.boxplot(d1[d1['요일']=='일']['사상자수'])
plt.xlabel('일요일')
plt.ylabel('사상자수')
plt.title('일요일의 교통사고 사상자수 분포')
plt.show()

# 3) 요일별 교통사고 사상자수를 상자그림으로
list = ['일', '월', '화', '수' ,'목' ,'금' ,'토']
arr = []
for i in range(len(list)):
    arr.append(d1[d1['요일']=='{}'.format(list[i])]['사상자수'])
plt.boxplot(arr, labels = list)
plt.title('요일별 교통사고 사상자수')
plt.xlabel('요일')
plt.ylabel('사상자수')
plt.show()

# plt.boxplot([d1[d1['요일']=='일']['사상자수'], d1[d1['요일']=='월']['사상자수'], d1[d1['요일']=='화']['사상자수'], d1[d1['요일']=='수']['사상자수'], d1[d1['요일']=='목']['사상자수'], d1[d1['요일']=='금']['사상자수'], d1[d1['요일']=='토']['사상자수']], labels=['일','월','화','수','목','금','토'])
# plt.ylabel('사상자수')
# plt.title('요일별 교통사고 사상자수 분포')
# plt.show()