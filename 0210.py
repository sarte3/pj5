import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 한글처리
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 과제) r 에서 car 데이터를 가져와 세로로 읽어 출력, 그래프로 그리시오.
data = np.loadtxt('data/cars.csv', delimiter=',', skiprows=1, unpack=True)
print(data)
plt.plot(data[0,:], data[1,:])
plt.xlabel('speed')
plt.ylabel('dist')
plt.show()