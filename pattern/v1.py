from api.book import BookHandler
from api.books import BooksHandler

__author__ = 'lina'

handlers = [(r"/books/(\d+)", BooksHandler),
            (r"/book/(\d+)", BookHandler)]