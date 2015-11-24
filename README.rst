Terminal Weather
================

Display the weather in your terminal!

This project is designed to show off a standard python project structure

To work it assumes you have the `FORECAST_API` environment variable set to be your `Forecast.io
<https://developer.forecast.io/>`_ api key.

.. code:: bash

    export FORECAST_API="<your key here>"


This app takes two args. A latitude and a longitude. Example usage with output is below

.. code:: python

    python terminalweather/app.py 42.3907 -71.1157
    Currently: rain - Drizzle on Saturday and Tuesday, with temperatures peaking at 59°F on Friday.


Setting up a development environment. I assume the latest python is installed

.. code:: bash

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Run the tests to ensure this all worked try running the tests. Like running the app one test requires the `FORCAST_API`
environment variable to be set

.. code:: bash

    py.test tests
