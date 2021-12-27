#!/usr/bin/env bash

flag_process(){
while getopts ":nlivx" opts; do
   case $opts in
        n) linenumber=1 ;;
        l) filenameonly=1 ;;
        x) regex="^$regex$" ;;
        v) invert=1 ;;
        i) shopt -s nocasematch ;;
esac; done
}

get_text()
{
read -a inputarray <<< "$@"
for i in ${inputarray[@]}; do
    if [[ $i =~ [A-Za-z]+\.[A-Za-z]+ ]]; then files+=($i)
    elif [[ $i =~ ^[[:alpha:]] ]]; then words+=($i); fi
done
for count in ${files[@]}; do
((filescount++)); done
regex=$(echo "${words[@]}")
}

line_process(){
for f in ${files[@]}; do
    numline=0; printed=0
        while read -r line; do 
        ((numline++))
        if [[ $invert -eq 1 ]]; then match=1; fi
        if [[ $line =~ $regex ]] && [[ $invert -ne 1 ]]; then match=1
        elif [[ $line =~ $regex ]] && [[ $invert -eq 1 ]]; then match=0; fi
            while [[ $match -eq 1 ]] && [[ printed -ne 1 ]]; do
                if [[ $filenameonly -eq 1 ]]; then echo "$f" && printed=1 && match=0; fi
                if [[ $filescount -gt 1 ]] && [[ $printed -ne 1 ]]; then echo -n "$f:"; fi
                if [[ $linenumber -eq 1 ]] && [[ $printed -ne 1 ]]; then echo -n "$numline:"; fi
                if [[ $match -eq 1 ]]; then echo "$line" && match=0; fi
            done
        done < $f
done
}

get_text $@
flag_process $@
line_process
