import googlemaps
import requests
import smtplib

from datetime import datetime

filename = open('key.txt', 'r')

api_key = filename.read()
filename.close()

gmaps = googlemaps.Client(key=api_key)
print(api_key)
origin = input("Enter origin: ")
# origin = '2111 High Street'
origin = origin.replace(' ', '+')
dest = input("Enter destination: ")
# dest = 'Kean University'
dest = dest.replace(' ', '+')
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
concat = url + "origins=" + origin + "&destinations=" + dest + "&key=" + api_key
print(concat)
r = requests.get(concat)
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]

print(time)