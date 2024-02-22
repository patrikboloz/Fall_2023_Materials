#!/usr/bin/bash

#while read p
#do
#	echo $p
#done < read_file_while_loop.sh

cat read_file_while_loop.sh | while read p
do
	echo $p
done