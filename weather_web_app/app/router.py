from container_factory import ContainerFactory
from routes import Mapper
import logging

def build_map():

    url_map = Mapper(controller_scan= [
        "weather"
    ])

    # url_map.connect("/{controller}/{action}")
    # url_map.connect("/{controller}/{action}/")
    url_map.connect("/{controller}")
    url_map.connect("/{controller}/")
    # url_map.connect("/")
    return url_map

class Router:

    def __init__(self, config):
        self.config = config
        self.container = ContainerFactory().build_components(self.config)
        self.logger = logging.getLogger(config.get('app_logger'))

    def send_default_response(self, environ, start_response):
        # headers = [('Content-Type', 'text/html; charset=UTF-8'), ('Content-Encoding', 'gzip'), ('Accept-Ranges', 'bytes')]
        headers = [('Accept-Ranges', 'bytes')]
        start_response("200 OK", headers)

        file_path = self.config['src_location']

        if environ['PATH_INFO'] == '/':
            file_name = "index.html"
        else:
            file_name = environ['PATH_INFO']

        return open(file_path + file_name, 'rb')

    def serve(self, environ, start_response):
        url_map = build_map()

        request_context = url_map.match(environ["PATH_INFO"].lower())
        request_method = environ["REQUEST_METHOD"].lower()

        if request_context is not None and "controller" in request_context:
            controller = self.container.lookup(request_context['controller'] + "_controller")
        else:
            return self.send_default_response(environ, start_response)
        controller_actions = dir(controller)
        action = None

        if request_method in controller_actions:
                action = getattr(controller, request_method)

        if action == None:
            output = "this service is unavailable. Please try /weather endpoint"
            response_headers = [
                ('Content-type', 'text/plain'),
                ('Content-Length', str(len(output)))
            ]
            start_response("404 Not Found", response_headers)
            return [output.encode('utf-8')]
        else:
            print(str(action))
            print("{0}: {1}".format(environ['REQUEST_METHOD'].lower(), environ["PATH_INFO"].lower()))

            return action(environ, start_response)
