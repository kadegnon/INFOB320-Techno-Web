from app import app
from flask import render_template, url_for
from flask import request


tasks = []


@app.route('/todo')
def render_todo():
    if('task' in request.args):
        tasks.append(request.args.get('task'))
    if('delete' in request.args and len(tasks) > 0):
        id = int(request.args.get('delete'))
        tasks.pop(id - 1)
    return render_template('todo.html', todos=tasks)


@app.route('/todo', methods=['POST'])
def save_todo():
    if 'task' in request.form:
        tasks.append(request.form.get('task'))
        return(
            """
            New todo saved ! <br />
            <a href=/todo><< Go back</a>
        """)
    return render_todo()
