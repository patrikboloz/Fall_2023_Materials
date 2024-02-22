#!/usr/bin/bash

function Hello(){

	echo "Hello World!"
}

print(){

	local name=$1
	echo "The name is $name" 
}

name="Tom"
echo "The name is $name."
print "Max"
echo "The name is $name."