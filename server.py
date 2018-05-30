from flask import Flask
from flask.globals import request
# import base64
# import datetime
# import os
import pyphen

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    lang = request.args['lang']
    alter = request.args['alter']
    content = request.args['content']
    dic = pyphen.Pyphen(lang=lang)
    hyphenated = dic.inserted(content, alter)
    return hyphenated

if __name__ == '__main__':
    app.run(host='0.0.0.0')
