#!/bin/bash
# Part 1

# command line argument = directory dir
dir=$1
echo "Current shell is: $SHELL"
echo "Current directory is: $PWD"
echo "Home directory is: $HOME"
echo ""
echo "--5 most recently modified non-empty subdirectories--"
# 5 most recently modified non-empty subdirectories in the current directory in long listing format
ls -clt $dir | head -6 | tail -5
echo ""
echo "--Files in last 45 minutes"
# the files in the current directory that are modified less than 45 minutes ago with a size of at least 1000 bytes
find $dir -cmin -45 -size +1000b
echo ""
# line of 70 equal signs
for i in `seq 1 70`;
do
	echo -n "="
done
