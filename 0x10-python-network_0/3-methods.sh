#!/bin/bash
#http options
if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url="$1"

allow_methods=$(curl -s -X OPTIONS -I "$url" | grep "Allow:" | cut -d ' ' -f 2-)

if [ -z "$allow_methods" ]; then
	echo "No 'Allow' header found."
else
	echo "$allow_methods"
fi
