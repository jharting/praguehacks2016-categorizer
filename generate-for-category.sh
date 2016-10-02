#!/bin/bash
# $1 category

if [ -z "$1" ]; then
    echo "No category argument supplied!"
    exit 1;
fi

if [ -z "$2" ]; then
    echo "No features file argument supplied!"
    exit 1;
fi

cat input/* | ./generate-y.sh ${1} > ${1}-y.csv || exit 1
bash generate-x.sh ${1}-y.csv $2 > ${1}-x.csv || exit 1
cat ${1}-x.csv | wc -l
cat ${1}-y.csv | wc -l
cat ${1}-y.csv | grep ",1" | wc -l
