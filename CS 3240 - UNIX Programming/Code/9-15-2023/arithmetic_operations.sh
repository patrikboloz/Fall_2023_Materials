#!/usr/bin/bash


num1=11
num2=5

echo "$((num1 + num2))"
echo "$((num1 - num2))"
echo "$((num1 * num2))"
echo "$((num1 / num2))"
echo "$((num1 % num2))"

#Alternate way

num3=20
num4=10

echo "$(expr $num3 + $num4)"
echo "$(expr $num3 - $num4)"
echo "$(expr $num3 \* $num4)"
echo "$(expr $num3 / $num4)"
echo "$(expr $num3 % $num4)"
