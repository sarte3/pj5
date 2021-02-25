import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

data = pd.read_csv('data/mpg.csv', header=None)
# # print(data)

data.columns=['mpg', 'cyl', 'displace', 'horsepower', 'weight', 'acc', 'modelyear', 'country', 'name']
# print(data)

# 원그래프
# s1 = data.groupby('country').size()
# print(s1, type(s1))
# s1.index = ['미국', '유럽', '일본']
# print(s1)
# plt.style.use('ggplot')
# plt.pie(s1, labels=s1.index, colors=['red', 'green', 'blue'], autopct='%.2f%%')
# plt.title('자동차 생산국', size=20)
# plt.show()

# a = 30
# b = 3.14
# print('{}','{}'.format(a, b))
# print('%s, %s'%(a, b))
# print('%i, %i'%(a, b))
# print('%f, %f'%(a, b))

# d1 = data[['weight', 'acc', 'modelyear', 'country', 'name']].head()
# print(d1)
# # d1.info()
# print(d1.sum())
# print(d1.mean())

data['cnt']=1
# print(data)
# df1 = data.groupby('country').sum()
# print(df1)
# df1.index=['미국', '유럽', '일본']
# plt.pie(df1['cnt'])
# plt.show()

# 히스토그램

# data = pd.read_csv('data/mpg.csv', header=None)
# print(data)

# data.columns=['mpg', 'cyl', 'displace', 'horsepower', 'weight', 'acc', 'modelyear', 'country', 'name']
# print(data)
# plt.hist(data['mpg'], bins=5, color='red')
# plt.title('연비의 히스토그램')
# plt.show()

# 연비의 상자그림
# plt.boxplot(data['mpg'])
# plt.boxplot(data['mpg'], vert=False)
# plt.show()
# 나라별 연비의 상자 그림
# print(data[data['country']==1])
# print(data[data['country']==2])
# print(data[data['country']==3])

# plt.boxplot([data[data['country']==1]['mpg'], data[data['country']==2]['mpg'], data[data['country']==3]['mpg']], labels=['미국', '유럽', '일본'])
# plt.show()

# 자동차 무게와 연비와의 관계 산점도
# plt.scatter(data['weight'], data['mpg'], s = data['cyl']*20, c = 'orange', alpha=0.5)
# plt.scatter(data['weight'], data['mpg'], c = data['cyl'])
# plt.scatter(data['weight'], data['mpg'], c = data['cnt'])
# plt.title('자동차무게와 연비의 산점도')
# plt.show()

tips = sns.load_dataset('tips')
def getSex(x):
    if x == 'Female':
        return 0
    else:
        return 1


# print(tips.head())
tips['sex2']=tips['sex'].apply(getSex)
print(tips)
plt.scatter(tips['total_bill'], tips['tip'], s=tips['size']*15, c=tips['sex2'])
plt.show()

# 과제
# 1. 팁의 히스토그램과 상자그림을 하나의 화면에 나타내세요