import sys

import googlemaps
import requests
import smtplib

from datetime import datetime


def namelookup(search, mode='driving', choice='distance'):
    """Uses the GoogleMaps API to retrieve a JSON that contains the searched name, then use this for lookup) """
    # print("Start lookup:", origin_in, destination_in, "with", mode, choice)
    filename = open('multidestdjango/logic/key.txt', 'r')  # open the key.txt file on local machine
    api_key = filename.read()  # set api_key to file content
    filename.close()

    gmaps = googlemaps.Client(key=api_key)  # initialize googlemaps client


    origin = search.replace(' ', '+')
    destination = search.replace(' ', '+')
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
    concat = url + "origins=" + origin + "&destinations=" + destination + "&key=" + api_key + "&mode=" + mode
    r = requests.get(concat)
    # name = r.json()["rows"][0]["elements"][0][choice]["text"]
    name = r.json()["destination_addresses"][0]

    return name
