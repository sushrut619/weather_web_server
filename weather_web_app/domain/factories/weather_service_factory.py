from weather_web_app.domain.models.dark_sky_api_model import DarkSkyRequest

class WeatherServiceFactory:
    def build_dark_sky_api_model(self, model):
        return DarkSkyRequest(
            latitude=model.latitude,
            longitude=model.longitude
        )

    def get_coordinates_from_address(self, address, config):
        gmaps = googlemaps.Client(config.get('google_api_key'))

        # Geocoding an address
        geocode_result = gmaps.geocode('Boston')
        geocode_result = geocode_result[0]
        pprint(geocode_result)
        if ("geometry" in geocode_result and "location" in geocode_result['geometry'] and
            "lat" in geocode_result['geometry']['location'] and "lng" in geocode_result['geometry']['location']):
            return DarkSkyRequest(
                latitude=geocode_result['geometry']['location']['lat'],
                longitude=geocode_result['geometry']['location']['lng']
            )
        else:
            return None
