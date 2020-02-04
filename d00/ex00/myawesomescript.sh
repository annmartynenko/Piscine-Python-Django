#! /bin/sh
if [ "$#" -eq  "0" ]
    then
    echo "No arguments supplied"
else
	curl -s $* | grep -Eo '(http|https)://[^/"]+'
fi 
