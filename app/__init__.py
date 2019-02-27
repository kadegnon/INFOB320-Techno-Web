from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


def main():
    from app import routes


main()
