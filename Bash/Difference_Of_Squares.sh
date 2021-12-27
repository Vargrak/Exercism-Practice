#!/usr/bin/env bash
selector=$1 && n=$2

sum_of_square()
{
    for (( i=n; i>0; i-- ))
        do 
            ((sumofsq+=(i**2)))
        done
    result=$sumofsq
}

square_of_sum()
{
    for (( i=n; i>0; i-- ))
        do 
            ((summation+=i))
        done
    ((sqofsum=summation**2))
    result=$sqofsum
}

compare()
{
if ((sumofsq>=sqofsum)); then ((difference=sumofsq-sqofsum))
elif ((sqofsum>sumofsq)); then ((difference=sqofsum-sumofsq)); fi
result=$difference
}

case $selector in
    square_of_sum) square_of_sum ;;
    sum_of_squares) sum_of_square ;;
    difference) sum_of_square && square_of_sum && compare ;;
esac
printf "%s" "$result"