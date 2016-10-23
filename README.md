# SodiumBot
Slack `/sodium` command to math the nori.

## Imagine...
- What if you printed out an entire film, frame by frame, on nori (Japanese seaweed snacks)?
- How many sheets of nori would you need for any given film?
- What if you sat down and tried to eat the entire film?
- How much sodium would that be?
- Would you die?

This Slack Slash Command simplifies the process, so you can just `/sodium Braveheart` (or whatever movie of your choice)

# Configuration
This script is intended to run as an AWS Lambda Function + API Gateway trigger.

1. Run the install.sh shell script.
2. This will create a zip file containing:
- slash-sodium.py
- requests library

3. Upload that zip to AWS Lambda. (Instructions how to do this are beyond the scope of this README.)
