#!/usr/bin/env bash
message=${2,,}

encoder()
{
encoded=$( echo "$message" | tr 'a-z' 'zyxwvutsrqponmlkjihgfedcba' | tr -d [:space:] | tr -d [:punct:] | sed -e 's/...../& /g' -e 's/[[:space:]]$//g')
}

decoder()
{
decoded=$( echo "$message" | tr 'zyxwvutsrqponmlkjihgfedcba' 'a-z' | tr -d [:space:] )
}

case $1 in
    encode) encoder && echo "$encoded" ;;
    decode) decoder && echo "$decoded" ;;
         *) echo "Usage atbash_cipher.sh <encode|decode> <string>"
esac
