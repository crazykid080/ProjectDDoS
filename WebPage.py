import flask
from flask import render_template
from init import app

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
	return render_template("index.html",user="Crazykid080",funds=1000")