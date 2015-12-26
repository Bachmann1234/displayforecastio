import os
from mock import patch
from displayforecastio.app import (
    FORECAST_DEV_KEY_VAR, main, format_weather, get_weather
)


def test_no_key(monkeypatch):
    if os.getenv(FORECAST_DEV_KEY_VAR):
        monkeypatch.delenv(FORECAST_DEV_KEY_VAR)
    assert main(['4.3', '4']) == -1


def test_weather_called_correctly(monkeypatch):
    monkeypatch.setenv(FORECAST_DEV_KEY_VAR, "IamaKey")
    with patch('displayforecastio.app.get_weather') as get_weather_mock:
        main(['4.3', '4'])
        get_weather_mock.assert_called_with('IamaKey', 4.3, 4)


def test_api_live():
    # This test is live and assumes you have an api key in your environment
    result = get_weather(
        os.environ[FORECAST_DEV_KEY_VAR],
        42.361369,
        -71.083544
    )
    assert isinstance(result, dict)
    assert 'daily' in result
    assert 'summary' in result['daily']
    assert 'icon' in result['daily']


def test_format_weather():
    # This is an api call with unused data taken out of it.
    api_input = {
        u'daily': {
            u'icon': u'rain',
            u'summary': u'Drizzle on Saturday and Tuesday, '
                        u'with temperatures peaking at 59\xb0F '
                        u'on Friday.'
        }
    }
    assert format_weather(api_input) == (
        u'Currently: rain - Drizzle on Saturday and Tuesday, '
        u'with temperatures peaking at 59\xb0F on Friday.'
    )
