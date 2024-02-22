#!/usr/bin/bash

#break statement to get out of the loop prematurely
#exit stops the execution of any following code immediately
#continue skips the normal execution for that iteration

for (( i=1 ; i<=10; i++ ))
do
	if [ $i -eq 3 -o $i -eq 6 ]
	then
		continue
	fi
	echo "$i"
done

echo "Script done."