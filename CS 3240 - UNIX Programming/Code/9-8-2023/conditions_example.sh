#!/usr/bin/bash

#This is the structure of an if-statement
#if [ condition ]
#then
#	statement
#fi

count=520
if (( count >= 10 ))
then
	echo "This condition is true."
else
	echo "This condition is not true."
fi

word="a"
if   [[ "$word" > "c" ]] 
then
	echo "This condition is true."
else
	echo "This condition is not true."
fi

word="abc"
if   [[ "$word" > "acd" ]] 
then
	echo "The word is bigger than adc in ASCII"
elif [[ "$word" == "abc" ]]
then
	echo "The word is abc."
elif [[ "$word" != "aec" ]]
then
	echo "The word is not aec."
else 
	echo "No other comparisons were done. Exiting"
fi
