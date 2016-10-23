#!/bin/bash

# prompt
read -e -s -p "Install requests library and create sodiumbot.zip [y/n]? " -n 1 -r
[[ ! $REPLY =~ ^[Yy]$ ]] && { echo "Nope? Okay."; exit; }

pip install requests -t . --upgrade
zip -r9 sodiumbot.zip *
echo "upload sodiumbot.zip to your AWS Lambda function."
