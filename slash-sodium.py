#!/usr/bin/env python

'''
This function handles a Slack /sodium command + movie title and returns how much nori and sodium it would take if you used nori as film substrate.
'''

import json
import requests
from urlparse import parse_qs
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

# returns Slack message JSON object stating that format was invalid
def invalidFormat():
  return { "text":"Something is wrong. Please make sure your movie title is correct." }


def main(text, user):
    try:
        movie_data = requests.get("http://www.omdbapi.com/?t=" + text)
        title = movie_data.json()['Title']
        runtime = movie_data.json()['Runtime']
        frames = 1440 * int(runtime.split()[0])
        sheets = frames / 56
        nori_kg = (sheets * 2.1) / 1000
        sodium_mg = sheets * 10
        sodium_g = sodium_mg / 1000

        slack_message = "%s is %s frames.\nThat\'s %s sheets of nori.\n%s kg of nori.\n%s g of sodium." % (title, frames, sheets, nori_kg, sodium_g)
        response = { "response_type": "in_channel", "text": slack_message, "username": "SodiumFilmBot", 'icon_emoji': ':film_frames:' }

    except AttributeError:
        response = invalidFormat()

    return response


def lambda_handler(event, context):
    params = parse_qs(event['body'])
    user = params['user_name'][0]
    command = params['command'][0]
    channel = params['channel_name'][0]
    try:
        command_text = params['text'][0]
    except KeyError:
        command_text = "pulp fiction"

    return respond(None, main(command_text, user))
