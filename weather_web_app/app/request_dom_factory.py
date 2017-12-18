from urllib.parse import parse_qsl
import json
import sys

# this class and its associated methods convert incoming request data into dictionary for easier access throughout
# the rest of the application
class RequestDomFactory:

    def __init__(self, logger):
        self.logger = logger

    def build_dom(self, environ):
        result = {
            'path': environ['PATH_INFO'],
            'headers': self.get_http_headers(environ),
            'query': self.get_query_string(environ)
        }

        return result

    def get_http_headers(self, environ):
        return dict((key[5:].lower(), environ[key]) for key in environ if key.startswith("HTTP_"))

    def get_query_string(self, environ):
        result = dict([
            (key.lower(), value) for (key, value) in parse_qsl(environ.get('QUERY_STRING', ''), keep_blank_values=True)
        ])

        return result
