#!/bin/bash

# FIXME - check all of the questions
# >> = append, > redirect to
# $# contains the number of command line arguments (not including $0)

for num in "$@"
do
	echo "$num" >> q4_p5_temp.txt
done
echo -n "Min = " ; sort -g q4_p5_temp.txt | head -1
echo -n "Max = " ; sort -g q4_p5_temp.txt | tail -1

size=$(wc -l q4_p5_temp.txt | cut -f1 -d' ')

if [ $(($size % 2)) == 0 ]; then
	median_index=$((size / 2))
	first_num=$(sort -g q4_p5_temp.txt | head -"$median_index" | tail -1)
	((median_index++))
	second_num=$(sort -g q4_p5_temp.txt | head -"$median_index" | tail -1)
	
	# get average
	echo -n "Median = "; bc <<< "scale = 1; ($first_num + $second_num) / 2"
else
	median_index=$(((size / 2) + 1))
	echo -n "Median = " ; sort -g q4_p5_temp.txt | head -"$median_index" | tail -1
fi

rm q4_p5_temp.txt
