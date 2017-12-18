import json
from pyrecord import Record
from datetime import datetime
import decimal

class EnhancedJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,decimal.Decimal):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Record):
            return obj.get_field_values()
        return json.JSONEncoder.default(self,obj)
