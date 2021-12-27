#!/usr/bin/env bash
set -o noglob
list=("$@")
t=0

for i in "$@"; do ((index++)); done

for (( i=index; i > 0; i-- )); do
case $i in
    1) echo "And all for the want of a ${list[0]}." ;;

    *) echo -n "For want of a ${list[$t]} "; ((t++)); echo "the ${list[$t]} was lost." ;;
esac; done
