#!/bin/bash
#delete request
if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url="$1"

curl -X DELETE -s "$url"
