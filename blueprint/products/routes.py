from flask import render_template
from products import products_bp

@products_bp.route('/')
def index():
    return render_template('products/view.html')

