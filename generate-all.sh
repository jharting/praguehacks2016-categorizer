#!/bin/bash
# $1 features file

if [ -z "$1" ]; then
    echo "No features file argument supplied!"
    exit 1;
fi

if [ -z "$1" ]; then
    echo "No category list supplied!"
    exit 1;
fi

for i in $(echo $2 | sed "s/,/ /g"); do
    echo "Generating learning vectors for category: $i"
    time bash "generate-for-category.sh" $i $1
done
