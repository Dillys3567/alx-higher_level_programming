#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url="$1"

response=$(curl -I -s "$url")

code=$(echo "$response" |grep -i "HTTP/" | awk '{print $2}')

echo "$code"
