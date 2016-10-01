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

cat input/* | ./generate-y.sh ${1} > data-y.csv || exit 1
bash generate-x.sh data-y.csv $2 > data-x.csv || exit 1
cat data-x.csv | wc -l
cat data-y.csv | wc -l
cat data-y.csv | grep ",1" | wc -l
