import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 과제) gap.tsv 파일을 data라는 데이터프레임으로 생성하여
# 다음을 진행하세요
data = pd.read_csv('data/gap.tsv', sep='\t')

# 1) 연도별 기대수명의 평균을 구하세요
d1 = data.groupby('year')['lifeExp'].mean()
print(d1)

# 2) 연도별 기대수명의 변화를 선그래프로 출력
plt.plot(d1.index, d1.values)
plt.title('연도별 기대수명의 변화')
plt.xlabel('연도')
plt.ylabel('기대 수명')
plt.show()

# 3) 연도별, 대륙별, 기대수명의 평균을 구하세요
d2 = data.groupby(['year', 'continent'])['lifeExp'].mean()
print(d2)

# 4) result2007.csv를 활용하여 월별 도착지연 횟수를 선그래프로 출력하세요
data2 = pd.read_csv('data/2007.csv', names=['year', 'month', 'count'])
d3 = data2.sort_values('month', ascending=True)
plt.plot(d3['month'], d3['count'])
plt.title('월별 도착 지연 횟수')
plt.xlabel('월별')
plt.ylabel('일별')
plt.show()

# 소스와 그래프 이미지 캡처