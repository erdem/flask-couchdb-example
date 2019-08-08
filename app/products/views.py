from http import HTTPStatus

from flask import Blueprint, jsonify, request

from app import Products


products_api = Blueprint('products_api', __name__)


@products_api.route('/', methods=['GET'])
def get_products():
    products = Products.all()
    response_data = []
    for product in products:
        d = {
            'id': product.id,
            'prodname': product.name,
            'category': product.category,
            'quantity': product.quantity,

        }
        response_data.append(d)

    return jsonify(response_data), HTTPStatus.OK


@products_api.route('/', methods=['POST'])
def create_product():
    request_data = request.get_json()
    product_data = dict(
        name=request_data.get('prodname'),
        category=request_data.get('category'),
        quantity=request_data.get('quantity')
    )
    product = Products(**product_data)
    product.store()
    return HTTPStatus.CREATED


@products_api.route('/<string:product_id>/', methods=["GET"])
def retrieve_product(product_id):
    product = Products.load(id=product_id)
    if not product:
        return jsonify({
            'error': 'Product not found.'
        }), HTTPStatus.BAD_REQUEST

    response_data = {
        'id': product.id,
        'prodname': product.name,
        'category': product.category,
        'quantity': product.quantity,
    }
    return response_data, HTTPStatus.OK
