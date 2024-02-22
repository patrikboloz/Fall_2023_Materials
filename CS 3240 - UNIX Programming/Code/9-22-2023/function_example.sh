#!/usr/bin/bash

#Create a script that will check whether a file exists or not
#by using functions

does_file_exist() {
	local file=$1
	[[ -f "$file" ]] && return 0 || return 1
}

usage() {
	echo "You need to provide an argument:"
	echo "usage: $0 file_name"
}

[[ $# -eq 0 ]] && usage

if ( does_file_exist "$1" )
then 
	echo "File was found."
else
	echo "File was not found."
fi

