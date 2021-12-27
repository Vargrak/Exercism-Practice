#!/usr/bin/env bash
upper=0
lower=0
qmark=0

str=$(echo "$1" | tr -d [:space:])

parse()
{
if [[ $str =~ [A-Z] ]]; then upper=1; fi
if [[ $str =~ [a-z] ]]; then lower=1; fi
if [[ $str =~ \?+$ ]]; then qmark=1; fi
}

answer()
{
if (($qmark+$upper-$lower==2)); then echo "Calm down, I know what I'm doing!"
elif (($qmark==1)); then echo "Sure."
elif ((1==$upper-$lower)); then echo "Whoa, chill out!"
else echo "Whatever."
fi
}

parse "$@"
if [[ ${#str} -ne 0 ]]; then answer "$@"
else echo "Fine. Be that way!"
fi
