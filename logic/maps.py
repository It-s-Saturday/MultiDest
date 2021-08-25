import sys

import googlemaps
import requests
import smtplib

from datetime import datetime


def lookup(origin_in, destination_in, mode, choice):
    filename = open('key.txt', 'r')

    api_key = filename.read()
    filename.close()

    gmaps = googlemaps.Client(key=api_key)
    origin = origin_in.replace(' ', '+')
    destination = destination_in.replace(' ', '+')
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
    concat = url + "origins=" + origin + "&destinations=" + destination + "&key=" + api_key + "&mode=" + mode
    # print("Computed:", origin_in, "to", destination_in, concat)
    r = requests.get(concat)
    # try:
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    # except:
    #     time = str(sys.maxsize)
    #     print("ERROR: NO DESTINATION")
    return time
