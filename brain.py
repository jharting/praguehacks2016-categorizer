import tensorflow as tf
from numpy import *
import parse
import numpy as np




x = tf.contrib.learn.datasets.base.load_csv_without_header(filename='data-x.csv', target_dtype=np.float32, features_dtype=np.float32)
old_x = concatenate((mat(x.data), mat(x.target).T),axis=1)
x = old_x[:,1:]

y = tf.contrib.learn.datasets.base.load_csv_without_header(filename='data-y.csv', target_dtype=np.int32, features_dtype=np.int32)
y = mat(y.target).T

if shape(x)[0] != shape(y)[0]:
    raise NameError('matrices do not match!')

data = concatenate((x, y),axis=1)

data = parse.shuffle(data)

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

#new_samples = np.array([[0,1,0,0,4,5]], dtype=float32)
#y = classifier.predict(new_samples)
#print('Predictions: {}'.format(str(y)))

for i in range(30):
    sample = parse.grab(old_x, 1)
    g = int(sample.item((0,0)))
    y = classifier.predict(sample[:,1:])
    print('Guessing {} to be {}'.format(str(g), str(y)))
