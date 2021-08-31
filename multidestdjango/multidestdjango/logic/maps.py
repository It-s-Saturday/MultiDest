import sys

import googlemaps
import requests
import smtplib

from datetime import datetime


def lookup(origin_in, destination_in, mode, choice):
    print("Start lookup:", origin_in, destination_in, "with", mode, choice)
    filename = open('multidestdjango/logic/key.txt', 'r')  # open the key.txt file on local machine
    api_key = filename.read()  # set api_key to file content
    filename.close()

    gmaps = googlemaps.Client(key=api_key)  # initialize googlemaps client

    """
    Lines 20-23 build the URL for the API request.
    Line 25-26 grab the appropriate information for the query.
    """

    origin = origin_in.replace(' ', '+')
    destination = destination_in.replace(' ', '+')
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
    concat = url + "origins=" + origin + "&destinations=" + destination + "&key=" + api_key + "&mode=" + mode
    r = requests.get(concat)
    measurement = r.json()["rows"][0]["elements"][0][choice]["text"]

    return measurement

