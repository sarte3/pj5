import tensorflow as tf
import numpy as np
# a = tf.constant(120, name='aa')
# b = tf.constant(5, name='b')
# c = tf.constant(100)
# print(a)
# print(b)
# print(c)
# v = tf.Variable(0, name='v')
# op1 = a + b + c
# op2 = tf.assign(v, op1)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(op2))
#     result = sess.run([a, b, c, op2])
#     print(type(result), type(result[0]))

# dan = tf.placeholder(tf.int32)
# i = tf.placeholder(tf.int32)
# op1 = dan*i
# with tf.Session() as sess:
#     # print(sess.run(op1, feed_dict={dan: 5, i: [1, 2, 3, 4, 5, 6, 7, 8, 9]}))
#     result = sess.run([dan, i, op1], feed_dict={dan: 5, i: [1, 2, 3, 4, 5, 6, 7, 8, 9]})
#     print(result)
#     print(result[0], result[1], result[2])
#
# for j in range(len(result[1])):
#     print('{}*{}={}'.format(result[0], result[1][j], result[2][j]))

# a = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# b = tf.constant([[[1, 1], [2, 2]], [[3, 3], [4, 4]]])
# with tf.Session() as sess:
#     print(sess.run(tf.reshape(a, (3, 4))))
#     print(sess.run(tf.reshape(a, (3, 2, -1))))
#     print(sess.run(tf.reshape(b, (-1, 4))))

# a = tf.constant([[1., 2.]])
# b = tf.constant([[3.], [4.]])
# # print(a, a.get_shape())
# # print(b)
# # 행렬곱 matmul()
# op1 = tf.matmul(a, b)
# with tf.Session() as sess:
#     print(sess.run(op1))

# a = tf.constant([[1, 2, 3], [4, 5, 6]])
# b = tf.constant([1, 0, 1])
# print(a.get_shape()) # (2, 3)
# print(b.get_shape()) # (3,)
# bb = tf.reshape(b, (3, -1))
# op1 = tf.matmul(a, bb) # (2, 3)X(3, 1) = (2, 1)
#
# with tf.Session() as sess:
#     print(sess.run(bb))
#     print(sess.run(op1))

# a = tf.constant([1, 2, 3], dtype=tf.float32)
# print(a)
# a = tf.cast(a, tf.int64)
# print(a)
# x = tf.constant([1., 2., 3.])
# print(x)
# y = tf.constant([True, False, True, False])
# print(y)
# with tf.Session() as sess:
#     print(sess.run(tf.cast(x, tf.int32)))
#     print(sess.run(tf.cast(y, tf.int32)))
#     print(sess.run(tf.reduce_mean(tf.cast(y, tf.int32))))
#     print(sess.run(tf.reduce_mean(tf.cast(y, tf.float32))))

# 상수 생성
# z1 = tf.zeros([3, 4, 5])
# z2 = tf.zeros_like([3, 4, 5])
# f1 = tf.fill([2, 3], 7)
# f2 = tf.constant(7, shape=[2, 3])
# with tf.Session() as sess:
#     print(sess.run(z1))
#     print('-'*30)
#     print(sess.run(z2))
#     print('-' * 30)
#     print(sess.run(f1))
#     print('-' * 30)
#     print(sess.run(f2))
# xdata = np.random.randn(5, 10)
# print(xdata)
# wdata = np.random.randn(10, 1)
# x = tf.placeholder(tf.float32, shape=(5, 10))
# w = tf.placeholder(tf.float32, shape=(10, 1))
# b = tf.fill((5, 1), -1.)
# y = tf.matmul(x, w)+b
# with tf.Session() as sess:
#     print(sess.run(y, feed_dict={x: xdata, w: wdata}))

# tf.argmax() : 가장 큰 값을 찾아 인덱스를 반환
# a = tf.constant([10, 100, 1, 1000])
# b = tf.constant([[10, 100, 1], [11, 21, 31], [0, 80, 50]])
# with tf.Session() as sess:
#     # print('인덱스 갯수(차원)', sess.run(tf.rank(a)))
#     # print('가장 큰 값 위치', sess.run(tf.argmax(a)))
#     # print('가장 작은 값 위치', sess.run(tf.argmin(a)))
#     print('인덱스 갯수(차원)', sess.run(tf.rank(b)))
#     print(sess.run(b))
#     print('가장 큰 값 위치: 열방향', sess.run(tf.argmax(b)))
#     print('가장 큰 값 위치: 열방향', sess.run(tf.argmax(b, 0)))
#     print('가장 큰 값 위치: 행방향', sess.run(tf.argmax(b, 1)))
#
# # 행방향으로 가장 큰 값의 위치 출력
# a = tf.constant([[5, 10, 17], [4, 50, 6]])
# with tf.Session() as sess:
#     print(sess.run(a))
#     print('가장 큰 값 위치(행방향)', sess.run(tf.argmax(a, 1)))

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([0, 1, 2, 0, 2, 1, 1, 2, 2, 0])
# print(a)
x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.int32)
# 원핫 : 사람이 이해할 수 있는 데이터를 컴에게 입력시키는 방법
onehotx = tf.one_hot(x, 10)
onehotx2 = tf.reshape(onehotx, shape=[-1])
onehoty = tf.one_hot(y, 3)
argmaxy = tf.argmax(onehoty, 1)
with tf.Session() as sess:
    # print(sess.run(x, feed_dict={x: a}))
    print('x=\n', sess.run(onehotx, feed_dict={x: a}))
    print('x=\n', sess.run(onehotx2, feed_dict={x: a}))
    print('원핫으로 y=\n', sess.run(onehoty, feed_dict={y: b}))
    print('원래값으로 y=\n', sess.run(argmaxy, feed_dict={y: b}))


