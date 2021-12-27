#!/usr/bin/env bash
t=0; z=0; zeroed=0

for i in $1 $2 $3; do
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

((t+=1))
if [ $t == 3 ]; then for (( x = $value; x > 0; x-- )); do 
zeros+=$(echo "0"); done
else sigval+=$value; fi
done
if [[ $sigval =~ ^(0) ]]; then sigval=${sigval#0}; fi

valout=$( echo "$sigval$zeros" )

until [ $zeroed -eq 1 ] || ((z==5)); do
test=$( echo "$valout" | rev )
if [[ $test =~ ^(000) ]]; then valout=${valout%000} && ((z+=1))
else zeroed=1; fi
done

case $z in 
    0) mod="ohms" ;;
    1) mod="kiloohms" ;;
    2) mod="megaohms" ;;
    3) mod="gigaohms" ;;
esac
echo "$valout $mod"
