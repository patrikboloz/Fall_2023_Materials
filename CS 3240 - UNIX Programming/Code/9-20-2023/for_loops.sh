#!/usr/bin/bash

#Only works for bash version 4.0 and up
for i in {1..10..2} #START..END..INCREMENT
do
	echo $i
done

#Works for all versions
for (( i=1;i<10;i+=2 )) #START..END..INCREMENT
do
	echo $i
done