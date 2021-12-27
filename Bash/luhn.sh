#!/usr/bin/env bash
x=$(echo "${1// /}" | sed 's/[$|£]/f/g' | rev)
len=${#x}
t=0; i=1

if [ $len -lt 2 ] || [[ $x =~ [^0-9] ]]; then echo "false"; exit; fi

until ((i>=len && t>=len)); do
nondouble=${x:$t:1}
predouble=${x:$i:1}
((double=2*predouble))
if [ $double -gt 9 ]; then ((double=double-9)); fi
((summation+=double+nondouble)); ((i+=2)); ((t+=2)); done

if ((0==summation%10)); then echo "true"; else echo "false"; fi
