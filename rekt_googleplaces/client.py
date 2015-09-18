import rekt
from rekt.utils import load_builtin_config
from rekt_googlecore import GoogleAPIClient

from . import specs

__all__ = ['GooglePlacesClient']

_API_KEY_ARG_NAME = 'key'

_googleplaces = rekt.load_service(load_builtin_config('googleplaces', specs.__name__))

class GooglePlacesClient(GoogleAPIClient):
    def __init__(self, api_key):
        GoogleAPIClient.__init__(self, _googleplaces, api_key)
