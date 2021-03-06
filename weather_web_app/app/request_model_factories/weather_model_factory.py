from weather_web_app.domain.models.weather_model import WeatherRequestModel
import re

# this class converts the relevant incoming url data from dictionary to object
# this helps ensure that we only deal with relevant data in domain services (business logic)
class WeatherModelFactory:
    def build_get(self, request_dom):
        headers = request_dom["headers"]
        query = request_dom["query"]

        language = None
        if headers['language'] is not None:
            language = headers['language']
            language = language.split(',')
            language = language[0].split(';')

        print("language header: ", headers.get('language'))
        return WeatherRequestModel(
            address=query.get("address"),
            latitude=query.get("latitude"),
            longitude=query.get("longitude"),
            # language_flag = True if (
            #                          headers['language'] is not None and
            #                             (
            #                                 headers['language'] in ["en", "en_US", "en-US", "en-US,en;q=0.9"] or
            #                                 "en" in re.split(re.split(',|;|=', headers['language']))
            #                             )
            #                          ) else False
            language_flag = True if (
                                        language is not None and
                                        (
                                            language[0] in ["en", "en_US", "en-US"]
                                        )
                                    ) else False
        )
