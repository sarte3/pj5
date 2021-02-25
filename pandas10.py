from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

from datetime import datetime

# now1 = datetime.now()
# print(now1)
# print(type(now1))
# s1 = now1.strftime('%Y-%m-%d')
# s2 = now1.strftime('%H-%M-%S')
# print(s1)
# print(s2)
# print(type(s1))

# t1 = datetime(2020,1,1)
# print(t1)
# # 시간 계산
# print(now1-t1)
# print(type(now1-t1))

# ebola = pd.read_csv('data/ebola.csv')
# ebola.info()
# ebola['Date'] = pd.to_datetime(ebola['Date'])
# ebola.info()

ebola = pd.read_csv('data/ebola.csv', parse_dates=['Date'])
# ebola.info()
# print(ebola['Date'].head())
# print(ebola['Date'][2])
# print(ebola['Date'][2].year)
# print(ebola['Date'][2].month)
# print(ebola['Date'][2].day)
# print(ebola['Date'][2].quarter)
# print('에볼라 최초 발생일', ebola['Date'].min())
# print(ebola['Date'].tail())
# ebola['new']=ebola['Date']-ebola['Date'].min()
# print(ebola)

# bank = pd.read_csv('data/bank.csv')
# bank.info()
# print(bank)

# 연도별 파산한 은행 수
bank = pd.read_csv('data/bank.csv', parse_dates=['Closing Date', 'Updated Date'])
# bank.info()
# print(bank)
bank['year']=bank['Closing Date'].dt.year
# print(bank)
# print(bank.groupby('year').count())
# print(bank.groupby('year')['Bank Name'].count())
# s1 = bank.groupby('year').size()
# plt.plot(s1)
# plt.xticks(list(range(2000, 2020, 2)))
# plt.show()

# 연도별 분기별 파산한 은행 수
bank['quarter']=bank['Closing Date'].dt.quarter
# print(bank)
s2 = bank.groupby(['year', 'quarter']).size()
# print(s2)
# print(type(s2))

# # plt.plot(s2) error
# plt.plot(s2.values)
# plt.title('연도별 분기별 파산한 은행 수')
# plt.show()

d2 = s2.reset_index()
# print(d2)
d2['new']=d2['year'].astype(str)+'-'+d2['quarter'].astype(str)
print(d2)

plt.plot(d2['new'], d2[0])
plt.title('연도별 분기별 파산한 은행 수')
plt.show()

