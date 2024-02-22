#!/usr/bin/bash

#Test file operators are used to check different files and their extensions

echo -e "Enter the name of a file: \c"
read filename 

if [ -f "$filename" ]
then
	if [ -w "$filename" ]
	then
		echo "Write permissions were located."
		echo "Type some text to be appended. Use CTRL+D to leave."
		cat >> $filename #append mode adds information, does not replace data
	else
		echo "No write permissions found."
	fi
else
	echo "File with the name $filename was not found."
fi