import controlers.main

url_pattern=[
    (r'/',controlers.main.IndexHandler),
    #(r'/linkdata',handler.main.LinkdataHandler),
    #(r'/feedback',handler.main.FeedbackHandler),
    #(r'/news/([0-9a-z]+)\.html',handler.main.NewsHandler),
    #(r'/test',handler.test.TestHandler),
    #(r'/(staticfile\.txt)',tornado.web.StaticFileHandler,dict(path=settings['static_path'])),
    #(r'.*',handler.common.NotFoundHandler),
]