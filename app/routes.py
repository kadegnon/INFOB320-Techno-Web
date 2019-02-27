from app import app
from flask import render_template, redirect
from flask import url_for, request
from flask import flash

import os
from werkzeug.utils import secure_filename

from app.upload_file import allow_file
from app.config import Config


@app.route("/")
def yello():
    return """
        <!DOCTYPE html> 
        <html> 
            <head>
                <title>YOLO</title>
            </head>
            <body>
                <h1>Yello WoOord !</h1>
            </body> 
        </html>
    """


@app.route("/yello_world_2/<username>")
def yello_2(username="World"):
    return "Yo {}".format(username)


@app.route("/yello_world_3/<string(length=8):username>")
def yello_3(username="World"):
    return "Yo {}".format(username)


@app.route("/yello_world_4/<string(minlength=4, maxlength=8):username>")
def yello_4(username="World"):
    return "Yo {}".format(username)


@app.route("/yello_world_5/<int:userid>")
def yello_id(userid=123):
    return "Yo your ID is #{:d}".format(userid)


@app.route("/yello_world_6")
def yello_6(name="", surname=""):
    name = request.args.get("name")
    surname = request.args.get("surname")
    return "The quick brown fox ({})  jumps over the lazy dog ({})  --> {}".format(name, surname, type(name).__name__)


@app.route('/yello_world')
def yello_world():
    return render_template('yello.html')


@app.route('/my_form', methods=['GET', 'POST'])
def process_request():
    if(request.method == "POST"):
        _username = request.form['username']
        if _username:
            return render_template('process_response.html', response=_username)
        else:
            return "WHERE is the fu**ing name ?!", 400
    else:
        return render_template('process_form.html')


@app.route('/uploaded_file')
def uploaded_file():
    return 'File uploaded :-)'


@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file send')
            return redirect(request.url)
        send_file = request.files['file']
        if send_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if send_file and allow_file(send_file.filename):
            file_name = secure_filename(send_file.filename)
            send_file.save(os.path.join(Config.UPLOAD_DIR, file_name))
            return redirect(url_for('uploaded_file', file_name=file_name))
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Upload new File</title>
        </head>
        <body>
            <h1>Send me a new file</h1>
            <form method=post enctype=multipart/form-data>
                <input type=file name=file>
                <input type=submit value=Upload>
            </form> 
        </body>
        </html>
    """
