#!/usr/bin/bash

for command in ls pwd date
do
	echo "==================$command=================="
	$command #execution of the command
	sleep 1
done

for item in * #take all the files in current directory
do
	if [ -d $item ] #checking if the item is a directory
	then
		echo "$item is a directory."
	elif [ -f $item ]
	then
		echo "$item is a file."
	fi
	sleep 1
done