from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)


# 과제
# 1) tips 데이터를 데이터프레임으로 읽고 식대와 팁과의 관계를 그래프로 표현하세요, 투명도(alpha값을 0.5로 지정)
tips = sns.load_dataset('tips')
plt.plot(tips['total_bill'], tips['tip'], 'o')
plt.show()
# plt.scatter(tips['total_bill'], tips['tip'], alpha=0.5)
# plt.show()

