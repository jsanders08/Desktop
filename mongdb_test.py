from pymongo import MongoClient

url = "mongodb://admin:admin@cluster0-shard-00-00.b75yo.mongodb.net:27017,cluster0-shard-00-01.b75yo.mongodb.net:27017,cluster0-shard-00-02.b75yo.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-11zqk8-shard-0&authSource=admin&retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())

print("end of program, press any key to terminate...")