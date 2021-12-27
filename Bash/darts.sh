#!/usr/bin/env bash
run()
{
presquared=$(echo "((($x-0)^2)+(($y-0)^2))" | bc)
out=$( echo "scale=3; sqrt($presquared)" | bc )

if [ $(echo "if (${out} <= 1) 1 else 0" | bc) -eq 1 ]; then echo "10"
elif [ $(echo "if (${out} <= 5) 1 else 0" | bc) -eq 1 ]; then echo "5"
elif [ $(echo "if (${out} <= 10) 1 else 0" | bc) -eq 1 ]; then echo "1"
elif [ $(echo "if (${out} > 10) 1 else 0" | bc) -eq 1 ]; then echo "0"
fi
}

x=$1; y=$2
regex="^[-*0-9].*"
if [[ $1 =~ $regex ]] && [[ $2 =~ $regex ]]; then run
else echo "Darts.sh Usage: <x> <y>"; exit 1; fi
