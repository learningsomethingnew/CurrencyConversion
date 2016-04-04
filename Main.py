####################################################################
#Main class that drives the interactions of the currency exchanges
####################################################################

from SupportClasses.URLActions import URLActions
from SupportClasses.JSONActions import JSONActions

class Main():
    def __init__(self):
        self._currency_url = "http://api.fixer.io/latest?base=USD"

        url = URLActions.open_url(self._currency_url)
        print(url)


    def main(self):
        pass