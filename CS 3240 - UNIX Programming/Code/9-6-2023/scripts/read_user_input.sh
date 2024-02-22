#!/usr/bin/bash

clear

#Creating multiple name variables
#echo "Enter a name: "
#read name1 name2 name3
#echo "Entered names: $name1 $name2 $name3"

#Showing silent and one line input with echo statement
#read -sp "Enter a password: " password
#echo
#echo "This is the password: $password"

#Showing how to insert inputs into an array
echo "Enter the names to be saved in an array:"
read -a names
echo "Names are: ${names[0]} ${names[2]}"

#Usage of REPLY system variable
echo "Enter a message: "
read
echo "Your message was: $REPLY"

