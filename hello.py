from flask import Flask
from flask import url_for
from flask import request
import json

app = Flask(__name__)

db = {
  'id1': 12334534,
  'id2': 123534534,
  'id3': 14353423,
}


def do_num(a):
    return json.dumps({'result': db[a]})


# {"result": True}


def del_num(b):
    if b in db:
        del(db[b])
        return json.dumps({'result': True})
    else:
        return json.dumps({'result': False})


def post_num(c):
    if c in db:
        if db[c] == request.json[c]:
            return json.dumps({'result': False})
        else:
            db[c] = request.json[c]
            return json.dumps({'result': True})
    else:
        db[c] = request.json[c]
        return json.dumps({'result': True})


@app.route('/hello/<path:id_num>', methods=['GET', 'DELETE', 'POST'])
def ind(id_num):
    # print(id)
    print(request.json)
    # print(request.args.get('id'))
    if request.method == 'GET':
        return do_num(id_num)
    elif request.method == 'DELETE':
        return del_num(id_num)
    else:
        return post_num(id_num)


    # if request.method == 'POST':
    #     do_the_login()
    # else:
    #     # show_the_login_form()
    #     pass


@app.route('/')
def index():
    return 'Index page'


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/projects')
def projects():
    return 'Страница в проекте'

@app.route('/hello/about')
def about():
    return 'О другом'

if __name__ == '__main__':
    app.run()