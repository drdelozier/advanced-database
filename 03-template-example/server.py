from bottle import route, run, template, get, post, request, response, redirect
import bottle

# bottle.TEMPLATE_PATH.insert(0, '/Users/greg/Projects/advanced-database/example/views')
# bottle.TEMPLATE_PATH.insert(0, 'views')

@route('/')
@route('/hello')
def get_hello():
    return template('hello.tpl')

run(host='localhost', port=8080)