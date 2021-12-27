#!/usr/bin/env bash
Input_Num=$1

Invalid_Num()
{
    echo "Invalid number.  [1]NXX-NXX-XXXX N=2-9, X=0-9" && exit 1
}

Process_Num()
{
    Cleaned_Num=$( echo $Input_Num | tr -d [:space:] | tr -d [:punct:] )

    case ${#Cleaned_Num} in
        10) if [[ $Cleaned_Num =~ ^[2-9]..[2-9] ]]; then echo "$Cleaned_Num"
            else Invalid_Num; fi
            ;;
        11) if [[ $Cleaned_Num =~ ^1[2-9]..[2-9] ]]; then ( echo "$Cleaned_Num" | tr -d "^1" )
            else Invalid_Num; fi
            ;;
        *) Invalid_Num 
            ;;
    esac
}

Process_Num $@