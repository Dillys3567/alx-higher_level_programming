#!/bin/bash
curl -L -s -X HEAD -w "%{http_code}" "$1"
