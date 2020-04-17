from flask import Flask, render_template
from flask_mail import Mail, Message
from datetime import datetime


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


mail = Mail(app)

from mail import send_email


@app.route('/')
def index():
    send_email('Hey there - '+str(datetime.now()),
      sender='**************',
      recipients=['n4djib@gmail.com'],
      text_body=render_template('email/text_.txt', url='google.com'),
      html_body=render_template('email/html_.html', url='google.com')
    )

    return 'index mail - '+str(datetime.now())
    
    
    