#!/bin/bash
#post request

if [$# -e 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url="$1"

email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -s -d "email=$email&subject=$subject" "$url")

echo "$response"
