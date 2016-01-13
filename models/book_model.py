from db.db_api import DBApi

__author__ = 'lina'


class BookModel():

    def __init__(self):
        pass

    def get_books(self):
        data = {"a": "c"}
        return data

    def get_book(self, id):
        db = DBApi()
        return db.query_data_by_id(id)
