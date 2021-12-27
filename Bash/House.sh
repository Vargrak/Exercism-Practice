#!/bin/bash
Startline=$(($1-1))
Stopline=$(($2-1))

if [[ $1 -lt 1 ]] || [[ $2 -gt 12 ]] || [[ $1 -gt $2 ]]; then echo "invalid" && exit 1; fi

First_Line=(
    'This is the house that Jack built.'
    'This is the malt'
    'This is the rat'
    'This is the cat'
    'This is the dog'
    'This is the cow with the crumpled horn'
    'This is the maiden all forlorn'
    'This is the man all tattered and torn'
    'This is the priest all shaven and shorn'
    'This is the rooster that crowed in the morn'
    'This is the farmer sowing his corn'
    'This is the horse and the hound and the horn'
)

Finishing_Lines=(
    'that belonged to the farmer sowing his corn'
    'that kept the rooster that crowed in the morn'
    'that woke the priest all shaven and shorn'
    'that married the man all tattered and torn'
    'that kissed the maiden all forlorn'
    'that milked the cow with the crumpled horn'
    'that tossed the dog'
    'that worried the cat'
    'that killed the rat'
    'that ate the malt'
    'that lay in the house that Jack built.'
)

To_Line()
{
    echo "${First_Line[$Startline]}"
    ((Begin=11-Startline))
    for (( i=Begin; i<11; i++ ))
        do
            echo "${Finishing_Lines[$i]}"
        done
}

Repeat_Line()
{
    ((repeat=Stopline-Startline))
    for (( i=0; i<=repeat; i++ ))
        do
            ((Begin=11-(Startline+i)))
            ((BeginS=Startline+i))
            echo "${First_Line[$BeginS]}"
            for (( x=Begin; x<11; x++ ))
                do
                    echo "${Finishing_Lines[$x]}"
                done
                echo ""
        done
}

if [[ $Startline == "$Stopline" ]]; then To_Line
else Repeat_Line; fi