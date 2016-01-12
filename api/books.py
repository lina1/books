# coding=utf-8
import tornado.web

from api.base import BaseHandler
from models.book_model import BookModel

__author__ = 'lina'

# 处理请求时，将类实例化，定义的get函数代表处理http的get请求，write表示http响应


class BooksHandler(BaseHandler):

    def __init__(self, application, request, **kwargs):
        super(BooksHandler, self).__init__(application, request, **kwargs)
        self.book_model = BookModel()

    def get(self, page=1):
        # self.write("Hello World")
        self.write(self.book_model.get_books())
