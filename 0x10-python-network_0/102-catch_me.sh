#!/bin/bash
#catch me

response=$(curl -s 0.0.0.0:5000/catch_me)

message="${response#*You got me!}"
message="${message%%</h1>*}"
printf "%s\n" "message"
