from flask import Flask
from flask_restful import Api


app = Flask(__name__)


api = Api(app)
from resources import routes


@app.route('/')
def index():
    return 'index'

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
# https://blog.miguelgrinberg.com/post/restful-authentication-with-flask


### add Authentication Flask-HTTPAuth 
# https://blog.miguelgrinberg.com/post/restful-authentication-with-flask 


### Token based with: "flask_jwt_extended" like in (movie-bag)
# and password Reset
