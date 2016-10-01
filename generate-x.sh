#!/bin/bash
# $1 - y file
# $2 - features file

if [ -z "$1" ]; then
    echo "No y-data argument supplied!"
    exit 1;
fi

if [ -z "$2" ]; then
    echo "No features file argument supplied!"
    exit 1;
fi

for i in `cat $1 | cut -d ',' -f1`; do
     grep "^$i," $2
done
