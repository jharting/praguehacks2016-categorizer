import tensorflow as tf
from numpy import *

trainX = mat([[1,1], [0,0]])
trainY = [1,0]

feature_columns = [tf.contrib.layers.real_valued_column("", dimension=2)]
classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10])

classifier.fit(x=trainX, y=trainY, steps=2000)
