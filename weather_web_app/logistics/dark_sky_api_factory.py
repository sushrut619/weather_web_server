import requests
import json
from weather_web_app.domain.models.weather_model import WeatherResponseModel

class DarkSkyApiFactory:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
    def get_weekly_forecast(self, model):
        url = self.config['dark_sky_url_template'].format(self.config['dark_sky_secret_key'],
                                                          model.latitude, model.longitude)
        api_response = requests.get(url, verify=False)

        if api_response.status_code == 200:
            return self.parse_weather_data(api_response)
        else:
            return None

    def parse_weather_data(self, response):
        raw_weather_data = response.text

        result = None
        if raw_weather_data is not None:
            weather_data = json.loads(raw_weather_data)
            result = self.build_temp_model(weather_data)
        return result

    def build_temp_model(self, weather_data):
        min_temps = [None]*7
        max_temps = [None]*7
        wind_speeds = [None]*7
        if ('daily' in weather_data and 'data' in weather_data['daily'] and len(weather_data['daily']['data']) > 0):
            if 'temperatureLow' in weather_data['daily']['data'][0]:
                min_temps = [weather_data['daily']['data'][i]['temperatureLow'] for i in range(7)]
            if 'temperatureHigh' in weather_data['daily']['data'][0]:
                max_temps = [weather_data['daily']['data'][i]['temperatureHigh'] for i in range(7)]
            if 'windSpeed' in weather_data['daily']['data'][0]:
                wind_speeds = [weather_data['daily']['data'][i]['windSpeed'] for i in range(7)]

            return WeatherResponseModel(
                current_temp=weather_data['currently']['temperature'],
                latitude=weather_data['latitude'],
                longitude=weather_data['longitude'],
                min_temps=min_temps,
                max_temps=max_temps,
                time=weather_data['daily']['data'][1]['time'],
                units="C",
                wind_speeds=wind_speeds
            )
        else:
            result = "Incorrect data received from dark sky API"
