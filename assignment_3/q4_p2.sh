#!/bin/bash
# Part 2

i=1

while [ $i -le 10 ]
do
	if [ $(($i % 2)) == 0 ]; then
		touch "even$i"
		chmod 764 "even$i"
	else 
		touch "odd$i"
		chmod 554 "odd$i"
	fi
	((i++))
done
