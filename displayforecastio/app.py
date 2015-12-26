import os
import sys
import argparse

import requests

FORECAST_DEV_KEY_VAR = "FORECAST_API"


def format_weather(weather_dict):
    """Make the weather pretty for the terminal

    Args:
        weather_dict (dict): Dict with an api response
        from the forcast.io api

    Returns: String summarizing the current weather
    """
    return u"Currently: {} - {}".format(
        weather_dict['daily']['icon'],
        weather_dict['daily']['summary']
    )


def get_weather(key, lat, long):
    """Call our api to get the weather

    Args:
        key (str): ForcastIO api key
        lat (float): Latitude
        long (float): Longitude

    Returns:
        dict: The api response
    """
    # todo: some error handling would be nice
    return requests.get(
        "https://api.forecast.io/forecast/{}/{},{}".format(key, lat, long)
    ).json()


def main(args):
    parser = argparse.ArgumentParser(description='Print the weather')
    parser.add_argument(
        'latitude', type=float,
        help='latitude is a float providing a partial position on a map. '
             'This combined with longitudg will tell us where to get the weather'
    )
    parser.add_argument(
        'longitude', type=float,
        help='Longitude is a float providing a partial position on a map. '
             'This combined with long will tell us where to get the weather'
             'from'
    )
    args = parser.parse_args(args)
    try:
        key = os.environ[FORECAST_DEV_KEY_VAR]
    except KeyError:
        print(
            "I'm sorry. You need a forecast.io dev key defined as "
            "an an environment variable: {}".format(
                FORECAST_DEV_KEY_VAR
            )
        )
        print("You can register for one here: https://developer.forecast.io/")
        return -1

    print(format_weather(get_weather(key, args.latitude, args.longitude)))


# Run is the entry point for the runnable script
# Main is for if you run this python script directly

def run():
    sys.exit(main(sys.argv[1:]))

if __name__ == '__main__':
    run()
