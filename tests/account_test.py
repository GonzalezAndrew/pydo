import pytest

from pydo import account


@pytest.fixture()
def do():
    return account.Account()


def test_account(do):
    """ Test the account endpoint"""
    account = do.account()
    assert isinstance(account, dict)
