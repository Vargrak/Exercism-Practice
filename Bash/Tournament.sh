#!/bin/bash
input=$( cat <<INPUT
Courageous Californians;Devastating Donkeys;win
Allegoric Alaskans;Blithering Badgers;win
Devastating Donkeys;Allegoric Alaskans;loss
Courageous Californians;Blithering Badgers;win
Blithering Badgers;Devastating Donkeys;draw
Allegoric Alaskans;Courageous Californians;draw
INPUT
)

declare -A MP Wins Losses Draws Total
Process_Input()
{
   IFS=';'
    while read -ra Input_Array 
        do

            if [[ -z "${Input_Array[0]}" ]]; then Text_Output && exit 0; fi
            ((MP[${Input_Array[0]}]++))
            ((MP[${Input_Array[1]}]++))
            case ${Input_Array[2]} in
                win) 
                    ((Wins[${Input_Array[0]}]++))
                    ((Losses[${Input_Array[1]}]++))
                    ;;
                loss)
                    ((Wins[${Input_Array[1]}]++))
                    ((Losses[${Input_Array[0]}]++))
                    ;;
                draw)
                    ((Draws[${Input_Array[0]}]++))
                    ((Draws[${Input_Array[1]}]++))
                    ;;
            esac
        done <<< "$input"
}    

Totaling()
{
    local Winsval Drawval
    for key in "${!MP[@]}"
        do
            Winsval=${Wins[$key]}
            Drawval=${Draws[$key]}
            ((Total["$key"]=(Winsval*3)+Drawval))
            Teams+=("$key")
        done
}

Text_Output()
{
    pad="                               "
    printf "%s\n" "Team                           | MP |  W |  D |  L |  P"

  #redo fucking stupid sorting AAAAAAAAAAAAAAAAAA

    for (( i=0; i<Team_Amt; i++ ))
        do
            if ((equ==Team_Amt)); then team_out=${TSortA[$i]}
            else team_out=${TSort[$i]}; fi
            printf "%.31s%s%5s%5s%5s%5s%3s\n" "$team_out${pad:${#string}}" "|" "${MP[$team_out]:-0} |" "${Wins[$team_out]:-0} |" "${Draws[$team_out]:-0} |" "${Losses[$team_out]:-0} |" "${Total[$team_out]:-0}"
        done
}

Process_Input "$@"
Totaling "$@"
Text_Output "$@"