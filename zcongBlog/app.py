import tornado.ioloop
import tornado.web
import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
try:
    import zcongBlog
except ImportError:
    import sys
    sys.path.append(os.path.join(ROOT_PATH,'..'))
    import zcongBlog

import zcongBlog.config as config
import zcongBlog.routes as routes

def run(port=config.GLOBAL_SETTINGS['Default_Port']):
    application=tornado.web.Application(routes.url_pattern,**config.TORNADO_SETTINGS)
    application.listen(port)
    print port
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()

if __name__ =="__main__":
    import sys
    if len(sys.argv)>1 :
        run(int(sys.argv[1]))
    else:
        run()