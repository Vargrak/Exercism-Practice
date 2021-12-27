#!/usr/bin/env bash
code=()
bit1=$(($1&1))
bit2=$(($1&2))
bit3=$(($1&4))
bit4=$(($1&8))
bit5=$(($1&16))
binary=$( echo "obase=2;$1" | bc )
leng=${#binary}

appender()
{
if [ $t == 1 ] && [ $bit1 -gt 0 ]; then code+=("wink"); fi
if [ $t == 2 ] && [ $bit2 -gt 0 ]; then code+=("double_blink"); fi
if [ $t == 3 ] && [ $bit3 -gt 0 ]; then code+=("close_your_eyes"); fi
if [ $t == 4 ] && [ $bit4 -gt 0 ]; then code+=("jump"); fi
}

regular()
{
for ((t=0; t<=leng; t++ )); do
appender; done
}

reverse()
{
for ((t=leng; t>=0; t-- )); do
appender; done
}

format()
{
comma=${code[*]}
commad=${comma// /,}
underline=${commad//_/ }
echo "$underline"
}

if [ $bit5 -gt 0 ]; then reverse
else regular; fi
format
