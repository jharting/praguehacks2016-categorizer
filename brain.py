import tensorflow as tf
from numpy import *
import parse

categoryCount = 2
train, testX, testY = parse.parse('test.csv', categoryCount)
featureCount = shape(train)[1] - 1

print 'category count ' + str(categoryCount)
print 'feature count ' + str(featureCount)
print 'training set ' + str(shape(train)[0])
print 'testing set ' + str(shape(testX)[0])


# placeholder for input value
x = tf.placeholder(tf.float32, [None, featureCount])

# weights and biases
# Variable - mutable tensor

W = tf.Variable(tf.zeros([featureCount, categoryCount]))
b = tf.Variable(tf.zeros([categoryCount]))


# Model description
# first multiply our input with weights
# then add bias
# then run softmax
y = tf.nn.softmax(tf.matmul(x, W) + b)

# training

# cross-entropy
y_ = tf.placeholder(tf.float32, [None, categoryCount])

# numerically unstable
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# cost function - we're using cross_entropy here
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# define init operation (does not run it yet)
init = tf.initialize_all_variables()

# run init in session
sess = tf.Session()
sess.run(init)

# run this 1000 times
# each time grab 100 random images

print "learning"

for i in range(1000):
  batch_xs, batch_ys = parse.grab(train, 2, categoryCount)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

print "learning done"

# evaluating model

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print "accuracy: " + str(sess.run(accuracy, feed_dict={x: testX, y_: testY}))


# use the model
sx, sy = parse.grab(train, 1, categoryCount)
#model = sess.run(W)
print "shh it's " + str(argmax(sy))
res = argmax(mat(sx) * mat(sess.run(W)) + mat(sess.run(b)))
print "predicting: " + str(res)
