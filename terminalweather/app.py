import sys

import os
import argparse

import requests

FORECAST_DEV_KEY_VAR = "FORECAST_API"


def format_weather(weather_dict):
    """
    Make the weather pretty for the terminal
    :param weather_dict:
        Dict with an api response from the forcast.io api
    :return:
        String summarizing the current weather
    """
    return u"Currently: {} - {}".format(
        weather_dict['daily']['icon'],
        weather_dict['daily']['summary']
    )


def get_weather(key, lat, long):
    """
    Call our api to get the weather
    :param key:
        str - ForcastIO api key
    :param lat:
        float - Latitude
    :param long:
        float - Longitude
    :return:
        A dictionary of the api response
    """
    # todo: some error handling would be nice
    return requests.get("https://api.forecast.io/forecast/{}/{},{}".format(key, lat, long)).json()


def main():
    parser = argparse.ArgumentParser(description='Print the weather')
    parser.add_argument(
        'lat', type=float,
        help='an integer for the accumulator'
    )
    parser.add_argument(
        'long', type=float,
        help='an integer for the accumulator'
    )
    args = parser.parse_args()
    try:
        key = os.environ[FORECAST_DEV_KEY_VAR]
    except KeyError:
        print "I'm sorry. You need a forecast.io dev key defined as an an environment variable: {}".format(
            FORECAST_DEV_KEY_VAR
        )
        print "You can register for one here: https://developer.forecast.io/"
        return -1

    print format_weather(get_weather(key, args.lat, args.long))


if __name__ == '__main__':
    sys.exit(main())
