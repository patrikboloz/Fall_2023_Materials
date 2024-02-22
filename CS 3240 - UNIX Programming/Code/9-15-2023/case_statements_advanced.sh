#!/usr/bin/bash

echo -e "Enter some character: \c"
read value

case $value in
	[a-z] )
		echo "User entered $value between a and z." ;;
	[A-Z] )
		echo "User entered $value between A and Z." ;;
	[0-9] )
		echo "User entered $value between 0 and 9." ;;
	? )
		echo "User entered $value which is a special character." ;;
	* )
		echo "Unknown input." ;;
esac
