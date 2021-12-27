#!/usr/bin/env bash

str=$1; leng=${#str}
As=0; Cs=0; Gs=0; Ts=0
for (( i=0; i<leng; i++ )); do
    case "${str:$i:1}" in
        [A]) ((As+=1)) ;;
        [C]) ((Cs+=1)) ;;
        [G]) ((Gs+=1)) ;;
        [T]) ((Ts+=1)) ;;
        *) echo "Invalid nucleotide in strand"; exit 1 ;;
    esac
done
echo -e "A: $As\nC: $Cs\nG: $Gs\nT: $Ts"