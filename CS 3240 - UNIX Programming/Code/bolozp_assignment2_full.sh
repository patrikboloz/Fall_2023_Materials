#!/usr/bin/bash

#With the use of arrays, a select loop, and case statements, create a bash program
#that will print out information about a chosen department. 
#Requirements: 
#-At least 4 departments with at least 1 faculty member
#-Faculty members stored in an array
#-Use the select loop so that the user can choose to print out the departments info
#-Print out the faculty names and the amount of faculty in each choice.
#-When the wrong choice is chosen, break out of the program

#Setting up the departments and faculty:
CS_faculty=("Boloz" "Gallegos" "Martinez" "Johnson" "Bhutta")
MATH_faculty=("Jeffries" "Martinez" "Turner")
CHEM_faculty=("Gogia" "Castaneda" "Timofeeva")
GEO_faculty=("Petronis" "Foucher")

#Select loops 
echo "Choose the department and I'll show you its faculty information:"

select department in CS CHEM MATH GEO
do
	case $department in

		CS)
			echo "======================================================="
			echo "You have chosen the CS Department."
			echo "Here are all the faculty members of the CS department:"
			echo "${CS_faculty[@]}"
			echo "Here is the number of all CS faculty members: ${#CS_faculty[@]}"
			echo "======================================================="
			;;
		CHEM)
			echo "======================================================="
			echo "You have chosen the CHEM Department."
			echo "Here are all the faculty members of the CHEM department:"
			echo "${CHEM_faculty[@]}"
			echo "Here is the number of all CHEM faculty members: ${#CHEM_faculty[@]}"
			echo "======================================================="
			;;
		GEO)
			echo "======================================================="
			echo "You have chosen the GEO Department."
			echo "Here are all the faculty members of the GEO department:"
			echo "${GEO_faculty[@]}"
			echo "Here is the number of all GEO faculty members: ${#GEO_faculty[@]}"
			echo "======================================================="
			;;
		MATH)
			echo "======================================================="
			echo "You have chosen the MATH Department."
			echo "Here are all the faculty members of the MATH department:"
			echo "${MATH_faculty[@]}"
			echo "Here is the number of all MATH faculty members: ${#MATH_faculty[@]}"
			echo "======================================================="
			;;
		*)
			echo "Wrong choice. Exiting"
			break
			;;
	esac
done


