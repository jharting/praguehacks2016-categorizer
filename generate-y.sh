#!/bin/bash
# bash prepy.sh category

if [ -z "$1" ]; then
    echo "No category argument supplied!"
    exit 1;
fi

TEMP=`grep "^###.*#" | sed -e "s/###\(.*\)#/\1/g" | sed -e "s/:/,/g"`
for i in $TEMP; do
    if [[ $i == *"$1"* ]]; then
        echo $i | sed -e "s/\([0-9]*\),.*$/\1,1/"
    else
        echo $i | sed -e "s/\([0-9]*\),.*$/\1,0/"
    fi
done
