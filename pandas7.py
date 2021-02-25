import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='D2Coding-Ver1.3.2-20180524-all.ttc').get_name()
rc('font', family=fontname)

ebola = pd.read_csv('data/ebola.csv')
# print(ebola)
# ebola.info()
# print(ebola.shape)
# print('값의 개수\n', ebola.count())
# print('누락 값의 개수\n', ebola.shape[0]-ebola.count())
# e1 = ebola.iloc[:10, :5]
# print(e1)
# 누락값 처리 fillna()
# print('지정된 값으로 변경\n', e1.fillna(0))
# print('누락값 전의 값으로 변경\n', e1.fillna(method='ffill'))
# print('누락값 후의 값으로 변경\n', e1.fillna(method='bfill'))
# print('누락값 양쪽에 있는 값의 평균값으로 변경\n', e1.interpolate())
# print('누락값이 포함된 행 삭제', e1.dropna())
# 누락값이 포함된 연산
# e1['tot'] = e1['Cases_Guinea']+e1['Cases_Liberia']+e1['Cases_SierraLeone']
# print(e1)
# e1['tot'] = e1['Cases_Guinea'].fillna(0)+e1['Cases_Liberia'].fillna(0)+e1['Cases_SierraLeone'].fillna(0)
# # print(e1)
# print(e1.Cases_Guinea.sum())
# print(e1['Cases_Guinea'].sum(skipna=False)) #skipna 결측치 무시
# print(e1.Cases_Guinea.mean())

# 피벗테이블
# data = pd.DataFrame({
#     "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천" ],
#     "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010" ],
#     "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 2632035],
#     "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
# })
# # print(data)
# # pivot(행인덱스로 사용할 열, 열인덱스로 사용할 열, 데이터로 사용할 열)
# # pivot_table(데이터로 사용할 열, 행인덱스로 사용할 열, 열인덱스로 사용할 열)
# # p1 = data.pivot('도시', '연도', '인구')
# p1 = data.pivot_table(index='도시', columns='연도', values='인구')

# # print(p1)
# # print(type(p1))
# # print(p1.index)
# # print(p1.columns)
# p2 = data.pivot_table(index=['도시','연도'], values='인구')
# print(p2)

data2 = pd.read_excel('data\\판매현황.xlsx')
# p2 = pd.pivot_table(data2, index='분류', values='판매수량')
# p2 = pd.pivot_table(data2, index='분류', values='판매수량', aggfunc=sum) 
# # aggfunc을 지정하지 않으면 평균을 구함
# print(p2)
# p2 = p2.reset_index()
# print(p2)

# 교통사고
data = pd.read_csv('data/accidentdata.csv')
# print(data)
# 요일별 발생지시도별 교통사고 사망자 분석
print(data.columns)
p1 = data.pivot_table(index='요일', columns='발생지시도', values='사망자수', aggfunc=sum)
print(p1)
p1 = p1.reindex(['월','화','수','목','금','토','일'])
plt.plot(p1)
plt.legend(p1.columns)
plt.show()