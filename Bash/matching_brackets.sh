#!/usr/bin/env bash
str=$1
swiggle=0; square=0; round=0

for (( i=0; i <= ${#str}; i++ )); do 
(((summation=($swiggle+$square+$round))))
case ${str:$i:1} in

    "{") ((swiggle+=1)) && ((slevel=summation+1)) ;;

    "[") ((square+=1)) && ((qlevel=summation+1)) ;;

    "(") ((round+=1)) && ((rlevel=summation+1)) ;;

    "}") if [[ $swiggle -gt 0 ]]; then ((swiggle--)); elif [[ $swiggle -eq 0 ]]; then err=1; fi 
        if [[ $summation -gt slevel ]]; then nesterr=1; fi ;;

    "]") if [[ $square -gt 0 ]]; then ((square--)); elif [[ $square -eq 0 ]]; then err=1; fi
        if [[ $summation -gt qlevel ]]; then nesterr=1; fi ;;

    ")") if [[ $round -gt 0 ]]; then ((round--)); elif [[ $round -eq 0 ]]; then err=1; fi
        if [[ $summation -gt rlevel ]]; then nesterr=1; fi ;;
esac
done

if [[ $summation -eq 0 ]] && [[ err -eq 0 ]] && [[ nesterr -eq 0 ]]; then echo "true"
else echo "false"; fi
