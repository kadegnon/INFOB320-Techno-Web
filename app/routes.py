from app import app
from flask import render_template, redirect


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
