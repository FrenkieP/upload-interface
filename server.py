from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/')
def index():
  return '<h3>Server Successfully Open</h3>'

app.run()