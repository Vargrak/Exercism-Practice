#!/usr/bin/env bash

Initialization()
{
    rna=$@
    leng=${#rna}
}

Input_Processing()
{
    for i in $(seq 0 3 $leng); do
        currcodon=${rna:$i:3}
        if [ -z $currcodon ]; then echo "${Protein[@]}" && exit 0; fi
        case $currcodon in
            AUG) Protein+=("Methionine") ;;
            UUU | UUC) Protein+=("Phenylalanine") ;;
            UUA | UUG) Protein+=("Leucine") ;;
            UCU | UCC | UCA | UCG) Protein+=("Serine") ;;
            UAU | UAC) Protein+=("Tyrosine") ;;
            UGU | UGC) Protein+=("Cysteine") ;;
            UGG) Protein+=("Tryptophan") ;;
            UAA | UAG | UGA) echo "${Protein[@]}"; exit 0 ;;
            *) echo "Invalid codon"; exit 1 ;;
        esac
    done
}

Initialization $@
Input_Processing $@