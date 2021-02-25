import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 데이터파일 rtest.csv를 이용하여 data란 이름의 데이터프레임을 생성한후 다음을 진행 하시오. 
data = pd.read_csv('data/rtest.csv')

# 1) data 데이터 프레임의 각 열의 데이터 타입과 행과 열의 수를 확인하시오
data.info()

# 2) 거주지(regident) 컬럼은 다음과 같다. regident2컬럼을 추가하여 해당하는 지역을 표현하시오
#  1. 서울 2. 인천 3. 대전 4. 대구 5.시구군
def getResident(x):
    if x == 1:
        return '서울'
    elif x == 2:
        return '인천'
    elif x == 3:
        return '대전'
    elif x == 4:
        return '대구'
    elif x == 5:
        return '시구군'

data['resident2'] = data['resident'].apply(getResident)
# print(dat/)

# 3) age변수가 널인 자료 제거하고 자료의 행과 열의 수를 확인하시오
# data = data.dropna(subset=['age'])
data = data[data['age'].notnull()]
print(data.shape)

# 4) age변수의 최소값, 최대값, 평균을 출력하시오. 
min = data['age'].min()
max = data['age'].max()
mean = data['age'].mean()
print(min, max, mean) 

# 5) age 변수를 박스그림으로 표현하여 값의 범위를 확인하시오
plt.boxplot(data['age'], labels=['age'])
plt.show()

# 6) age 변수를 참조하여 30세이하는 청년층, 31세-55세는 중년층,56세 이상은 장년층
# 으로 하여 age2변수를 추가하시오
def getAge(x):
    if x<=30:
        return "청년층"
    elif 31<=x<=55:
        return "중년층"
    elif x>=56:
        return "장년층"

data['age2']=data['age'].apply(getAge)
print(data)

# 7) data의 gender 칼럼을 대상으로 1->"남자", 2->"여자" 형태로 코딩 변경하여 gender2 칼럼에 추가하시오. 
def getGender(x):
    if x==1:
        return "남자"
    elif x==2:
        return "여자"

data['gender2']=data['gender'].apply(getGender)
print(data)

# 8) gender2칼럼을 기준으로 남녀의 빈도수를 확인하시오
g1 = data.groupby('gender2')['gender'].count()
print(g1)

# 9) 7번의 결과를 파이차트로 표현하시오
plt.pie(g1)
plt.legend(g1.index)
plt.show()

# 10) 나이에 따른 구매비용의 관계를 그래프로 표현하시오
plt.scatter(data['age'], data['price'])
plt.title('나이에 따른 구매비용')
plt.show()