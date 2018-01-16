from weather_web_app.domain.models.weather_model import WeatherRequestModel

# this class converts the relevant incoming url data from dictionary to object
# this helps ensure that we only deal with relevant data in domain services (business logic)
class WeatherModelFactory:
    def build_get(self, request_dom):
        headers = request_dom["headers"]
        query = request_dom["query"]

        return WeatherRequestModel(
            latitude=query.get("latitude"),
            longitude=query.get("longitude"),
            language_flag = True if (headers['language'] is not None and headers['language'] in ["en", "en_US"]) else False
        )
