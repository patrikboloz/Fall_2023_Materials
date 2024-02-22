#!/usr/bin/bash

#clear
echo "This script appends new data to an existing valid file, only if the file is not empty."
echo -e "Enter the name of the file: \c"
read file_name

if [ -f "$file_name" ] 
then
	echo "$file_name was found."

	if [ -s "$file_name" ] 
	then
		echo "$file_name is not empty. Exiting."
	else
		echo "$file_name is empty. Would you like to add data into the file?"
		echo -e "Type N for No or Y for Yes: \c"
		read answer
		if [ $answer == "Y" ]
		then
			echo "You chose to add data into this file in the append mode. Use CTRL + D to get out of it."
			cat >> $file_name
		elif [ $answer == "N" ]
		then
			echo "You chose not to add anything new. Exiting."
		else
			echo "Not a valid choice. Exiting."
		fi
	
	fi
else
	echo "$file_name was not found."
	echo -e "Would you like to create an empty file? Type N for No or Y for Yes: \c"
	read answer2
	if [ $answer2 == "Y" ]
	then
		touch $file_name
		echo "Your file with the name $file_name was created. Showing the files details:"
		ls -l $file_name
	elif [ $answer2 == "N" ]
	then
		echo "You chose not to create this file. Exiting."
	else
		echo "Not a valid choice. Exiting."
	fi
fi
