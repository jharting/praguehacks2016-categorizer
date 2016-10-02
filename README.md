1) copy tagged content files to ./input
2) export CATS=`cat cats.txt`
3) bash generate-all.sh features.csv $CATS
4) python train.py $CATS
5) python predict.py doprava-x.csv $CATS output.csv
