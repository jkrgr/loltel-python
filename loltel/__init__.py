__version__ = '0.1'


import requests
import os
from platform import python_version


class Error(Exception):
    pass


class ClientError(Error):
    pass


class ServerError(Error):
    pass


class AuthenticationError(ClientError):
    pass


class Client():

    def __init__(self):
        self.api_key = os.environ.get('LOLTEL_ACCESS_TOKEN')
        self.msisdn = os.environ.get('LOLTEL_MSISDN')
        self.api_host = 'https://loltelapi.com/api/'

        user_agent = 'loltel-python/{0}/{1}'.format(__version__, python_version())

        self.headers = {'User-Agent': user_agent,
                        'Authorization': "Bearer $s" % self.api_key
                        }

    def do_req(self, data=None, method='get', path=''):
        assert method in ['get', 'post'], 'HTTP method must be either `get` or `post`.'

        url = self.api_host + path
        r = getattr(requests, method)

        res = r(url, json=data, headers=self.headers)
        # TODO: check response, throw errors, prepare result

        return res

    def send_sms(self, message='', to=''):
        """ Send SMS to phone number.
        :param message: Message to send
        :param to: Phone number (MSISDN) to send to
        :return: Response object containing `status`, `error_code` and `error`
        """

        data = { "to_msisdn": to,
                 "message": message}

        res = self.do_req(data=data, method='post', path='sms')
        return res

    def search_sms(self, starts_with='', contains='', sender='', max_results=50):
        """ Search in SMS inbox.
        :param starts_with: The text that the SMS starts with
        :param contains: Text that the SMS contains
        :param sender: Phone number of the SMS sender
        :param max_results: Maximum search result hits (deafult=50)
        :return:
        """


        data = {"starts_with": starts_with,
                "contains_substring": contains,
                "from_number": sender,
                "limit": max_results}

        res = self.do_req(data=data, method='post', path='sms/search')

    def search_call(self):
        pass

    def register_webhook(self):
        pass

    def delete_webhook(self):
        pass

    def list_webhook(self):
        pass


