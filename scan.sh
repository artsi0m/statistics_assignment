#!/usr/bin/env sh

for fname in $(ls -1 stats*.jpg)
do
    num=$(echo $fname | sed -e 's/[^0-9]//g')
    tesseract -l rus $fname out_$num
done
    



