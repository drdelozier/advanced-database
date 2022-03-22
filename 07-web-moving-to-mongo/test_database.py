# tests for database abstraction layer

import database

def test_setup_shopping_list():
    print("testing setup_shopping_list...")
    database.setup_shopping_list()
    shopping_list = database.get_shopping_list()
    assert type(shopping_list) is list
    assert len(shopping_list) > 0, "The shopping list has no items in it."
    items = [item['desc'] for item in shopping_list]
    assert "apples" in items
    assert "potatoes" in items
    assert shopping_list[-1]['quantity'] == 6

def test_get_shopping_list():
    print("testing get_shopping_list...")
    shopping_list = database.get_shopping_list()
    assert type(shopping_list) is list
    assert len(shopping_list) > 0, "The shopping list has no items in it."
    for item in shopping_list:
        assert type(item) is dict
        assert "id" in item
        assert "desc" in item

import string, random

def test_add_item():
    print("testing add_item...")
    new_item = "".join(random.choices(string.ascii_letters,k=14))
    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        assert item['desc'] != new_item
    database.add_item(new_item)
    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        if item['desc'] == new_item:
            # print("ITEM = ",item)
            database.delete_item(item['id'])
            return
    assert False, "The item was not apparently added to the shopping list"

def test_delete_item():
    print("testing delete_item...")
    new_item = "".join(random.choices(string.ascii_letters,k=14))
    database.add_item(new_item)
    shopping_list = database.get_shopping_list()
    id = None
    for item in shopping_list:
        if item['desc'] == new_item:
            id = item['id']
    assert id != None, "id of new item not found"
    database.delete_item(id)
    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        assert item['id'] != id, "id of deleted item still found in database"
        assert item['desc'] != new_item, "deleted item still found in database"

def test_update_item():
    print("testing update_item...")
    new_item = "".join(random.choices(string.ascii_letters,k=14))
    database.add_item(new_item)
    shopping_list = database.get_shopping_list()
    id = None
    for item in shopping_list:
        if item['desc'] == new_item:
            id = item['id']
    assert id != None, "id of new item not found"
    new_name = "".join(random.choices(string.ascii_letters,k=14))
    database.update_item(id, new_name)
    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        if item['id'] == id:
            assert item['desc'] == new_name, "id was not updated with new name"
        database.delete_item(id)

def test_get_item():
    print("testing get_item...")
    shopping_list = database.get_shopping_list()
    id = shopping_list[0]["id"]
    desc = shopping_list[0]["desc"]
    item = database.get_item("1a2a3a1a2a3a1a2a32aa2a3a")
    assert item == None
    item = database.get_item("1a2a3a1a2a3a1a2")
    item = database.get_item(id)
    assert type(item) is dict
    assert "id" in item
    assert "desc" in item
    assert item['id'] == id
    assert item['desc'] == desc

if __name__ == "__main__":
    test_setup_shopping_list()
    test_get_shopping_list()
    test_add_item()
    test_delete_item()
    test_update_item()
    test_get_item()
    print("done.")