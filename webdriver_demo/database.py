import dataset

db = dataset.connect("sqlite:///shopping_list.db")

def setup_shopping_list():
    try:
        db.begin()
        db['list'].drop()
        table = db['list']
        items = [
            {"description":"apples", "quantity":12, "variety":"golden delicious" },
            {"description":"broccoli", "quantity":4},
            {"description":"pizza", "quantity":1, "toppings":"cheese, pepperoni"},
            {"description":"tangerine", "quantity":3},
            {"description":"potatoes", "quantity":6},
            ]
        # for item in items:
        #     table.insert(item)
        table.insert_many(items)
        db.commit()
    except Exception as e:
        db.rollback()


def get_shopping_list():
    items = [dict(item) for item in db['list'].find()]
    shopping_list = [{"id":item['id'], "desc":item['description']} for item in items]
    return shopping_list

def add_item(item):
    db['list'].insert({"description":item})

def delete_item(id):
    db['list'].delete(id=id)

def update_item(id, description):
    db['list'].update({'id':id, 'description':description},['id'])
