import tensorflow as tf
import pandas as pd
import numpy as np
# 과제) iris1.csv 데이터를 읽어 다음을 진행하시오
# 1) 앞쪽 4개의 모든 열은 xdata, 3개의 열은 ydata에 넣으시오
data = np.loadtxt('data/iris1.csv', delimiter=',', skiprows=1)
xdata = np.array(data[:, 0:4])
ydata = np.array(data[:, 4:7])
# 2) 실행 시에 x에 xdata, y에 ydata 값을 넣어서
# y의 값을 원래의 값으로 복원하여 출력하시오
x = tf.placeholder(tf.float32, [150, 4])
y = tf.placeholder(tf.float32, [150, 3])
argmaxy = tf.argmax(y, 1)
with tf.Session() as sess:
    sess.run(x, feed_dict={x: xdata})
    print(sess.run(argmaxy, feed_dict={y: ydata}))
