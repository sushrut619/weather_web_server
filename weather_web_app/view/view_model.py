from pyrecord import Record

View = Record.create_type("View",
    "status",
    "headers",
    "body")
