from flask import Flask, request
from db import *

testDB = ytDB()


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"