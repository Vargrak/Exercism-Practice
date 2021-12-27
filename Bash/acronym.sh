#!/usr/bin/env bash
#uses parameter expansion with regex to remove chars * _ - 
pass=${1//[\*\_\-]/ }
#Capitalizes remaining chars
pass=${pass^^}
#Sets delimiter for read to whitespace
IFS=" "
#Seperates whitespace delimited words into an array
read -a split <<< $pass
for word in ${split[@]}
do
#Parameter expansion used to get the first char in each array position and then add it to variable $acro
    acro+=${word:0:1}
done
echo "$acro"
exit 0
