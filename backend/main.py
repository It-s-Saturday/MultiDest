import os
import math

from flask import Flask, jsonify, request
from datetime import datetime
from itertools import permutations
from .Timer import Timer

import requests as make_call

app = Flask(__name__)

app.config.from_pyfile("settings.py")

SUCCESS = "success"
DEBUG = False

api_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"


# override print function to output when DEBUG is set to True
def pr(*args):
    if DEBUG:
        print(*args)

@app.route("/")
def index():
    return "Hello, World!"


def convert_string_to_params(string):
    return string.replace(" ", "%20").replace(",", "%2C").replace("\n", "%0A")


def lookup(i_from, i_to, metric="duration"):
    use_url = (
        api_url
        + "origins="
        + convert_string_to_params(i_from)
        + "&destinations="
        + convert_string_to_params(i_to)
        + "&units=imperial&key="
        + app.config["API_KEY"]
    )
    response = make_call.request("GET", use_url, headers={}, data={})
    value = response.json()["rows"][0]["elements"][0][metric]["value"]
    pr(f"Looking up {i_from} to {i_to}: {value}")
    return int(value)


@app.route("/get_optimal_route", methods=["POST"])
def get_optimal_route():
    with Timer("get_optimal_route") as t:
        metric = "duration"
        data = request.get_json()
        list_of_stops = data["inputValues"]
        origin_stop = list_of_stops[0]
        intermediate_stops = list_of_stops[1:-1] if len(list_of_stops) > 2 else []
        destination_stop = list_of_stops[-1]

        valid_paths = [
            [origin_stop] + list(intermediate_permutation) + [destination_stop]
            for intermediate_permutation in list(permutations(intermediate_stops))
        ]

        if DEBUG:
            for path in valid_paths:
                pr(path)
        min_cost = math.inf
        min_cost_path = []

        for path in valid_paths:
            cost = 0
            for i in range(len(path) - 1):
                cost += lookup(path[i], path[i + 1], metric)
            if cost < min_cost:
                min_cost = cost
                min_cost_path = path
            pr(f"Cost of {path} is {cost}")

        url = "https://www.google.com/maps/dir/"
        url += "/".join(min_cost_path).replace(" ", "+")

    out =        {
            "path": min_cost_path,
            "cost": min_cost,
            "url": url,
            "computation_time": t.elapsed,
            "status": SUCCESS,
        }
    pr(out)
    return jsonify(out)


@app.route("/server_status", methods=["GET"])
def server_status():
    return jsonify({"status": 400, "current_time": datetime.now()})


if __name__ == "__main__":
    app.run(debug=True)
