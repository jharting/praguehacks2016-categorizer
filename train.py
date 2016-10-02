import tensorflow as tf
from numpy import *
import parse
import numpy as np
import common
import sys

def train(model="categorizer", file_x="data-x.csv", file_y="data-y.csv"):
    x = tf.contrib.learn.datasets.base.load_csv_without_header(filename=file_x, target_dtype=np.float32, features_dtype=np.float32)
    old_x = concatenate((mat(x.data), mat(x.target).T),axis=1)
    x = old_x[:,1:]

    y = tf.contrib.learn.datasets.base.load_csv_without_header(filename=file_y, target_dtype=np.int32, features_dtype=np.int32)
    y = mat(y.target).T

    if shape(x)[0] != shape(y)[0]:
        raise NameError('matrices do not match!')

    data = concatenate((x, y),axis=1)

    data = parse.shuffle(data)

    train, test = parse.split(data)
    trainX, trainY = parse.splitLabels(train)
    testX, testY = parse.splitLabels(test)

    featureCount = shape(trainX)[1]

    print 'feature count ' + str(featureCount)
    print 'training set ' + str(shape(trainX)[0])
    print 'testing set ' + str(shape(testX)[0])

    classifier = common.prepare_classifier("./" + model, featureCount)

    print 'Training start'
    classifier.fit(x=trainX, y=trainY, steps=2000)
    print 'Training done'

    accuracy_score = classifier.evaluate(x=testX, y=testY)["accuracy"]
    print('Accuracy: {0:f}'.format(accuracy_score))

    #for i in range(10):
    #    sample = parse.grab(old_x, 1)
    #    g = int(sample.item((0,0)))
    #    y = classifier.predict(sample[:,1:])
    #    print('Guessing {} to be {}'.format(str(g), str(y)))

def run(categories):
    for category in categories:
        train(category, category + "-x.csv", category + "-y.csv")
        print "Training of " + category + " done"
        print

if len(sys.argv) < 2:
    raise NameError("specify a list of categories (e.g. python train.py doprava,prodej_pronajem)")

cats = sys.argv[1].split(',')
run(cats)
