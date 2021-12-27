#!/usr/bin/env bash
prime=()

for (( i=2; i <= $1; i++ )); do
nonprime=0
    for t in ${prime[*]}; do
        ((Y=($i%$t)))
        if [[ $Y == 0 ]]; then nonprime=1; fi
    done
    if [[ $nonprime -ne 1 ]]; then prime+=($i); fi
done
echo "${prime[@]}"
