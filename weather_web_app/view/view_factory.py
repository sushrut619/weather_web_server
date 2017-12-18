from weather_web_app.view.view_model import View
from weather_web_app.utils.enhanced_encoder import EnhancedJsonEncoder
from pyrecord import Record
from urllib.parse import urlencode
from datetime import datetime
import json


class ViewFactory:
    def build_get_response(self, request, response_model):
        content_type = self.__build_content_type(request, response_model)
        body = self.__build_body(request, response_model)

        return View(
            status="200 OK",
            headers=[('Content-type', content_type)],
            body=[body.encode('utf-8')]
        )

    def __build_body(self, request, response_model):
        if response_model == None:
            return ""

        if "application/json" in request['headers'].get("accept","").lower():
            result = json.dumps(response_model, cls=EnhancedJsonEncoder)

            return result
        elif(isinstance(response_model, str)):
            return response_model
        else:
            if isinstance(response_model, Record):
                response_model = response_model.get_field_values()
            return urlencode(response_model)

    def __build_content_type(self, request, data_model):
        if "application/json" in request['headers'].get("accept","").lower():
            return "application/json; charset=utf-8"
        else:
            return "application/x-www-form-urlencoded; charset=utf-8"
