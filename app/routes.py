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


@app.route("/yello_world/<username>")
def yello_world_2(username="World"):
    return "Yo {}".format(username)
