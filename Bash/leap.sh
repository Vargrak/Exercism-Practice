#!/usr/bin/env bash
x=${1//[0-9]/}

if [ -z $1 ] || [ 0 -ne ${#x} ] || [ 1 != $# ]; then echo "Usage: leap.sh <year>"; exit 1; fi

if [ 0 -eq $(($1%4)) ] && [ 0 -ne $(($1%100)) ]; then echo "true"
elif [ 0 -eq $(($1%400)) ]; then echo "true"
else echo "false"
fi
