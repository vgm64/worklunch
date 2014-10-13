# imports
from flask import Flask

# Creates our application.
app = Flask(__name__)

app.debug = True

# DATABASE SETTINGS
from app import views
