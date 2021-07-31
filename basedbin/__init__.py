from flask import Flask

app = Flask(__name__)

from basedbin import routes
