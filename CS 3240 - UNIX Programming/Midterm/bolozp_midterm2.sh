#!usr/bin/bash

# Display user and system variables
echo "Current name: $1"
name=$1

# Read user input
read -p "Enter your age: " age

# Display a personalized message
echo "Hello, $name!"
if [ "$age" -ge 18 ]; 
then
    echo "You are an adult since your age is $age."
else
    echo "You are a minor since your age is $age."
fi

# Append user data to a file
echo "Name: $name, Age: $age" >> bolozp_midterm2_data.txt

# Logical AND and OR operators
if [ "$age" -ge 18 ] && [ "$age" -le 65 ]; 
then
    echo "You are between 18 and 65 years old."
fi

if [ "$age" -lt 18 ] || [ "$age" -ge 65 ]; 
then
    echo "You are either under 18 or 65 and older."
fi
