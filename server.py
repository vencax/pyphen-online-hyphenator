from flask import Flask
from flask.globals import request
# import base64
# import datetime
import re
import pyphen

app = Flask(__name__)

def removeFalseOcurrences(s, alter):
    """
    Remove all occurences of hyphen sign surrounded by a space-like char.
    """
    return re.sub('\s+(%s)|(%s)\s+' % (alter, alter), ' ', s)


@app.route('/', methods=['GET'])
def hello():
    lang = request.args['lang']
    alter = request.args['alter']
    content = request.args['content']
    dic = pyphen.Pyphen(lang=lang)
    hyphenated = dic.inserted(content, alter)
    return removeFalseOcurrences(hyphenated, alter)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
