from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/2º projeto web')
def hello():
    name = request.args.get('name')
    if not name: #loads the error template
        return render_template('failed.html')
    return render_template('hello.html', name = name)
