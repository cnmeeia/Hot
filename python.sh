#!/bin/bash

for file in $(find /root/Hot/ -type f -name *.py)
do
 python3 $file 
done