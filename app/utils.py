import os

from werkzeug.utils import import_string

CONFIG_NAME_MAPPER = {
    'development': 'config.LocalConfig',
}


def get_config(config_name=None):
    flask_config_name = os.getenv('FLASK_CONFIG', 'development')
    if config_name is not None:
        flask_config_name = config_name
    return import_string(CONFIG_NAME_MAPPER[flask_config_name])
