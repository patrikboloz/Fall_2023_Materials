#!/usr/bin/bash

vehicle=$1

case $vehicle in
	"car" )
		echo "Rent of the $vehicle is 100 dollars." ;;
	"van" )
		echo "Rent of the $vehicle is 120 dollars." ;;
	"bicycle" )
		echo "Rent of the $vehicle is 10 dollars." ;;
	* )
		echo "Unknown vehicle." ;;
esac