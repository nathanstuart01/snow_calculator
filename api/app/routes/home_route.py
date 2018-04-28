from flask import jsonify, request
from app import app

@app.route('/')
@app.route('/index')
def home_page():
	return "Home page for all the Utah snow information you need to know"


