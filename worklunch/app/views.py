from flask import render_template, request, redirect, url_for, send_from_directory
from app import app
import sqlite3

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
