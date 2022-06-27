import os
from flask import flask
app = Flask(__name__)

@app.route("/)
def main():
	return "Welcome"

@app.route("/)
def hello():
	return "I am good!Thankyou"

if __name__ == "__main__":
	app.run()
