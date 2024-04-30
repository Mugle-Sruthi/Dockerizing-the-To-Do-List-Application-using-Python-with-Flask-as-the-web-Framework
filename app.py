from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample to-do list
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todo_list.append(task)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if task_id < len(todo_list):
        todo_list.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '_main_':
    app.run(debug=True)