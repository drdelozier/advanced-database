from mongita import MongitaClientDisk
client = MongitaClientDisk()
from bson.objectid import ObjectId

def setup_shopping_list():
    try:
        shopping_db = client.shopping_db
        shopping_list = shopping_db.shopping_list
        shopping_list.delete_many({})
        items = [
            {"desc":"apples", "quantity":12, "variety":"golden delicious" },
            {"desc":"broccoli", "quantity":4},
            {"desc":"pizza", "quantity":1, "toppings":"cheese, pepperoni"},
            {"desc":"tangerine", "quantity":3},
            {"desc":"potatoes", "quantity":6},
            ]
        shopping_list.insert_many(items)
    finally:
        pass

def get_shopping_list():
    try:
        shopping_db = client.shopping_db
        shopping_list = shopping_db.shopping_list
        the_list = list(shopping_list.find({}))
        for item in the_list:
            item['id'] = str(item['_id'])         
        return the_list
    finally:
        pass

def add_item(item):
    try:
        shopping_db = client.shopping_db
        shopping_list = shopping_db.shopping_list
        shopping_list.insert_one({"desc":item})
    finally:
        pass

def delete_item(id):
    try:
        shopping_db = client.shopping_db
        shopping_list = shopping_db.shopping_list
        _id = ObjectId(id)
        shopping_list.delete_one({"_id":_id})
    finally:
        pass

def update_item(id, description):
    try:
        shopping_db = client.shopping_db
        shopping_list = shopping_db.shopping_list
        _id = ObjectId(id)
        shopping_list.update_one({"_id":_id},{'$set':{'desc':description}})
    finally:
        pass
