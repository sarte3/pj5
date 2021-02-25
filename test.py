import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 1) 데이터 시각화의 개념과 목적을 쓰시오. 
# 데이터 시각화(data visualization)는 데이터 분석 결과를 쉽게 이해할 수 있도록 시각적으로 표현하고 전달되는 과정을 말한다. 
# 데이터 시각화의 목적은 도표(graph)라는 수단을 통해 정보를 명확하고 효과적으로 전달하는 것이다.

# 2-10) 데이터파일 report.csv, bank.csv파일과 seaborn내의 tips 데이터를 이용하여 다음을 진행하시오. 
# 2) report.csv파일을 활용하여 데이터를 데이터프레임으로 읽어 들여 해당 데이터프레임의 변수들을 확인하고 처음 10개, 마지막 10개의 데이터를 출력하시오
df = pd.read_csv('data/report.csv')
df.info()
print(df.head(10))
print(df.tail(10))

# 3) report.csv파일을 활용하여 New Hampshire주의 Beer 소비량과 Wine 소비량의 산점도를 나타내시오
plt.scatter(df[df['State']=='New Hampshire']['Beer'], df[df['State']=='New Hampshire']['Wine'])
plt.title('New Hampshire주의 Beer 소비량과 Wine 소비량의 산점도')
plt.show()

# 4) report.csv파일을 활용하여 New Hampshire, Colorado, Utah 주의 맥주 소비량의 변화를 선그래프로 작성하시오 (그래프제목 : 주별 맥주 소비량의 변화, 범례추가,
#  x축제목 : 년도, y축제목 : 맥주소비량, 스타일 :ggplot)
plt.style.use('ggplot')
plt.plot(df[df['State']=='New Hampshire']['Year'], df[df['State']=='New Hampshire']['Beer'])
plt.plot(df[df['State']=='New Hampshire']['Year'], df[df['State']=='Colorado']['Beer'])
plt.plot(df[df['State']=='New Hampshire']['Year'], df[df['State']=='Utah']['Beer'])
plt.title('주별 맥주 소비량의 변화')
plt.legend(['New Hampshire', 'Colorado', 'Utah'])
plt.xlabel('연도')
plt.ylabel('맥주소비량')
plt.show()

# 5) tips 데이터의 각 열의 데이터 형을 확인하시오
tips = sns.load_dataset('tips')
tips.info()

# 6) tips 데이터에서 식사시간별 total_bill의 최소값, 최대값, 평균, 중간값을 확인하고 상자그림을 그리시오
d1 = tips.groupby('time').agg({'total_bill': ['min', 'max', 'mean', 'median']})
print(d1)
d2 = tips.groupby('time')['total_bill']
print(d2)
plt.boxplot([tips[tips['time']=='Lunch']['total_bill'], tips[tips['time']=='Dinner']['total_bill']], labels=['점심', '저녁'])
plt.show()

# 7) tips 데이터에서 행인덱스로 좌석수, 열인덱스로 요일을 지정하여 식사비용의 금액의 합계를 나타내시오
d3 = tips.pivot_table(index='size', columns='day', values='total_bill' ,aggfunc='sum')
print(d3)

# 8) 6번의 결과를 선그래프로 나타내시오.
# (그래프제목 : 식사 비용 현황, 범례:요일표시, x축제목 : 좌석수, y축제목 : 식사비용 )
d3 = d3.fillna(0)
plt.plot(d3)
plt.title('식사 비용 현황')
plt.legend(d3.columns)
plt.xlabel('좌석수')
plt.ylabel('식사비용')
plt.show()

# 9) bank.csv 데이터 파일의 데이터를 확인하고 날짜와 관련된 열은 datetime형으로 변환하시오
bank = pd.read_csv('data/bank.csv')
bank.info()
bank['Closing Date'] = pd.to_datetime(bank['Closing Date'])
bank['Updated Date'] = pd.to_datetime(bank['Updated Date'])
bank.info()

# 10) bank.csv 데이터에서 연도별 파산한 은행의 수를 그래프로 표시하시오
bank['year']=bank['Closing Date'].dt.year
s1 = bank.groupby('year').size()
plt.plot(s1)
plt.title('연도별 파산한 은행 수')
plt.xticks(list(range(2000, 2020, 2)))
plt.show()