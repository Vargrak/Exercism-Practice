((x=$1%3))
((y=$1%5))
((z=$1%7))
if [ $x -eq 0 ]; then raindrop+="Pling"
fi
if [ $y -eq 0 ]; then raindrop+="Plang"
fi    
if [ $z -eq 0 ]; then  raindrop+="Plong"
fi
if [[ -n $raindrop ]]; then echo "$raindrop"
else echo "$1"
fi
