#!/usr/bin/env bash
len=${#1}
str=${1,,}
for i in {a..z}
do
letlen=${str//$i/}
if ((len<=${#letlen})); then ((no+=1))
fi
done

if ((no>0)); then echo "false"
else echo "true"
fi
