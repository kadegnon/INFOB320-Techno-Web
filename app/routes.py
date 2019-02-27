from app import app
from flask import render_template, redirect


@app.route("/")
def yello():
    return "Yello WoOord !"
