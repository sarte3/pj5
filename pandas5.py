import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='D2Coding-Ver1.3.2-20180524-all.ttc').get_name()
rc('font', family=fontname)

# tips = sns.load_dataset('tips')

# print(tips)

# 요일별 식대의 집계
# print(tips.groupby('day')['total_bill'].mean())
# tips10 = tips.sample(10, random_state=42)
# # print(tips10)

# g1 = tips10.groupby('sex')
# # print(g1)
# # 그룹 객체의 속성 groups
# print(g1.groups)
# # 그룹 객체의 메서드
# print(g1.get_group('Female')) # 특정 그룹 추출
# print('-'*30)
# for data in g1:
#     print(data)
#     print(type(data))
#     print(len(data))
#     print(type(data[0]), type(data[1]))
# print(tips)

# # 성별별 식대의 평균
# # g1 = tips.groupby('sex')['total_bill'].mean()
# g1 = tips.groupby('sex').total_bill.mean()

# print(g1)

# # 성별별 식사시간의 식대 평균
# g2 = tips.groupby(['sex', 'time']).total_bill.mean()
# # print(g2)
# # print(type(g2)) # 시리즈
# # print(g2.index)
# # print(g2.values)
# print(g2.sort_values()) # 값 순서대로 정렬
# print('-'*30)
# d2 = g2.reset_index() # 기존 인덱스를 일반 칼럼으로, 인덱스는 일련번호로 부여
# print(d2)
# print(type(d2)) # 데이터 프레임

# data = pd.read_csv('data/accidentdata.csv')
# print(data)
# 요일별 교통사고 사상자 합계분석(단, 사상자수 3명 이상인 데이터)
# d1 = data[data['사상자수']>=3]
# print(d1)
# g1 = d1.groupby('요일')['사상자수'].sum()
# print(g1) # 시리즈
# g1 = g1.reindex(['월','화','수','목','금','토','일'])
# print(g1)
# plt.plot(g1) # plt.plot([x값,] y값)
# plt.plot(g1.index, g1.values)
# plt.title('2012~2014 교통사고 요일별 사상자수 합')
# plt.xlabel('요일')
# plt.ylabel('사상자수')
# plt.show()

# 시리즈를 데이터프레임으로 변경
# d2 = g1.reset_index()
# print(d2)
# plt.plot(d2['요일'], d2['사상자수'])
# plt.show()

# 경기도내 교통사망사고가 높은 5개지역 분석하여 도식화
# d2 = data[data['발생지시도']=='경기']
# # print(d2)
# # print(d2.loc[1])
# g2 = d2.groupby('발생지시군구')['사망자수'].sum()
# # print(g2)
# g2 = g2.sort_values(ascending=False).head(5)
# print(g2)
# # plt.plot(g2.index, g2.values, 'o')
# # plt.show()
# plt.pie(g2, labels=g2.index, colors=['red', 'green', 'blue', 'yellow', 'purple'], autopct='%.2f%%')
# plt.title('2012-2014 경기도 교통사망사고 높은 지역 5')
# plt.show()

# movies = pd.read_csv('data/ml-1m/movies.dat', sep='::', names=['MovieID', 'Title', 'Genres'])
# print(movies)

# ratings = pd.read_csv('data/ml-1m/ratings.dat', sep='::', names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
# print(ratings)

# users = pd.read_csv('data/ml-1m/users.dat', sep='::', names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'])
# print(users)

c1 = pd.read_csv('data/concat_1.csv')
# print(c1)
c2 = pd.read_csv('data/concat_2.csv')
# print(c2)
c3 = pd.read_csv('data/concat_3.csv')
# print(c3)

# 데이터의 연결
# concat : 한 번에 2개 이상의 데이터프레임을 연결
# data = pd.concat([c1, c2, c3])
# print(data)
# print(data.loc[3])
# data = pd.concat([c1, c2, c3], ignore_index=True)
# print(data)

c2['E']='eee'
# print(c2)
# print(c3)
# data = pd.concat([c1, c2, c3], ignore_index=True)
# print(data)
# 열방향 합치기
data = pd.concat([c1, c2, c3], ignore_index=True, axis=1)
print(data)

# 과제) gap.tsv 파일을 data라는 데이터프레임으로 생성하여
# 다음을 진행하세요

# 1) 연도별 기대수명의 평균을 구하세요
# 2) 연도별 기대수명의 변화를 선그래프로 출력
# 3) 연도별, 대륙별, 기대수명의 평균을 구하세요

# 4) result2007.csv를 활용하여 월별 도착지연 횟수를 선그래프로 출력하세요
# 소스와 그래프 이미지 캡처