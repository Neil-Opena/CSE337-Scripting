#!/bin/bash
# Part 3
echo -n "Enter a sentence: "
read sentence

count=0

while read -n1 char; do
	if [ "$char" == "k" ]; then
		((count++))
	fi
done < <(echo -n $sentence)

echo "$count"
