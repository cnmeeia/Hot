#!/bin/bash

for file in $(find ./ -type f -name *.py)
do
 python3 $file 
done
