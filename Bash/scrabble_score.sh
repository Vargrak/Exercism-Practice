#!/usr/bin/env bash
total=0

sc1=$( echo "$1" | sed -e 's/[AEIOULNRST]//Ig' )
sc2=$( echo "$1" | sed -e 's/[DG]//Ig' )
sc3=$( echo "$1" | sed -e 's/[BCMP]//Ig' )
sc4=$( echo "$1" | sed -e 's/[FHVWY]//Ig' )
sc5=$( echo "$1" | sed -e 's/[K]//Ig' )
sc6=$( echo "$1" | sed -e 's/[JX]//Ig' ) 
sc7=$( echo "$1" | sed -e 's/[QZ]//Ig' )
((total+=${#1}-${#sc1}))
((total+=2*(${#1}-${#sc2})))
((total+=3*(${#1}-${#sc3})))
((total+=4*(${#1}-${#sc4})))
((total+=5*(${#1}-${#sc5})))
((total+=8*(${#1}-${#sc6})))
((total+=10*(${#1}-${#sc7})))
echo "$total"
