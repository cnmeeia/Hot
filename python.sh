#!/bin/bash

find . -type f -name "*.py" | xargs -I {} -P 4 bash -c 'python3 "{}"'{}
do
 python3 $file 
done
