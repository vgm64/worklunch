from app import app
from flask import request
import socket, errno

import os

app.debug=True

if os.geteuid():
  app.run(host='0.0.0.0', port=5000)
else:
  app.run(host='0.0.0.0', port=80)
