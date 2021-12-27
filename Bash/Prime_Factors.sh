#!/usr/bin/env bash

declare -i factorize=$1
declare -i i=2

while [[ $factorize -ne 1 ]]
    do  
        for x in ${prime_factor[@]}
            do
                if [[ ${#prime_factor[@]} -lt 1 ]]; then break; fi
                if [[ $i -ne $x ]] && [[ $((i%x)) == 0 ]]; then ((i+=1))
                else break; fi
            done
        if [[ $((factorize%i)) -eq 0 ]]; then prime_factor+=("$i") && ((factorize=factorize/i))
        else ((i+=1)); fi
    done

echo "${prime_factor[@]}"