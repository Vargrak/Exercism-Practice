#!/usr/bin/env bash

Input_Str=$1
if [[ $2 -gt 25 ]]
    then ((Rotation_Key=(26-$2)))
    else ((Rotation_Key=$2))
fi

Cipher_Alphabet_Gen()
{
alphabet=({a..z})

for (( i=0; i<$Rotation_Key; i++ ))
    do
       Last_Half+=${alphabet[$i]}
    done

for (( i=$Rotation_Key; i<26; i++ ))
    do
       First_Half+=${alphabet[$i]}
    done

Rot_Cipher=$( echo "$First_Half$Last_Half")
}

Encoder()
{
encoded=$( echo "$Input_Str" | tr 'a-z' "${Rot_Cipher}" | tr 'A-Z' "${Rot_Cipher^^}" )
}

Cipher_Alphabet_Gen $@
Encoder $@
echo "$encoded"