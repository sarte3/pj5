import tensorflow as tf
import numpy as np

# data = np.loadtxt('data/iris1.csv', skiprows=1, delimiter=',')
# # print(data)
# # print(data.shape)
# xdata = data[:, :4]
# ydata = data[:, 4:]
# # print(xdata)
# # print(ydata)
#
# x = tf.placeholder(tf.float32, [150, 4])
# y = tf.placeholder(tf.float32, [150, 3])
# op1 = tf.argmax(y, 1)
# with tf.Session() as sess:
#     print(sess.run(op1, feed_dict={y: ydata}))

# data = np.loadtxt('data/iris2.csv', delimiter=',', skiprows=1)
# print(data.shape)
# xdata = data[:, :4]
# ydata = data[:, 4:]
# print(ydata.shape)
#
# y = tf.placeholder(tf.int32, [150, 1])
# y = tf.placeholder(tf.int32, [None, 1])
# onehot = tf.one_hot(y, 3)
# onehot2 = tf.reshape(onehot, [-1, 3])
# with tf.Session() as sess:
#     # print(sess.run(onehot, feed_dict={y: ydata}))
#     # print(sess.run(onehot2, feed_dict={y: ydata}))
#     # 새로운 데이터 입력
#     print(sess.run(onehot2, feed_dict={y: [[0], [2]]}))

from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
data = input_data.read_data_sets('../mnist/data/', one_hot=True)
print(data.train)  # 학습용 데이터
print(data.test)  # 검증용 데이터
# print('학습용 데이터 갯수', data.train.num_examples)
# print('학습용 데이터의 첫 번째 실제 데이터', data.train.labels[0:1])
# print('학습용 데이터의 실제 이미지', data.train.images[0:1])
# print('학습용 데이터의 실제 이미지', data.train.images[0:1].shape)
# plt.imshow(data.train.images[0:1].reshape(28, 28), cmap='Greys', interpolation='nearest')
# plt.show()
print('학습용 데이터의 50000번째 실제 데이터', data.train.labels[49999:50000])
print('학습용 데이터의 실제 이미지', data.train.images[49999:50000])
print('학습용 데이터의 실제 이미지', data.train.images[49999:50000].shape)
plt.imshow(data.train.images[49999:50000].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()

