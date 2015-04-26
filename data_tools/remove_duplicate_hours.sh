#!/bin/bash  
OLDIFS=$IFS
IFS=","
ZEROS="00"

while read year month day hour min hum temp wspd wdir airp
 do 
  # echo -e "$min\n"
  if [ "$min" == '00' ]; then   	
  	echo $min
  else
  	echo "must be 0"
  fi
 done < $1
 IFS=$OLDIFS

# awk -F "," '{$5}' "raw weather - local time Beijing-January-2014.csv" 