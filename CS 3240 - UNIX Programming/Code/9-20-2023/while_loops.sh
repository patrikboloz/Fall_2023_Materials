#!/usr/bin/bash

n=1

while (( $n <= 3 )) 
do
	echo "$n"
	(( n++ ))
	#gnome-terminal &
done