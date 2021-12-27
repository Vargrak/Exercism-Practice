#!/usr/bin/env bash
Type=$1; Side1=$2; Side2=$3; Side3=$4

if [[ $(echo "$Side1 > ($Side2 + $Side3) || $Side2 > ($Side1 + $Side3) || $Side3 > ($Side1 + $Side2) || $Side1 == 0 || $Side2 == 0 || $Side3 == 0" | bc) -eq 1 ]]; then echo "false" && exit 0; fi

RA=$(echo "$Side1 == $Side2" | bc)
RB=$(echo "$Side2 == $Side3" | bc)
RC=$(echo "$Side3 == $Side1" | bc)

case $Type in
    equilateral) ((3==(RA+RB+RC))) && echo "true" || echo "false" ;;
    isosceles) ((1<=(RA+RB+RC))) && echo "true" || echo "false" ;;
    scalene) ((0==(RA+RB+RC))) && echo "true" || echo "false" ;;
esac