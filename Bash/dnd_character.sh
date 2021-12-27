#!/usr/bin/env bash
mode=$1
inp=$2

moder()
{ case $inp in
    3)  ((result=-4)) ;;
    4 | 5) ((result=-3)) ;;
    6 | 7) ((result=-2)) ;;
    8 | 9) ((result=-1)) ;;
    10 | 11) ((result=0)) ;;
    12 | 13) ((result=1)) ;;
    14 | 15) ((result=2)) ;;
    16 | 17) ((result=3)) ;;
    18) ((result=4)) ;;
esac }

gener()
{
for i in strength dexterity constitution intelligence wisdom charisma; do
    Total=0
    X=0
    comp=0
    Sum=0
    
    while ((X<4))
    do
        Roll=$[ $RANDOM % 6 + 1 ]
        if [ $Roll -lt $comp ]; then comp=Roll; fi
        ((Sum+=Roll)) && ((X+=1))
    done
    
    ((Total=(Sum-comp)))
    
    if [ $i == constitution ]
        then inp=$Total
        moder
        ((hitpoints=10+result))
    fi
    
    echo "$i $Total"
done
echo "hitpoints $hitpoints"
}

if [ $mode == modifier ]; then moder; echo "$result"
elif [ $mode == generate ]; then gener
fi
