####################################################################
# Library of URL functions
####################################################################

from urllib.request import urlopen
from json import loads
import pickle


class URLActions():
    """init with the web address"""
    def __init__(self, a_web_address):
        self._a_web_address = a_web_address

    """Tests and returns URLs response code"""
    def get_site_status_code(self):
        return urlopen(self._a_web_address).getcode()

    """Open a url, read it, and decode it. Returns JSON dict"""
    def open_read__decode_return_json(self):
        data = urlopen(self._a_web_address).read().decode('utf8')
        return loads(data)

    def save_to_file(self):
        data = self.open_read__decode_return_json()
        pickle.dump(data, open("currencies.p", "wb"))



if __name__ == '__main__':

    url = 'http://api.fixer.io/latest?base=USD'
    f = URLActions(url)
    print(f.get_site_status_code())
    f.save_to_file()
