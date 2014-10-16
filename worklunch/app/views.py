from flask import render_template, request, jsonify
#from flask import redirect, url_for, send_from_directory
from app import app
import sqlite3
import json

# ROUTING/VIEW FUNCTIONS
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/_read_db', methods=['GET'])
def _read_db():
  #conn = sqlite3.connect("static/records.db")
  #c = conn.cursor()
  import random
  return str(random.random())

@app.route('/_add_to_db', methods=['GET'])
def _add_to_db():
  data = request.args.get('data')
  print "Request Args:", request.args
  print data, type(data)
  print jsonify(result=data)
  return jsonify(result=str(data))
