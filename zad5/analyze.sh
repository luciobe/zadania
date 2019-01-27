#!/bin/bash
if [ -z "$1" ]
then
	echo "No error code is defined, Checking whole log for all errors!"

	echo "Number of lines in file:"
	awk '{print "lines"}' access.log | sort | uniq -c | sort -rn

	echo "Number of all errors:"
	awk '($9 >= 400) {print "errors"}' access.log | sort | uniq -c | sort -rn

	echo "Number of specific errors:"
	awk '($9 >= 400) {print $9}' access.log | sort | uniq -c | sort -rn

	echo "Check output file - errors.csv - you can find there error count per date"		
	awk '($9 >= 400) { gsub("\[","",$4); gsub("\/","-",$4); print $9" "$4  }' access.log | cut -f1 -d':' | uniq -c | awk -F ' ' '{cmd="date -d \""$3"\" \"+%F\""; cmd | getline out; print out ";" $2 ";" $1}' > errors.csv
else
	
	echo "Count of $1 errors:"
	awk -v CODE=$1 '($9 == CODE) {print $9}' access.log | sort | uniq -c | sort -rn

	echo "Check output file - $1.csv - you can find there error count per date"		
	awk -v CODE=$1 '($9 == CODE) { gsub("\[","",$4); gsub("\/","-",$4); print $9" "$4  }' access.log | cut -f1 -d':' | uniq -c | awk -F ' ' '{cmd="date -d \""$3"\" \"+%F\""; cmd | getline out; print out ";" $2 ";" $1}' > $1.csv

fi
