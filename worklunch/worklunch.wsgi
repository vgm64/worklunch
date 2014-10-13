import sys, os
cur_file = os.path.abspath(__file__)
path = os.path.dirname(cur_file)
sys.path.insert(0, path)
from app import app as application
