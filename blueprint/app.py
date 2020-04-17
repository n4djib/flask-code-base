from flask import Flask, render_template
from products import products_bp


app = Flask(__name__)
app.register_blueprint(products_bp, url_prefix='/products')


@app.route('/')
def index():
    return render_template('view.html')


# url_for()

