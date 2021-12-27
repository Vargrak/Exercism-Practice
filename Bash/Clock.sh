#!/usr/bin/env bash
Inp_H=$1
Inp_M=$2
Inp_Op=$3
Inp_Var=$4
Inp_Nums=$( echo "$1$2$4")

Pre_Process()
{
((Inp_M=$Inp_M$Inp_Op$Inp_Var))
}

Clock()
{
((hours=$Inp_H%24))
((minutes=$Inp_M%60))
((hours+=$Inp_M/60))

while [[ $minutes -lt 0 ]]
    do
        ((minutes+=60)) && ((hours-=1))
    done
while [[ $minutes -gt 59 ]]
    do
        ((minutes-=60)) && ((hours+=1))
    done
while [[ $hours -lt 0 ]]
    do
        ((hours+=24))
    done
while [[ $hours -gt 23 ]]
    do
        ((hours-=24))
    done
hours=$(printf "%02d" $hours)
minutes=$(printf "%02d" $minutes)
}

Exception()
{
echo "invalid arguments" && exit 1
}

if [[ "$#" -ne 2 ]] && [[ "$#" -ne 4 ]]; then Exception; fi
if [[ -n $3 ]] && [[ ! $3 =~ [-+] ]]; then Exception; fi
if [[ ! $Inp_Nums =~ [0-9] ]] || [[ $Inp_Nums =~ [:alpha:] ]]; then Exception; fi

Pre_Process $@
Clock $@
echo "$hours:$minutes"