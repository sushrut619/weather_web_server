from weather_web_app.domain.models.dark_sky_api_model import DarkSkyRequest

class WeatherServiceFactory:
    def build_dark_sky_api_model(self, model):
        return DarkSkyRequest(
            latitude=model.latitude,
            longitude=model.longitude
        )
