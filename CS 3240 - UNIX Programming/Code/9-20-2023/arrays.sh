#!/usr/bin/bash


os=('ubuntu' 'windows' 'kali')

echo "${os[@]}" #getting all elements in the array
#echo "${os[1]}" #getting the element by calling its respective index
#echo "${!os[@]}" #indexes in the array
#echo "${#os[@]}" #length of the array

os[3]='mac'
echo "${os[@]}"

os[2]='redhat'
echo "${os[@]}"

os[10]='debian'
echo "${os[@]}"
echo "${!os[@]}"

string="hello"
echo "${string[@]}"
echo "${string[0]}"
echo "${string[1]}"
