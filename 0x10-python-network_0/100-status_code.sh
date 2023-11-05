#!/bin/bash
#display status code
curl -L -s -X HEAD -w "%{http_code}" "$1"
