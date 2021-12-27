#!/usr/bin/env bash
Input=$1; i=0
if [[ $Input -lt 1 ]]; then echo "Error: Only positive numbers are allowed" && exit 1; fi
until [[ $Input == 1 ]]
    do
        ((i++))
        if [[ $((Input%2)) == 0 ]]; then ((Input=Input/2))
        else ((Input=(Input*3)+1)); fi
    done

echo "$i"