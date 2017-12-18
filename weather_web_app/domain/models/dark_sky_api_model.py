from pyrecord import Record

DarkSkyRequest = Record.create_type("DarkSkyrequest",
    "latitude",
    "longitude",
    latitude=None,
    longitude=None)
