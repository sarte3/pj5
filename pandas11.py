import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# def plus3(x):
#     return x+3

# def plusn(x, n):
#     return x+n

# def cal(x, n, m):
#     return (x+n)*m

# df = pd.DataFrame({'a':[1, 2, 3],
#     'b':[10, 20, 30]})
# # print(df)
# # print(df['a'].apply(plus3))
# # print(df['a'].apply(plusn, n = 10))
# # print(df['a'].apply(cal, n = 10, m = 3))

# print(df.apply(cal, n=10, m=3))
# print(df.apply(cal, n=10, m=3, axis=1))

# def hap(x):
#     print(x)
#     print('-'*30)
#     return x.sum()

# df = pd.DataFrame({'name':['kim', 'park', 'kim', 'park'],
#     'grade':[1, 2, 3, 2],
#     'kor':[10, 20, 10, 30],
#     'eng':[10, 20, 30, 40]})

# print(df)
# # print(df.groupby(['name', 'grade']).apply(hap))
# # print(df.groupby(['name', 'grade'])['kor'].apply(hap))
# # print(df.groupby(['name', 'grade'])['kor'].apply(lambda x:x.sum()))

# def getAvg(x):
#     # print(x)
#     return x.mean()

# # print(df.groupby('name')['kor'].apply(getAvg))
# # agg() 메서드
# # 여러 개의 집계메서드를 한 번에 사용
# # print(df.groupby('name')['kor'].agg(getAvg))
# # print(df.groupby('name')['kor'].mean())

# # print(df.groupby('name')['kor'].agg(['sum', 'mean', 'median', 'std']))
# # print(df.groupby('name').agg({'kor':'sum', 'eng':'mean'}))
# print(df.groupby(['name', 'grade']).agg({'kor':['sum', 'mean', 'median', 'std'], 'eng':lambda x:x.mean()}))

# tips = sns.load_dataset('tips')
# # print(tips.head())
# tips['rate'] = tips['tip']/tips['total_bill']
# print(tips.head())
# g1 = tips.groupby(['sex', 'smoker'])
# print(g1.agg({'total_bill':'sum', 'tip':'std', 'rate':'mean'}))

# print(list(range(1, 100, 10)))

# print(pd.date_range(start='2020-1-1', end='2020-12-31'))
# print(pd.date_range(start='2020-1-1', end='2020-12-31', freq='W-MON'))

ebola = pd.read_csv('data/ebola.csv')
# print(ebola)
# ebola5 = ebola.head()
# # print(ebola5)
# # 컬럼의 데이터 형 변환
# ebola5['Date']=pd.to_datetime(ebola5['Date'])
# ebola5.info()
# # print(pd.date_range(start='2014-12-31', end='2015-1-5'))
# # 인덱스 변경
# ebola5 = ebola5.set_index('Date')
# # print(ebola5)
# # 인덱스 정렬
# ebola5 = ebola5.reindex(pd.date_range(start='2014-12-31', end='2015-1-5'))
# print(ebola5)
# # plt.plot(ebola5)
# # plt.show()

# # print(ebola)
# ebola['Date']=pd.to_datetime(ebola['Date'])
# ebola = ebola.set_index('Date')
# print(ebola.iloc[:,:5])
# ebola = ebola.reindex(pd.date_range(start='2014-3-22', end='2015-1-5'))
# print(ebola.iloc[:5, :5])

# print(pd.date_range(start='2021-1-1', end='2021-12-31', freq='M'))
# print(pd.date_range(start='2021-1-1', end='2021-12-31', freq='W'))
print(pd.date_range(start='2021-1-1', end='2021-12-31', freq='B'))

# 과제
# 1) tips 데이터를 데이터프레임으로 읽고 식대와 팁과의 관계를 그래프로 표현하세요, 투명도(alpha값을 0.5로 지정)