from pydo.client import Client


def test_client():
    """ Test base client class """
    expected_url = 'https://api.digitalocean.com/v2'
    do = Client(url=expected_url, token='fake-token')
    assert do.url == expected_url
