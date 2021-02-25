import tensorflow as tf
# 과제) 텐서플로를 활용하여 실행시 값을 입력받아 해당 구구단을 출력하세요
num = input('정수를 입력하세요')
x = tf.placeholder(tf.int32)
y = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9])
xy = tf.multiply(x, y)
with tf.Session() as sess:
    print(sess.run(xy, feed_dict={x: num}))