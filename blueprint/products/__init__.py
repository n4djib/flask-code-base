from flask import Blueprint


products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')


from products import routes
