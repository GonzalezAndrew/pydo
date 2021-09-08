from pydo.util import format_url


def test_format_url():
    """ Test the format_url utility function"""
    base_url = "https://api.digitalocean.com/v2"
    path = "/droplet"
    expected = base_url + path
    assert format_url(base_url=base_url, path=path) == expected

