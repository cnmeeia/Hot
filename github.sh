#!/bin/bash

for file in $(find /home/runner/work/Hot/Hot/ -type f -name *.py)
do
 python3 $file 
done
