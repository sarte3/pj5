import pandas as pd
import seaborn as sns
# 과제) tips 데이터를 이용하여 요일을 행 인덱스, 성별을 열인덱스로 하여 식사 금액의 합을 출력하세요
tips = sns.load_dataset('tips')
# tips.info()

tips = tips.pivot_table(index='day', columns='sex', values='total_bill', aggfunc='sum');
print(tips)
