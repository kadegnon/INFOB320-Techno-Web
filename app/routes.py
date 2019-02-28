from app import app
from flask import render_template, url_for
from flask import request


tasks = []


@app.route('/todo')
def render_todo():
    return render_template('todo.html')


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
