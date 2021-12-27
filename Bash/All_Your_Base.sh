#!/usr/bin/env bash
Starting_Base=$1; Input="$2"; Output_Base=$3
read -ra Num_Array <<< "$Input"

To_Decimal()
{
    NX=${#Num_Array[@]}
    for Int in "${Num_Array[@]}"
        do
            if [[ $Int -lt 0 ]] || ((Int>=Starting_Base)); then echo "Invalid Input" && exit 1; fi
            ((NX--))
            ((Dec_Total+=Summation=Int*(Starting_Base**NX)))
            Dec_Array+=("$Summation")
        done
}

To_Output()
{
    Quotient="$Dec_Total"
    if ((Output_Base==0)); then return; fi
    if ((Quotient==0)); then echo "" && exit 0; fi
    while [[ $Tick -ne 1 ]]
        do
            SQuot=$Quotient
            ((Quotient=Quotient/Output_Base))
            ((Remainder=SQuot%Output_Base))
            Out_Array+=("$Remainder")
            if ((Quotient==0)); then Tick=1; fi
        done

}

if ((Starting_Base<2)) || ((Output_Base<2)) || ((Starting_Base==Output_Base)); then echo "Invalid Input" && exit 1; fi
To_Decimal "$@"
To_Output "$@"

Leng=${#Out_Array[@]}
((Leng--))
for ((i=Leng; i>=0; i--))
    do
        echo -n "${Out_Array[$i]}" && if [[ $i -ne 0 ]]; then echo -n " "; fi
    done
