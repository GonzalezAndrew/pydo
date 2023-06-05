import json
import os

import requests

from pydo.util import format_url


class Client:
    """
    The base client class for communicating with an API.
    """

    def __init__(self, url: str = 'https://api.digitalocean.com/v2', token: str = None):
        self.url = url
        if token is None:
            self.token = os.getenv('DIGITALOCEAN_TOKEN', None)
        else:
            self.token = token
        self.session = requests.Session()
        self.__set_auth_header()

    def __set_default_header(self) -> None:
        self.session.headers.update({'Accept': 'application/json'})

    def __set_auth_header(self) -> None:
        self.session.headers.update({'Authorization': 'Bearer ' + self.token})

    def _request(self, method: str, base_url: str, path: str, data: dict = {}, header: dict = {}, params: dict = {}):
        if path is not None and base_url is not None:
            url = format_url(self.url, path)
        elif path is not None and base_url is None:
            url = format_url(self.url, path)
        elif path is None:
            raise ValueError('The argument `path` cannot be None.')

        if data is not None:
            data = json.dumps(data)

        if header is not None:
            if not isinstance(header, dict):
                header = json.loads(header)
            self.session.headers.update(header)
        else:
            self.__set_default_header()

        response = self.session.request(method=method, url=url, data=data, headers=self.session.headers, params=params)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise (e)
        except requests.exceptions.RequestException as e:
            raise (e)
        except requests.exceptions.ConnectionError as e:
            raise (e)
        except requests.exceptions.Timeout as e:
            raise (e)

        if response.text != '':
            try:
                _response = response.json()
                while 'next' in response.links.keys():
                    response = self.session.request(method=method, url=response.links['next']['url'], data=data, headers=self.session.headers, params=params)
                    _response.extend(response.json())
                return _response
            except json.decoder.JSONDecodeError:
                return response.text
        else:
            return response.status_code

    def get(self, base_url: str = '', path: str = '', data: dict = {}, header: dict = {}, params: dict = {}):
        return self._request(method='GET', base_url=base_url, path=path, data=data, header=header, params=params)

    def post(self, base_url: str = '', path: str = '', data: dict = {}, header: dict = {}, params: dict = {}):
        return self._request(method='POST', base_url=base_url, path=path, data=data, header=header, params=params)

    def delete(self, base_url: str = '', path: str = '', data: dict = {}, header: dict = {}, params: dict = {}):
        return self._request(method='DELETE', base_url=base_url, path=path, data=data, header=header, params=params)

    def patch(self, base_url: str = '', path: str = '', data: dict = {}, header: dict = {}, params: dict = {}):
        return self._request(method='PATCH', base_url=base_url, path=path, data=data, header=header, params=params)

    def put(self, base_url: str = '', path: str = '', data: dict = {}, header: dict = {}, params: dict = {}):
        return self._request(method='PUT', base_url=base_url, path=path, data=data, header=header, params=params)
