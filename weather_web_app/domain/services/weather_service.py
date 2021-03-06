# this class handles most of the business logic including data validation

class WeatherService:
    def __init__(self, api_factory, config, logger, validation_factory, weather_service_factory):
        self.api_factory = api_factory
        self.config = config
        self.logger = logger
        self.validation_factory = validation_factory
        self.weather_service_factory = weather_service_factory

    def get(self, request_model):
        print("request model:", request_model)
        valid_coordinates = self.validation_factory.validate_coordinates(self.logger, request_model)

        api_request_model = None
        if valid_coordinates:
            api_request_model = self.weather_service_factory.build_dark_sky_api_model(request_model)
            print("fetching weather data from coordinates")

        elif request_model.address is not None and len(request_model.address) > 0:
            api_request_model = self.weather_service_factory.get_coordinates_from_address(request_model.address, self.config)
            print("fetching weather data from address")

        print("api request model 1: ", api_request_model)
        weather_data = None
        if api_request_model is not None:
            weather_data = self.api_factory.get_weekly_forecast(api_request_model)
            if request_model.language_flag == True:
                self.to_fahrenheit(weather_data)

        print("api_request_model2: ", api_request_model)
        print("response: ", weather_data)
        return weather_data

    def to_fahrenheit(self, weather_data):
        print("before conversion:")
        print(weather_data.min_temps)
        print(weather_data.current_temp)
        for i in range(7):
            weather_data.min_temps[i] = weather_data.min_temps[i] * 1.8 + 32
            weather_data.max_temps[i] = weather_data.max_temps[i] * 1.8 + 32

        weather_data.current_temp = int(weather_data.current_temp) * 1.8 + 32

        weather_data.units = "F"
        print(weather_data.min_temps)
        print(weather_data.current_temp)
        return
