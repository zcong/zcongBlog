import base
import zcongBlog.config as config

class IndexHandler(base.BasicHandler):
    def get(self):
        self._DynamicValue['body'] = 'shit';
        self.generate('index.html')