class ValidationFactory:
    def validate_coordinates(self, logger, model):
        # check if either of the corrdinates are null
        if model.latitude is None or model.longitude is None:
            return False

        # convert latitude to decimal and return false if failed
        try:
            model.latitude = float(model.latitude)
        except ValueError as e:
            logger.info("Cannot convert latitude value to decimal", e)
            return False

        try:
            model.longitude = float(model.longitude)
        except ValueError as e:
            logger.info("Cannot convert longitude value to decimal", e)
            return False

        if model.latitude > 90 or model.latitude < -90:
            return False
        if model.longitude > 180 or model.longitude < -180:
            return False

        # else if all the validation checks passed
        return True
