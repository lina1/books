#-*-encoding=utf-8 -*-
__author__ = 'lina'

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

import sys
import os

sys.path.insert(0, os.path.pardir)
# print sys.path

from pattern import v1
#
# class MainHandler(tornado.web.RequestHandler):
#
#     def get(self):
#         self.write("Hello World")
#
# application = tornado.web.Application(handlers=[
#     (r"/", MainHandler)
# ])
#
#
# if __name__ == "__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()

#从命令行中读取设置，给定port，否则使用默认值，参数必须为int
from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    #创建IndexHandler的实例，handler将url和Handler匹配
    app = tornado.web.Application(handlers=v1.handlers)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    #不断处理http请求（loop）
    tornado.ioloop.IOLoop.instance().start()