#!/usr/bin/env bash

for i in $1 $2; do
value=0
case ${i^^} in 
    BLACK) ((value=0)) ;;
    BROWN) ((value=1)) ;;
    RED) ((value=2)) ;;
    ORANGE) ((value=3)) ;;
    YELLOW) ((value=4)) ;;
    GREEN) ((value=5)) ;;
    BLUE) ((value=6)) ;;
    VIOLET) ((value=7)) ;;
    GREY) ((value=8)) ;;
    WHITE) ((value=9)) ;;
    *) echo "invalid color"; exit 1 ;;
esac
res+=$value
done

echo "$res"
