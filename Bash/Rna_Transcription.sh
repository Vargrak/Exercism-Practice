#!/usr/bin/env bash
Handler=$( echo "$1" | sed 's/[ACGT]/ /g' )
if [[ $Handler =~ [A-Z] ]]; then echo "Invalid nucleotide detected." && exit 1; fi
( echo "$1" | tr 'G' 'X' | tr 'C' 'G' | tr 'X' 'C'| tr 'A' 'U' | tr 'T' 'A' )