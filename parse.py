import numpy
import math
from numpy import *

def readCsv(filename):
    file = open(filename)

    data = []
    featureCount = -1

    for line in file.readlines():
        items = line.strip().split(',')
        items = map(int, items)
        if len(items) == 0:
            print "Empty line"
            continue

        if featureCount == -1:
            featureCount = len(items)
        if featureCount != len(items):
            raise NameError('inconsistent feature counts! expected ' + str(featureCount) + ' was ' + str(len(items)))
        data.append(items)

    return mat(data)

def split(data, testRatio=0.2):
    splitIndex = int(shape(data)[0] * (1 - testRatio)) - 1
    return numpy.split(data, [splitIndex], axis=0)

def splitLabels(data):
    return data[:, :-1], data[:, -1:]

def shuffle(data):
    numpy.random.shuffle(data)
    return data

def grab(data, count):
    temp = data.copy()
    numpy.random.shuffle(temp)
    return numpy.split(temp, [count], axis=0)[0]

def nominalToVector(y, cats):
    dims = shape(y)
    if (dims[1] != 1):
        raise NameError('Unexpected shape ' + dims)
    result = zeros((dims[0], cats))
    for i in range(dims[0]):
        val = y.item((i, 0))
        result[i][val] = 1
    return result

def parse(filename, cats):
    data = readCsv('test.csv')
    data = shuffle(data)

    train, test = split(data)
    trainX, trainY = splitLabels(train)
    testX, testY = splitLabels(test)

    return trainX, trainY, testX, testY
