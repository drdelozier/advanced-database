import pymongo

client = pymongo.MongoClient("mongodb+srv://new_user:new_password@soliton.zk5ax.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.sample_restaurants

restaurants = db.restaurants

print(restaurants.find_one())
