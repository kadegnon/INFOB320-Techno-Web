from flask import Flask
app = Flask(__name__)

def main():
	from app import routes

main()
