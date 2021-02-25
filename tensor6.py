from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

# diabetes = load_diabetes()
# # print(diabetes.data.shape)
# # print(diabetes.target.shape)
# # print(diabetes.data[:3])
# # print(diabetes.target[:3])
# xdata = diabetes.data[:, 2]
# ydata = diabetes.target
# # print('xdata=', xdata)
# # print('ydata=', ydata)
#
# # plt.plot(xdata, ydata, 'o')
# # plt.show()
#
# w = 1.0
# b = 1.0
# print('xdata = ', xdata[:10])
# print('ydata = ', ydata[:10])
# h = xdata[0]*w+b
# print('예측값 h=', h)
# print('정답 ydata=', ydata[0])
# # w를 0.1 증가 --> h 값 변화
# winc = w + 0.1
# hinc = xdata[0] * winc + b
# # print('예측값 hinc =', hinc)
# # print('정답 ydata =', ydata[0])
# wrate = (hinc-h)/(winc-w)
# # # ((xdata[0]*winc+b)-(xdata[0]*w*b))/(winc-w)=
# # # ((xdata[0]*winc)-(xdata[0]*w))/(winc-w)=
# # # xdata[0]*(winc-w)/(winc-w)=xdata[0]
# # print('wrate =', wrate)  # data[0]
# # wnew = w + wrate
# # print('wnew =',wnew)
# #
# # # 경사하강법 : 모델이 데이터를 잘 표현할 수 있도록 기울기를 사용하여 모델을 조금씩 조정하는 알고리즘
# # # b 값을 0.1 증가시 예측값의 변화
# binc = b + 0.1
# hinc = xdata[0] * w + binc
# # print('절편값의 변화에 따른 예측값 hinc =', hinc)
# brate = (hinc - h)/(binc - b)
# # print('brate =', brate)
# # bnew = b + brate
# # print('bnew =', bnew)
#
# # 오차역전파 : 예측값과 정답의 차이를 이용하여 w와 b를 업데이트
# # 오차가 연이어 전파되는 모습
# # err = ydata[0] - h
# # wnew = w+wrate*err
# # bnew = b+brate*err
# # print('wnew =', wnew, 'bnew =', bnew)
# #
# # # 두 번째 샘플에 적용
# # h = xdata[1] * wnew + bnew
# # print('예측값=', h, '정답=', ydata[1])
# #
# # err = ydata[1] - h
# # wrate = xdata[1]
# # wnew = wnew+wrate*err
# # bnew = bnew+brate*err
# # print('wnew =', wnew, 'bnew =', bnew)
#
# for xi, yi in zip(xdata, ydata):
#     h = xi * w + b
#     err = yi - h
#     wrate = xi
#     w = w+wrate*err
#     b = b+1*err
#
# # print('w =', w, 'b =', b)
# # plt.plot(xdata, ydata, 'o')
# # left = -0.1 * w + b
# # right = 0.2 * w + b
# # plt.plot([-0.1, 0.2], [left, right])
# # plt.show()
#
# # 에포크(epoch) : 한 단위의 작업을 진행하는 것
# # 여러 에포크 반복
# for i in range(1000):
#     for xi, yi in zip(xdata, ydata):
#         h = xi * w + b
#         err = yi - h
#         wrate = xi
#         w = w + wrate * err
#         b = b + 1 * err
# print('w =', w, 'b =', b)
# plt.plot(xdata, ydata, 'o')
# left = -0.1 * w + b
# right = 0.2 * w + b
# plt.plot([-0.1, 0.2], [left, right])
# plt.show()

# x = tf.placeholder(tf.float32, [None])
# y = tf.placeholder(tf.float32, [None])
# w = tf.Variable(tf.random_uniform([1]))
# b = tf.Variable(tf.random_uniform([1]))
# h = x * w + b
# cost = tf.reduce_mean(tf.square(y-h))
# train = tf.train.GradientDescentOptimizer(0.65).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(2001):
#         sess.run(train, feed_dict={x: xdata, y: ydata})
#         if i % 100 == 0:
#             print(sess.run([cost, w, b], feed_dict={x: xdata, y: ydata}))
#
#     result = sess.run(h, feed_dict={x: [-0.1, 0.15]})
#     print(result)
#     print(sess.run([w, b]))
# plt.plot([-0.1, 0.15], result)
# plt.plot(xdata, ydata, 'o')
# plt.show()

# data = np.loadtxt('data/iris1.csv', delimiter=',', skiprows=1)
# # print(data)
# # print(data.shape)
# # 70% 데이터로 학습, 30% 데이터로 검증
# np.random.shuffle(data)
# trainx, trainy = data[:105, :4], data[:105, 4:]
# # print(trainx.shape) # 학습용 데이터
# # print(trainy.shape) # 학습용 데이터 정답
# testx, testy = data[105:, :4], data[105:, 4:]
# # print(testx.shape) # 검증용 데이터
# # print(testy.shape) # 검증용 데이터 정답
# # print(testy)
#
# x = tf.placeholder(tf.float32, [None, 4])
# y = tf.placeholder(tf.float32, [None, 3])
# w = tf.Variable(tf.random_normal([4, 3]))
# b = tf.Variable(tf.random_normal([3]))
# logits = tf.matmul(x, w) + b
# h = tf.nn.softmax(logits)
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
# train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     # 학습하기
#     for i in range(3001):
#         sess.run(train, feed_dict={x: trainx, y: trainy})
#         if i % 1000 == 0:
#             print(sess.run(cost, feed_dict={x: trainx, y: trainy}))
#     # print(sess.run([w, b]))
#     # 검증하기
#     pred = sess.run(h, feed_dict={x: testx})
#     corr = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
#     acc = tf.reduce_mean(tf.cast(corr, tf.float32))
#     print('정확도 =', sess.run(acc, feed_dict={x: testx, y: testy}))

# 70% 데이터로 학습, 30%의 데이터로 검증
data = np.loadtxt('data/wine.csv', delimiter=';', skiprows=1)
# print(data)
# print(data.shape)
np.random.shuffle(data)
trainx, trainy = data[:3429, :11], data[:3429, 11:]
testx, testy = data[3429:, :11], data[3429:, 11:]
print(trainx.shape)
print(trainy.shape)

x = tf.placeholder(tf.float32, [None, 11])
y = tf.placeholder(tf.int32, [None, 1])
onehot = tf.one_hot(y, 11) # 3차원
onehot2 = tf.reshape(onehot, [-1, 11]) # 2차원
w = tf.Variable(tf.random_normal([11, 11]))
b = tf.Variable(tf.random_normal([11]))
logits = tf.matmul(x, w) + b
h = tf.nn.softmax(logits)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=onehot2))
train = tf.train.GradientDescentOptimizer(0.0005).minimize(cost)

corr = tf.equal(tf.argmax(h, 1), tf.argmax(onehot2, 1))
acc = tf.reduce_mean(tf.cast(corr, tf.float32))

with tf.Session() as sess:
    # print(sess.run(y, feed_dict={y: trainy}))
    # print(sess.run(onehot, feed_dict={y: trainy}))
    # print(sess.run(onehot2, feed_dict={y: trainy}))
    sess.run(tf.global_variables_initializer())
    # 훈련하기
    for i in range(3001):
        sess.run(train, feed_dict={x: trainx, y: trainy})
        if i % 1000 == 0:
            print(sess.run(cost, feed_dict={x: trainx, y: trainy}))

    # 검증하기
    print('정확도 =', sess.run(acc, feed_dict={x: testx, y: testy}))