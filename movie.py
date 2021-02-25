import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# movies = pd.read_csv('data/ml-1m/movies.dat', sep='::', names=['MovieID', 'Title', 'Genres'])
# # print(movies)

# ratings = pd.read_csv('data/ml-1m/ratings.dat', sep='::', names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
# # print(ratings)

# users = pd.read_csv('data/ml-1m/users.dat', sep='::', names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'])
# # print(users)

# mr = pd.merge(movies, ratings, on='MovieID')
# print(mr)
# data = pd.merge(mr, users, on='UserID')
# print(data)
# data.to_csv('data/movie2.csv', index=False)

data = pd.read_csv('data/movie2.csv')
# print(data)
# print(data.columns)

# 영화 제목 별 평점 건수
titlecnt = data.groupby('Title')['Rating'].size()
# titlecnt = data.groupby('Title')['Rating'].count() 
# print(titlecnt)

# 평점 정보가 200건 이상 있는 영화
r200 = titlecnt[titlecnt>=200]
# print(r200)
# print(r200.index) # 평점 정보가 200건 이상 있는 영화 제목
data = data.set_index('Title')
# print(data)
data200 = data.loc[r200.index]
# print(data200)
data200 = data200.reset_index()
# print(data200)

# # 영화별 평균 평점
# print(data200.groupby('Title').Rating.mean())

# # 성별에 따른 평균평점
# print(data200.groupby(['Title', 'Gender']).Rating.mean())

# # 여성에게 높은 평점을 받은 영화 5
# s1 = data200.groupby(['Title', 'Gender']).Rating.mean()
# d1 = s1.reset_index()
# print(d1)
# d1 = d1[d1['Gender']=='F']
# print(d1)
# print(d1.sort_values(by='Rating', ascending=False).head(5))

# # tips 데이터에서 토, 일 데이터만 추출
# # print('-'*30)
# import seaborn as sns
# tips = sns.load_dataset('tips')
# # print(tips)

# # 요일별 식사 건수
# g1 = tips.groupby('day').size()
# print(g1)

# # 식사 건수가 50건 이상인 데이터만 가지고 분석
# g2 = g1[g1>50]
# print(g2)
# print(g2.index)
# print(g2.values)

# tips = tips.set_index('day')
# print(tips)
# print(tips.loc[g2.index])

# tips = tips.set_index('day')
# print(tips)

# print(tips.loc[['Sun', 'Sat']])

# 성별에 따른 영화 평점
p1 = pd.pivot_table(data200, index='Title', columns='Gender', values='Rating')
# print(p1)

# # 남자들이 좋아하는 영화 10개
# print(p1.sort_values(by='M', ascending=False).head(10))

# # 남녀간에 호불호가 갈리는 영화 10개
# p1['diff']=(p1['F']-p1['M']).abs()
# print(p1)
# print(p1.sort_values(by='diff', ascending=False).head(10))

# 호불호가 갈리는 영화 10개
g2 = data200.groupby('Title')['Rating'].std() 
# print('영화별 평점의 표준편차\n', g2)
# print(g2.sort_values(ascending=False).head(10))

# 과제
# 1) data 데이터프레임의 'Age'열을 활용하여 data['Newage'] 열을 생성하세요
#    *  1:  "Under 18"
#    * 18:  "18-24"
#    * 25:  "25-34"
#    * 35:  "35-44"
#    * 45:  "45-49"
#    * 50:  "50-55"
#    * 56:  "56+"

def makeNewage(x):
     
    if x == 1:
        return 'Under 18'
    elif x == 18:
        return '18-24'
    elif x == 25:
        return '25-34'
    elif x == 35:
        return '35-44'
    elif x == 45:
        return '45-49'
    elif x == 50:
        return '50-55'
    elif x == 56:
        return '56+'

data['Newage'] = data['Age'].apply(makeNewage)
print(data)

# 2) 연령대별 평점 점수의 평균 출력(data['Newage']열 활용)
g1 = data.groupby('Newage')['Rating'].mean()
print(g1)

# 3) 연령대별 평점 점수가 낮은 사람 3건 출력(data['Newage']열 활용)
g2 = data.groupby('Newage')

def getRating(x):
    return x.sort_values(by='Rating')[:3]

r = g2.apply(getRating)
print(r)

