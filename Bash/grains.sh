#!/usr/bin/env bash
ans=0
error(){
echo "Error: invalid input"
exit 1
}

if [ $1 == "total" ]; then ans=$(bc <<< "2^64-1")
elif [ $1 -lt 1 ]; then error
elif [ $1 -gt 64 ]; then error
else ans=$(bc <<< "2^$1/2")
fi

echo "$ans"
