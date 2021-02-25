import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# tips = sns.load_dataset('tips')
# tips10 = tips.sample(10, random_state=42)
# print(tips10)

# # 성별별 식대의 큰 금액 2개 추출
# g3 = tips10.groupby('sex')

# def getbill2(x):
#     return x.sort_values(by='total_bill', ascending=False)[:2]

# bill2 = g3.apply(getbill2)
# print(bill2)

ebola = pd.read_csv('data/ebola.csv')
# print(ebola)

ebola2 = ebola.iloc[:5,[0, 2, 3, 10, 11]]
# print(ebola2)

# melt() 열의 데이터를 행으로
# id_vars : 위치를 유지할 열 이름
# var_name : 위치를 변경한 열 이름
# value_name : 위치를 변경한 열의 데이터 이름
# ebola3 = pd.melt(ebola2, id_vars='Date')
# print(ebola3)
# ebola3 = pd.melt(ebola2, id_vars=['Date','Day'])
# print(ebola3)
ebola3 = pd.melt(ebola2, id_vars=['Date'] ,var_name='kind', value_name='cnt')
# print(ebola3)
# print(ebola3['kind'])
# print(ebola3['kind'][0])
# print(ebola3['kind'][0].split('_'))

# 데이터프레임 또는 시리즈에서 접근자
# 문자열 str
# 날짜 dt
# print(ebola3['kind'].str.split('_'))
ebola3['new'] = ebola3['kind'].str.split('_')
# print(ebola3)
# print(ebola3['new'].str.get(0))
# print(ebola3['new'].str.get(1))

ebola3['st'] = ebola3['new'].str.get(0)
ebola3['country'] = ebola3['new'].str.get(1)
ebola3 = ebola3.drop('new', axis=1)
# print(ebola3)

ebola3['st,country']=ebola3['st']+ebola3['country']
# print(ebola3)

# ebola3.info()
ebola3['Date']=pd.to_datetime(ebola3['Date'])
ebola3.info()
# print(ebola3)

ebola3['yy']=ebola3['Date'].dt.year
ebola3['mm']=ebola3['Date'].dt.month
ebola3['dd']=ebola3['Date'].dt.day
print(ebola3)

# ebola4 = ebola.iloc[:5,[0, 2, 3, 10, 11]]
# print(ebola4)
# ebola5 = pd.melt(ebola2, id_vars=['Date','Day'])
# print(ebola5)

# s1 = 'Cases_Guinea' nu7  
# print(s1.split('_'))

