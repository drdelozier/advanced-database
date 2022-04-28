import pymongo

client = pymongo.MongoClient("mongodb+srv://new_user:new_password@soliton.zk5ax.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.sample_restaurants

restaurants = db.restaurants

print(restaurants.find_one())

# exercise 1: display all documents in restaurant

# for result in restaurants.find()[0:100]:
#     print(result)

# exercise 2: display the fields restaurant_id, name, borough and cuisine for all the documents

for result in restaurants.find({},{'_id':0, 'name':1, 'borough':1})[0:100]:
    print(result)
