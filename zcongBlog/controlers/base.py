# encoding=utf8
import tornado.web
import zcongBlog.config as config

class BasicHandler(tornado.web.RequestHandler):
    def initialize(self):
        self._templateLoader=tornado.template.Loader(self.get_template_path())
        self._DynamicValue={
            'title':'米堂兄|宅男腐女怪蜀黍のACG生活宅基地',
            'header':'',
            'error_code':500,
            'domain':'www.mitxiong.com',
            'currentUrl':self.request.uri
        }

    def get(self):
        self.write('Hello World, current mode is '+config.GLOBAL_SETTINGS['Mode'])

    def generate(self,templateFile):
        template = self._templateLoader.load(templateFile)
        self.write(template.generate(**self._DynamicValue))