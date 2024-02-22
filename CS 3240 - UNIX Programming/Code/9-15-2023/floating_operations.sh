#!/usr/bin/bash

num1=20
num2=2.5

echo "20+2.5" | bc
echo "20*2.5" | bc
echo "20/2.5" | bc
echo "20-2.5" | bc
echo "20%2.5" | bc

#Floating answer for division
echo "scale=10;20/2" | bc
echo "scale=5;20/2.3" | bc

#More complex operations
num=81
echo "scale=2;sqrt($num)" | bc
echo "scale=2;$num^2" | bc