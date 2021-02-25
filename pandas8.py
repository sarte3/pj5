import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

tips = sns.load_dataset('tips')

# print(tips.dtypes)

# 자료형 변환(astype(), to_numeric())
# tips['newsex']=tips['sex'].astype(str)
# # print(tips)
# # print(tips.dtypes)
# tips['total_bill'] = tips['total_bill'].astype(str)
# # print(tips.dtypes)

# tips10 = tips.head(10)
# # print(tips10)
# # print(tips10.dtypes)
# tips10.loc[[3, 6, 9], 'total_bill'] = 'not float'
# # print(tips10)
# # tips10['total_bill'] = tips10['total_bill'].astype(float) 오류 'not float'때문에 형변환 안됨
# # print(tips10)
# # tips10['total_bill'] = pd.to_numeric(tips10['total_bill']) # 오류
# # tips10['total_bill'] = pd.to_numeric(tips10['total_bill'], errors='ignore') # 오류가 나면 무시, 변환 안됨
# # print(tips10)
# # print(tips10.dtypes) # 데이터형 변환 X

# # tips10['total_bill'] = pd.to_numeric(tips10['total_bill'], errors='coerce')
# tips10['total_bill'] = pd.to_numeric(tips10['total_bill'], errors='coerce', downcast='float')
# # print(tips10)
# # print(tips10.dtypes)

# # tips.info()
# # tips['sex']=tips['sex'].astype(str)
# # tips.info()
# # tips['sex']=tips['sex'].astype('category')
# # tips.info()

# # 함수

# def double(x):
#     print(x, '\n**')
#     return x*2

# # print(double(7))

# data = pd.DataFrame({
#     'a':[1, 2, 3],
#     'b':[10, 20, 30]
# })
# print(data)

# 시리즈, 데이터프레임에 함수 적용시 
# 시리즈 or 데이터프레임.apply(함수명)
# s1 = data['a'].apply(double)
# print(s1)
# s2 = data['b'].apply(double)
# print(s2)
# d1 = data.apply(double) # 열 우선 실행
# print(d1)
# d2 = data.apply(double, axis=1) # 행 우선 실행
# print(d2)

# def sextonum(x):
#     if x=='Female':
#         return 1
#     else:
#         return 0


# # print(tips)
# tips['newsex']=tips['sex'].apply(sextonum)
# print(tips)

# def test1(x):
#     print(x)
#     print('**')

tips10 = tips.sample(10, random_state=42)
# print(tips10)
# tips10['total_bill'].apply(test1)
# tips10.apply(test1)
# g1 = tips10.groupby('sex')
# for g in g1:
#     print(g)
# g1.apply(test1)

# g2 = tips10.groupby(['sex', 'smoker'])
# g2.apply(test1)

# 성별별 식대의 큰 금액 2개 추출
g3 = tips10.groupby('sex')

def getbill2(x):
    return x.sort_values(by='total_bill', ascending=False)[:2]

bill2 = g3.apply(getbill2)
print(bill2)