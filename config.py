import os


class BaseConfig:
    DEBUG = False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


class LocalConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    DOMAIN = 'http://localhost:5000'
    COUCHDB_SERVER = 'http://localhost:5984/'
    COUCHDB_DATABASE = 'product'
    SECRET_KEY = 'set this to something secret'
