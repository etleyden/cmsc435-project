#!/bin/bash

for file in unlabelled_features/*; do
    python normalizeandlabel.py $file features.csv
    filename=$(basename "$file")
    mv normalized_labeled_data.csv "labelled_features/$filename"
done