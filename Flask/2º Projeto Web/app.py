from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    number = randint(0, 1)
    return render_template('index.html', number = number)

@app.route('/2º projeto web')
def hello():
    name = request.args.get('name')
    if not name: #loads the error template
        return render_template('failed.html')
    return render_template('hello.html', name = name)
