import types
from itertools import chain
from pathlib import Path, PurePath

from pkg_resources import resource_filename

import rekt
from rekt.service import RestClient
from rekt.utils import load_config, api_method_names
from rekt_googlecore import GoogleAPIClient

from . import specs

__all__ = ['GooglePlacesClient']

_API_KEY_ARG_NAME = 'key'

def _load_builtin_config():
    config_path = Path(next(iter(specs.__path__)))
    config_path = config_path / PurePath(resource_filename('rekt_googleplaces.specs', 'googleplaces.yaml'))
    return load_config(config_path)

_googleplaces = rekt.load_service(_load_builtin_config())

class GooglePlacesClient(GoogleAPIClient):
    def __init__(self, api_key):
        GoogleAPIClient.__init__(self, _googleplaces, api_key)
