import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 과제) 팁스데이터 이용해서 요일별식대의 합을 그래프로 출력
tips = sns.load_dataset('tips')
# tips.info()

tips = tips.groupby('day')['total_bill'].sum()

plt.plot(tips)
plt.title('요일별 식대의 합')
plt.show()
