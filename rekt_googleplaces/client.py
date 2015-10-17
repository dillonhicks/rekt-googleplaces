from requests.exceptions import HTTPError

import rekt
from rekt.httputils import HTTPStatus
from rekt.utils import load_builtin_config
from rekt_googlecore import GoogleAPIClient

from . import specs
from . import errors

__all__ = ['GooglePlacesClient']

_googleplaces = rekt.load_service(load_builtin_config('googleplaces', specs.__name__))

class GooglePlacesClient(GoogleAPIClient):
    def __init__(self, api_key):
        GoogleAPIClient.__init__(self, _googleplaces, api_key)

    def get_photo2(self, **kwargs):
        """
        The get_photo api is not consistent with the rest of the places
        api. This method tries to make it a bit more consistent by
        returning an actual api error instead of the raw requests 400.
        """

        try:
            return self.get_photo(**kwargs)
        except HTTPError as e:
            if e.response.status_code == HTTPStatus.BAD_REQUEST:
                raise errors.InvalidRequestError('get_photo2', kwargs, None, None) from e
            raise


