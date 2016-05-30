#!/bin/bash
opt=$1
echo START THE TEST

export MAIN_DIR=./project/main
cases=()

if [ "$opt" = "all" ]; then
    for f in $MAIN_DIR/*.py
    do
        ff=${f##*/}
        ff=${ff%.*}
        if [ "$ff" = "base"]; then
            continue
        fi
        cases+=("$ff")
    done
else
    cases=(1 2 3 4 5 6 7)
fi
cnt=0
for case_num in ${cases[@]}
do
    echo RUN PROBLEM $case_num
    ./run.py $case_num
    echo done
    echo
    let cnt=cnt+1
done
echo $cnt cases have been run.
