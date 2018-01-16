# define the appropraite models realted to weather data here
from pyrecord import Record

WeatherRequestModel = Record.create_type("WeatherRequestModel",
    "address",
    "latitude",
    "longitude",
    "language_flag",
    address=None,
    latitude=None,
    longitude=None,
    language_flag=None)

WeatherResponseModel = Record.create_type("WeatherResponseModel",
    "current_temp",
    "latitude",
    "longitude",
    "min_temps",
    "max_temps",
    "time",
    "units",
    "wind_speeds",
    current_temp=None,
    latitude=None,
    longitude=None,
    min_temps=None,
    max_temps=None,
    time=None,
    units=None,
    wind_speeds=None)
