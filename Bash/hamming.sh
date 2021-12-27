#!/usr/bin/env bash
#check each character in string, if they are equal
hamm()
{
until [ $i -eq $leng ]
do
	if [ ${x:i:1} = ${y:i:1} ]
	then ((i+=1))
	else ((off+=1)) && ((i+=1))
    fi
done
echo "$off"
}

#defines
defines()
{
x=$1
y=$2
i=0
leng=${#x}
off=0
equalss "$@"
}

#check if variables are equal length
equalss()
{
if [ ${#x} = ${#y} ]; then hamm "$@"
else echo "strands must be of equal length"
exit 1
fi
