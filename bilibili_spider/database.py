import pymongo
from scrapy.conf import settings

if settings.get("MONGO_USERNAME") == "" and settings.get("MONGO_PASSWORD") == "":
    connection = pymongo.MongoClient(
        f'mongodb://{settings.get("MONGO_HOST")}:{settings.get("MONGO_PORT")}')
else:
    connection = pymongo.MongoClient(
        f'mongodb://{settings.get("MONGO_USERNAME")}:{settings.get("MONGO_PASSWORD")}@{settings.get("MONGO_HOST")}:{settings.get("MONGO_PORT")}')

db = connection[settings.get("MONGO_DATABASE")]
