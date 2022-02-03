from bottle import route, run, template
import sqlite3

connection = sqlite3.connect("shopping_list.db")

@route('/list')
def get_list():
    global connection
    cursor = connection.cursor()
    items = cursor.execute("select id, description from list")
    items = list(items)
    shopping_list = [{"id":item[0], "desc":item[1]} for item in items]
    return template('shopping_list.tpl', shopping_list=shopping_list)


@route("/delete/<id>")
def get_delete(id):
    return template('confirm_delete.tpl', id=id)


run(host='localhost', port=8080)