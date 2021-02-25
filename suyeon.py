import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)
# 과제
# 서울에서 경기, 부산, 광주, 제주로 이사한 데이터를 한 화면에 선 그래프로 각각 그리세요
data=pd.read_excel('data\\시도별 전출입 인구수.xlsx')
# print(data.head(10))
data = data.fillna(method='ffill')
d1=data[(data['전출지별']=='서울특별시') & (data['전입지별']!='서울특별시')]
d1=d1.drop('전출지별',axis=1)
d1=d1.rename(columns={'전입지별':'전입지'})
d1=d1.set_index('전입지')
print(d1)
dk=d1.loc['경기도']
d2=d1.loc[['부산광역시','광주광역시','제주특별자치도'],:]
d2=d2.transpose()
d2['광주광역시']=pd.to_numeric(d2['광주광역시'],errors='coerce')
d2['광주광역시']=d2['광주광역시'].fillna(0)
fig = plt.figure()
a1 = fig.add_subplot(2, 2, 1)
a2 = fig.add_subplot(2, 2, 2)
a3 = fig.add_subplot(2, 2, 3)
a4 = fig.add_subplot(2, 2, 4)

a1.plot(dk)
a2.plot(d2['부산광역시'], 'r')
a3.plot(d2['광주광역시'], 'g')
a4.plot(d2['제주특별자치도'], 'y')

a1.set_title('경기')
a2.set_title('부산')
a3.set_title('광주')
a4.set_title('제주')

fig.suptitle('서울 -> 타지역 이동')
fig.tight_layout()
plt.show()