import tensorflow as tf 
with tf.device('/gpu:0'):
    x1 = tf.constant(5)
    x2 = tf.constant(6)
    result = tf.multiply(x1, x2)

# sess = tf.Session()
# print(sess.run(result))
# sess.close()

with tf.Session() as sess:
    # print(sess.run(result))
    output = sess.run(result)
print(output)