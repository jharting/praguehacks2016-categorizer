import tensorflow as tf
from numpy import *
import parse
import numpy as np




data = tf.contrib.learn.datasets.base.load_csv_without_header(filename='test.csv', target_dtype=np.int, features_dtype=np.int)
data = concatenate((mat(data.data), mat(data.target).T),axis=1)

train, test = parse.split(data)
trainX, trainY = parse.splitLabels(train)
testX, testY = parse.splitLabels(test)

categoryCount = 2
featureCount = shape(trainX)[1]

print 'category count ' + str(categoryCount)
print 'feature count ' + str(featureCount)
print 'training set ' + str(shape(trainX)[0])
print 'testing set ' + str(shape(testX)[0])


feature_columns = [tf.contrib.layers.real_valued_column("", dimension=featureCount)]

classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10, 30, 10],
                                            n_classes=categoryCount,
                                            model_dir="/tmp/iris_model")

print 'Fitting start'
classifier.fit(x=trainX, y=trainY, steps=2000)
print 'Fitting done'

accuracy_score = classifier.evaluate(x=testX, y=testY)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))

new_samples = np.array([[0,1,2,3,4,5]], dtype=float)
y = classifier.predict(new_samples)
print('Predictions: {}'.format(str(y)))
