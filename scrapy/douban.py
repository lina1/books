__author__ = 'lina'

import requests
from pymongo import MongoClient
import time

# 7999999


for i in range(1023004, 2000001):

    url = "https://api.douban.com/v2/book/%s" % i

    headers = dict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15"

    headers["X-Forward-For"] = "61.148.231.96"
    resp = requests.get(url, headers=headers)

    status_code = resp.status_code

    if(status_code == 403):
        print "BLOCKED......"
        break
    text = resp.text
    text_dict = eval(text)
    # text_dict["item_id"] = i


    if(text_dict.has_key("code")):
        if text_dict.get("code") == 6000:
            continue
        if text_dict.get("code") == 1998:
            break
    client = MongoClient()
    db = client.douban


    result = db.books.insert_one(text_dict)
    # client.close()

    print i





