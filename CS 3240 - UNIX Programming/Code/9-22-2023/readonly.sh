#!/usr/bin/bash

var=21
readonly var
var=50

hello(){
	echo "Hello World"
}

readonly -f hello
hello

hello(){
	echo "Hello World Again!"
}

hello
hello