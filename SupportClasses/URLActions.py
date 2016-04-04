####################################################################
# Library of URL functions
####################################################################

from urllib import request


class URLActions():
#init with the web address
    def __init__(self, a_web_address):
        self._a_web_address = a_web_address

#opens the url and returns the response
    def open_url(self):
        return request.urlopen(self._a_web_address)

#returns the status code of what the website is returning
    def get_status_code(self):
        return self.open_url().getcode()

    def get_url_response(self):
        if self.get_status_code() != 200:
            print("URL is not responding")
        else:
            return self.open_url()

if __name__ == '__main__':

    url = 'http://www.google.com'
    f = URLActions(url)
    f.open_url()
    print(f.get_status_code())

