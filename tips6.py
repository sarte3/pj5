# 과제
# 1) tips데이터를 활용하여 흡연여부별 팁금액의 평균을 출력
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
# tips.info()
tips = tips.groupby('smoker')['tip'].mean()
print(tips)