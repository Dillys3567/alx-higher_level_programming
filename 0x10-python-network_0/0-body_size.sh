#!/bin/bash
#Bash script takes URL, sends request,displays size of the body
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

response=$(curl -sI "$url")

content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

if [ -z "$content_length" ]; then
	echo "Content-Length header not found."
	exit 1
fi

echo "${content_length}"
