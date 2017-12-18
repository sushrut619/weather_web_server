# this class acts like a glue that passes the data to different classes in appropriate formats and
# together build the application
class Controller():

    def __init__(self, logger, request_dom_factory, model_factory, domain_service, view_factory):
        self.logger = logger
        self.request_dom_factory = request_dom_factory
        self.model_factory = model_factory
        self.domain_service = domain_service
        self.view_factory = view_factory

    def get(self, environ, start_response):
        dom = self.request_dom_factory.build_dom(environ)
        request_model = self.model_factory.build_get(dom)
        result = self.domain_service.get(request_model)
        view = self.view_factory.build_get_response(dom, result)
        start_response(view.status, view.headers)

        return view.body
