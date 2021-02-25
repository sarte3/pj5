import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 과제
# 1. 팁의 히스토그램과 상자그림을 하나의 화면에 나타내세요
tips = sns.load_dataset('tips')

fig = plt.figure(figsize=[15,5])
g1 = fig.add_subplot(1, 2, 1) 
g2 = fig.add_subplot(1, 2, 2) 

g1.hist(tips['tip'])
g2.boxplot(tips['tip'], labels=['tip'])

g1.set_title('팁의 히스토그램')
g2.set_title('팁의 상자그림')

fig.tight_layout()
plt.show()