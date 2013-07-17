#!/bin/bash

origin=$1
converted=$2
mkdir $converted
for file in $origin/*.txt
do
	filename="`basename "$file"`"
	extension="${filename##*.}"
	fileNoSuffix="${filename%.*}"
	echo $filename
	if [ ! -e "$converted$filename" ] 
	then
		echo "iconv -f gb18030 -t \"$origin/$filename\" > \"$converted/$filename\""
		iconv -f gb18030 -t utf-8 "$origin/$filename" > "$converted/$filename"
	fi
done
for file in $origin/*.TXT
do
	filename="`basename "$file"`"
	extension="${filename##*.}"
	fileNoSuffix="${filename%.*}"
	echo $filename
	if [ ! -e "$converted$filename" ] 
	then
		echo "iconv -f gb18030 -t \"$origin/$filename\" > \"$converted/$filename\""
		iconv -f gb18030 -t utf-8 "$origin/$filename" > "$converted/$fileNoSuffix.txt"
	fi
done
exit 0
