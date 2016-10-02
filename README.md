# Categorizer (a PragueHacks 2016 project)

Simple classification engine for government/municipality documents built with [TensorFlow](https://github.com/tensorflow/tensorflow) Documents are tagged based on occurrence of certain words and other characteristics of a document.

This project is a prototype for
* [mapasamospravy.cz](http://mapasamospravy.cz/)
* [edesky.cz](https://edesky.cz/)

## Setup

Requirements:

* bash
* python 2.7
* numpy
* tensorflow 0.10.0 (does not work with 0.11.0rc0 due to https://github.com/tensorflow/tensorflow/issues/4715)

## Run

Prepare data:

1. copy tagged content files to ./input
1. copy feature vector to features.csv
1. ```export CATS=`cat cats.txt```
1. `bash generate-all.sh features.csv $CATS`

Train DNN

1. `python train.py $CATS`

Run classification on new data

1. `python predict.py features.csv $CATS output.csv`
