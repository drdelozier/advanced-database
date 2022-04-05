from bottle import route, run, template, get, post, request, response, redirect

import database


@route('/')
@route('/list')
def get_list():
    shopping_list = database.get_shopping_list()
    return template('shopping_list.tpl', shopping_list=shopping_list)


@get("/add")
def get_add():
    return template('add_item.tpl')


@post("/add")
def post_add():
    description = request.forms.get("description")
    print(f"post was called. description={description}")
    database.add_item(description)
    redirect("/")


@route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/")


@route("/edit/<id>")
def get_edit(id):
    print(id)
    item = database.get_item(id)
    if item == None:
        redirect('/')
    return template('edit_item.tpl', id=item['id'], description=item['desc'])

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    database.update_item(id, description)
    redirect("/list")

run(host='localhost', port=8080)