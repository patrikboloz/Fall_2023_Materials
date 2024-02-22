#!/usr/bin/bash

#Logical and and how it is used.

age=25

if [[ "$age" -gt 18 && "$age" -lt 30 ]]
then
	echo "Valid age. Entry approved."
else
	echo "Either too young or too old. Get lost."
fi 

#Logical or and how it is used

age=$1

if [ "$age" -gt 18 -o "$age" -lt 30 ]
then
	echo "Valid age. Entry approved."
else
	echo "Either too young or too old. Get lost."
fi 