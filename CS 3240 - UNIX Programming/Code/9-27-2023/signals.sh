#!/usr/bin/bash

set -x
path="~/Desktop/Boloz/'CS 3240'/9-27-2023/text.txt"

trap "rm -f $path" 0 2 15 #the value 2
echo "pid is $$$"

set +x 

while (( COUNT < 10 ))
do
	sleep 10
	(( COUNT++ ))
	echo $COUNT
done
exit 0