import tensorflow as tf
from numpy import *
import parse
import numpy as np
import common
import sys

def load_model(featureCount, category):
    return common.prepare_classifier("./" + category "-model", featureCount)

def run_model(data, category="categorizer"):
    model = load_model(shape(data)[1], category)
    y = model.predict(data)
    return y

def load_data(filename):
    x = tf.contrib.learn.datasets.base.load_csv_without_header(filename=filename, target_dtype=np.float32, features_dtype=np.float32)
    x = concatenate((mat(x.data), mat(x.target).T),axis=1)
    return x[:,1:], x[:,:1]

def run(data, ids, categories):
    result = ids
    for category in categories:
        y = run_model(data, category)
        result = concatenate((result, mat(y).T),axis=1)
    return result

def export(result, cats):
    output = ""
    feature_count = shape(result)[1]
    for i in range(shape(result)[0]):
        output += str(result.item(i, 0))
        output += ","
        categories = []
        for j in range(1, feature_count):
            item = result.item(i, j)
            if item > 0:
                categories.append(cats[j - 1])
        output += ":".join(categories)
        output += "\n"
    return output


if len(sys.argv) < 3:
    raise NameError("specify the input feature file and a list of categories (e.g. python train.py docs.csv doprava,prodej_pronajem)")

data,ids = load_data(sys.argv[1])
cats = sys.argv[2].split(',')
result = run(data, ids, cats).astype(int)

summary = np.sum(result, axis=0)
print "Total documents: " + str(shape(data)[0])
for i in range(len(cats)):
    print cats[i] + ": " + str(summary.item(0, i+1))

if len(sys.argv) > 3:
    print "exporting to: " + sys.argv[3]
    output = export(result, cats)
    f = open(sys.argv[3],'w')
    f.write(output)
    f.close()
