from flask import Flask, current_app
from blinker import Namespace

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


event_signals = Namespace()
speakers_modified = event_signals.signal('event_json_modified')



@app.route('/')
def index():
    speakers_modified.send(current_app._get_current_object(), event_id='123')
    return 'index'


@speakers_modified.connect
def name_of_signal_handler(app, **kwargs):
    print('aaaaaaaaaaaaaaaa ' + app.config['SECRET_KEY'])
    print('aaaaaaaaaaaaaaaa ' + kwargs['event_id'])
    print('aaaaaaaaaaaaaaaa')
