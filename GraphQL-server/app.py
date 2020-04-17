# https://dev.to/mesadhan/python-flask-graphql-with-graphene-nla

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


# ------------------ Graphql Schemas ------------------
from schema import add_url_rules
add_url_rules()


# Flask Rest & Graphql Routes
@app.route('/')
def hello_world():
    return 'Hello From Graphql Tutorial!'

if __name__ == '__main__':
    app.run()

