import tensorflow as tf
import numpy as np

data = np.loadtxt('data/iris1.csv', delimiter=',', skiprows=1)
np.random.shuffle(data)
trainx, trainy = data[:105, :4], data[:105, 4:]
testx, testy = data[105:, :4], data[105:, 4:]

x = tf.placeholder(tf.float32, [None, 4])
y = tf.placeholder(tf.float32, [None, 3])
w = tf.Variable(tf.random_normal([4, 3]))
b = tf.Variable(tf.random_normal([3]))
logits = tf.matmul(x, w) + b
h = tf.nn.softmax(logits)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        sess.run(train, feed_dict={x: trainx, y: trainy})
        if i % 1000 == 0:
            print(sess.run(cost, feed_dict={x: trainx, y: trainy}))
    pred = sess.run(h, feed_dict={x: testx})
    corr = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    acc = tf.reduce_mean(tf.cast(corr, tf.float32))
    print('정답률 =', sess.run(acc, feed_dict={x: testx, y: testy}))
