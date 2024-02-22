#!/usr/bin/bash

name_array=(patrik john mark batman)

select name in ${name_array[@]}
do
	case $name in
	mark )
		echo "Mark goes to buy some milk." ;;
	john )
		echo "John needs to buy some football tickets." ;;
	patrik )
		echo "Patrik is forbidden from buying more V-Bucks." ;;
	batman )
		echo "Nobody tells batman what batman has to do." ;;
	* )
		echo "Error. Exiting"
		break ;;
	esac
done