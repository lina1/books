import logging

__author__ = 'lina'

import requests
from pymongo import MongoClient
import time

# 7999999

class DBApi():

    def __init__(self):
        self.client = MongoClient()

    def connect(self):
        pass

    def query_data(self):
        pass

    def query_data_by_id(self, id):

        try:

            db = self.client.douban

            book = db.books.find_one({"id": str(id)})


            # logging.info(book)

            if book:
                del book["_id"]
                return book

            else:
                return "Book Not Found"
        except Exception, e:
            print e
        finally:
            self.client.close()







