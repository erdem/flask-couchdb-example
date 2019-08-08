import connexion
from connexion.resolver import RestyResolver

import flask_injector

from app.products.models import Products
from app.utils import get_config
from flaskext.couchdb import CouchDBManager


INJECTOR_DEFAULT_MODULES = dict(
    db_manager=CouchDBManager,
)


def create_app(config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    from app.products.views import products_api

    connexion_app = connexion.FlaskApp(__name__, specification_dir='openapi/', **kwargs)
    app = connexion_app.app

    try:
        app.config.from_object(get_config(config_name))
    except ImportError:
        raise Exception('Invalid Config')

    connexion_app.add_api('products-api-docs.yaml', resolver=RestyResolver('products'))
    app.register_blueprint(products_api, url_prefix='/v1.0/api/products/')

    managet = CouchDBManager()
    managet.add_document(Products)
    managet.setup(app)
    flask_injector.FlaskInjector(app=app, modules=INJECTOR_DEFAULT_MODULES.values())
    app.run(port=8080)

    return app

