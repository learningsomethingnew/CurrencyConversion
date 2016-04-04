####################################################################
#Main class that drives the interactions of the currency exchanges
####################################################################

from SupportClasses.URLActions import URLActions
from CurrencyClasses.CurrencyConverter import CurrencyConverter

class Main():
    def __init__(self):
        self._currency_url = "http://api.fixer.io/latest?base=USD"

        #init the classes
        u = URLActions(self._currency_url)

        #pulls url for currency json
        currency_dict = u.open_read__decode_return_json()



    def main(self):
        pass


if __name__ == '__main__':

    f = Main()
