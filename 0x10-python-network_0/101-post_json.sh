#!/bin/bash

if [ $# -ne 2 ]; then
	echo "Usage: $0 <URL> <filename>"
	exit 1
fi

url="$1"
filename="$2"

if [ ! -f "$filename" ]; then
	echo "File '$filename' not found."
	exit 1
fi

curl -s -X POST -H "Content-Type: application/json" --data "@filename" "$url"
