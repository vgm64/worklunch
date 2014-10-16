from flask import render_template, request, jsonify
#from flask import redirect, url_for, send_from_directory
from app import app
import sqlite3
import json
import os

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
  db = request.args.get('db')
  if not db.endswith('.db'):
    db += '.db'
  # The default database shouldn't save markers added.
  if data=='default':
    pass
  #import pdb; pdb.set_trace();
  # TODO Create a response if the db doesn't exist to inform user.
  db_path = "app/static/" + db

  #if not os.path.exists("db_path"):
    #return
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  c.execute("CREATE TABLE geolocs (loc text)")
  print data, repr(data)
  c.execute("INSERT INTO geolocs VALUES (?)", (data,))
  conn.commit()

  print "Request Args:", request.args
  print data, type(data)
  print jsonify(result=data)
  return jsonify(result=str(data))
