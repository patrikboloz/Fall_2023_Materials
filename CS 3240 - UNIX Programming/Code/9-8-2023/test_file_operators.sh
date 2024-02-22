#!/usr/bin/bash

#Test file operators are used to check different files and their extensions

echo -e "Enter the name of a file: \c"
read filename 

#-e checks if the specified file exists
#-f checks if the file exists and if it is a valid file
#-d checks if a directory exists
#-s checks if the file is full/not empty
#-w, -r, -x to check the permissions (write, read, execute)

if [ -f "$filename" ] 
then
	echo "$filename was found."
	if [ -w "$filename" ]
	then
		echo "$filename is not empty."
	else
		echo "$filename is empty."
	fi
else
	echo "$filename was not found."
fi