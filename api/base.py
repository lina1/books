# coding=utf-8
import tornado.web

__author__ = 'lina'

# 处理请求时，将类实例化，定义的get函数代表处理http的get请求，write表示http响应


class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)


    # def prepare(self):
    #     self._prepare_context()

    def data_received(self, chunk):
        pass

