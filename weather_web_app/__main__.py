from weather_web_app.utils.arguments_factory import parse_arguments
from weather_web_app.utils.config_factory import build_config
from os import path
import cherrypy
from weather_web_app.app.router import Router

args = parse_arguments()
config = build_config(args.config_path)

router = Router(config)
application = router.serve

# mount the application
cherrypy.tree.graft(application, "/")

# unsubscribe from default server
cherrypy.server.unsubscribe()

# use CherryPy's signal handling
cherrypy.engine.signals.subscribe()

# instantiate a new server
server = cherrypy._cpserver.Server()

port = config.get('port') or 8080
thread_pool = config.get('thread_pool') or 4

#configure the server object
server.socket_host = "0.0.0.0"
server.socket_port = port
server.thread_pool = thread_pool

# subscribe the server
server.subscribe()

cherrypy.engine.start()
cherrypy.engine.block()
