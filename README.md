# Categorizer (a PragueHacks 2016 project)

Simple classification engine for government/municipality documents built with [TensorFlow](https://github.com/tensorflow/tensorflow)

Prepare data:

1. copy tagged content files to ./input
1. copy feature vector to features.csv
1. ```export CATS=`cat cats.txt```
1. `bash generate-all.sh features.csv $CATS`

Train DNN

1. `python train.py $CATS`

Run classification on new data

1. `python predict.py features.csv $CATS output.csv`
