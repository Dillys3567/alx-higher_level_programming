#!/bin/bash
#json post
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
