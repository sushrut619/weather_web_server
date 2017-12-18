from aglyph.binder import Binder
from aglyph.component import Reference
import logging
import logging.handlers


class ContainerFactory:
    def build_components(self, config):
        container = Binder()

        (container.bind("Config", to=dict).init(config))

        # Loggers
        logger = self.build_logger(config)

        # controller
        (container.bind("weather_controller", to="weather_web_app.app.controller.Controller")
            .init(
                logger,
                Reference("app.RequestDomFactory"),
                Reference("app.request_model_factories.WeatherModelFactory"),
                Reference("domain.services.WeatherService"),
                Reference("views.ViewFactory")
            ))

        # app model factories
        (container.bind("app.request_model_factories.WeatherModelFactory",
                        to="weather_web_app.app.request_model_factories.weather_model_factory.WeatherModelFactory"))

        # domain services
        (container.bind("domain.services.WeatherService", to="weather_web_app.domain.services.weather_service.WeatherService")
            .init(
                Reference("logistics.DarkSkyApiFactory"),
                Reference("Config"),
                logger,
                Reference("domain.factories.ValidationFactory"),
                Reference("domain.factories.WeatherServiceFactory")
            ))

        # domain factories
        (container.bind("domain.factories.ValidationFactory",
                        to="weather_web_app.domain.factories.validation_factory.ValidationFactory"))
        (container.bind("domain.factories.WeatherServiceFactory",
                        to="weather_web_app.domain.factories.weather_service_factory.WeatherServiceFactory"))

        # api factories
        (container.bind("logistics.DarkSkyApiFactory",
                        to="weather_web_app.logistics.dark_sky_api_factory.DarkSkyApiFactory")
                  .init(
                    Reference("Config"),
                    logger))

        # request_dom_factory
        (container.bind("app.RequestDomFactory",
                        to="weather_web_app.app.request_dom_factory.RequestDomFactory")
                  .init(logger))

        # view factory
        (container.bind("views.ViewFactory",
                        to="weather_web_app.view.view_factory.ViewFactory"))

        return container

    def build_logger(self, config):
        logger = logging.getLogger(config.get('app_logger'))

        fh = logging.handlers.RotatingFileHandler(config.get('log_file_path'), maxBytes=50000, backupCount=3)
        fh.setLevel(getattr(logging, config.get('file_log_level').upper() if "file_log_level"
                                                                             in config else "INFO", logging.INFO))

        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, config.get('console_log_level').upper() if "console_log_level"
                                                                                in config else "DEBUG", logging.DEBUG))

        # create a formatter for log
        # lf = logging.Formatter('%(levelname)s : %(filename)s : %(funcName)s : %(lineno)d : %(message)s')
        lf = logging.Formatter('{levelname} : {filename} : {funcName} : {lineno} : {message}', style='{')
        fh.setFormatter(lf)
        ch.setFormatter(lf)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger
