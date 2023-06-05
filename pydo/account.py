from pydo.client import Client


class Account(Client):
    def __init__(self):
        super().__init__()

    def account(self):
        """To show information about the current user account.
        :return: A JSON object keyed on account with an excerpt of the current user account data.
        :rtype: dict{}

        Example:
            {
            "account": {
                "droplet_limit": 25,
                "floating_ip_limit": 5,
                "email": "sammy@digitalocean.com",
                "uuid": "b6fr89dbf6d9156cace5f3c78dc9851d957381ef",
                "email_verified": true,
                "status": "active",
                "status_message": " "
                }
            }
        """
        return self.get(path='/account')
