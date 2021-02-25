import numpy as np
import tensorflow as tf
data = np.loadtxt('data/water.csv', skiprows=1, delimiter=',')
# print(data)
xdata = data[:, 1:-1]
ydata = data[:, -1:]
# print(xdata)
# print(ydata)
x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])
w = tf.Variable(tf.random_normal([2, 1]))
b = tf.Variable(tf.random_normal([1]))
h = tf.matmul(x, w) + b
cost = tf.reduce_mean(tf.square(y-h))
train = tf.train.GradientDescentOptimizer(0.00000000003).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        sess.run(train, feed_dict={x: xdata, y: ydata})
        if i % 1000 == 0:
            print(sess.run(cost, feed_dict={x: xdata, y: ydata}))
    print('예측 as시간', sess.run(h, feed_dict={x: [[70000, 230000]]}))
    ㅂ