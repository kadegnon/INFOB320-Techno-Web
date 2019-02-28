from app import app
from flask import render_template


@app.route('/todo')
def render_todo():
    return render_template('todo.html')
