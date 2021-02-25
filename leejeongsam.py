import numpy as np
import tensorflow as tf
import math
data = np.loadtxt('data/water.csv', skiprows=1, delimiter=',')
xdata = data[:, 1:-1]
ydata = data[:, -1:]
x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])
w = tf.Variable(tf.random_normal([2, 1]))
b = tf.Variable(tf.random_normal([1]))
h = tf.matmul(x, w) + b
cost = tf.reduce_mean(tf.square(y-h))
train = tf.train.GradientDescentOptimizer(0.000000000035).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5001):
        sess.run(train, feed_dict={x: xdata, y: ydata})
        # if i % 1000 == 0:
            # print(sess.run([cost, w, b], feed_dict={x: xdata, y: ydata}))
    print('최종 cost', sess.run(cost, feed_dict={x: xdata, y: ydata}))
    print('최종 기울기', sess.run(w))
    print('최종 절편', sess.run(b))
    print('예측 as시간', sess.run(h, feed_dict={x: [[80000, 270000]]}))
    print('필요한 기사 수', math.ceil(sess.run(h/160, feed_dict={x: [[80000, 270000]]})))