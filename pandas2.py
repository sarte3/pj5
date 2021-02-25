import pandas as pd
import seaborn as sns

# 데이터프레임(2차원), 시리즈(1차원)

tips = sns.load_dataset('tips')

# print(tips)
# print(tips.head())
# print(tips.head(7))
# print(tips.tail())
# print(tips.tail(7))
# print(type(tips)) # 데이터프레임(2차원)
# print(tips.shape) # 행과 열에 대한 정보
# print(tips.shape[0]) # 행의 수
# print(tips.shape[1]) # 열의 수
# print(tips.columns) # 열 이름
# print(tips.dtypes) # 각 열의 데이터형
# tips.info()
# print(tips.info())

# print(tips['total_bill']) # 원하는 열에 접근, 시리즈
# print(type(tips['total_bill']))

# sm = tips['smoker']
# print(type(sm))

# loc : 인덱스를 기준으로 행데이터 추출
# iloc : 행번호를 기준으로 행데이터 추출, 판다스에서 행번호 부여
# r240 = tips.loc[240]
# print(r240)
# print(type(r240))

# print(tips[['total_bill', 'tip', 'smoker']]) 
# print(type(tips[['total_bill', 'tip', 'smoker']]))

# titanic = sns.load_dataset('titanic')
# print(titanic)

# 인덱스 변경
# t1 = tips.set_index('total_bill')
# print(t1)
# t1 = t1.reset_index() # 기존 인덱스를 열로, 새롭게 번호 부여
# print(t1)
# print('-'*30)
# t1 = t1.reset_index()
# print(t1)

# print(tips.loc[[10, 20, 30]])
# print(tips.iloc[[10, 20, 30]])
# print(tips.loc[243])
# print(tips.loc[-1]) error
# print(tips.iloc[10:-1])

# print(range(10, 50, 10))
# print(list(range(10, 50, 10)))

# t1 = tips.loc[:,['total_bill','tip']] #데이터프레임[행, 열]
# print(t1)

# t1 = tips.iloc[:,['total_bill','tip']] #error
# t1 = tips.iloc[:, [0, 1]]
# print(t1)
# print(tips.iloc[list(range(10, 50, 10)), [0, 1]])
# print(tips.iloc[:10, 2:5])
# print(tips.loc[:10, ['sex', 'smoker', 'day']])


movies = pd.read_csv('data/movie.csv', header=None)
# # print(movies)
# m1 = movies.set_index(0)
# # print(m1)
# # print(m1[1])
# # print(m1.loc['도굴'])
# # print(m1.iloc[2])
# print(m1.loc[['조제', '도굴']])
# print(m1.iloc[[0, 2]])
print(movies.loc[list(range(10,100,30)), [0, 2]])