from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = list()

@app.route('/')
def tasks():
    return render_template('tasks.html', todos = todos)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        todo = request.form.get('task')
        todos.append(todo)
        return redirect('/')

@app.route('/remove', methods = ['GET', 'POST'])
def remove():
    if request.method == 'GET':
        return render_template('remove.html')
    else:
        todo = request.form.get('task')
        if todo in todos:
            todos.remove(todo)
        return redirect('/')
