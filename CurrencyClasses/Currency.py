####################################################################
#Currency class that sets up specific methods for adding currencies
# together
####################################################################

# Must be created with an amount and a currency code. ✓
# Must equal another Currency object with the same amount and currency code. ✓
# Must NOT equal another Currency object with different amount or currency code. ✓
# Must be able to be added to another Currency object with the same currency code. ✓
# Must be able to be subtracted by another Currency object with the same currency code.✓
# Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency
#      objects with different currency codes. ✓
# Must be able to be multiplied by an int or float and return a Currency object. ✓
# Currency() must be able to take one argument with a currency symbol embedded in it, like
#   "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two
#   arguments, one being the amount and the other being the currency code.

  # handle float/int multiplication
from decimal import *


class Currency():
    """Takes in an amount and currency code"""

    def __init__(self, a_amount, a_currency_code=None):

        # Decimal precision
        getcontext().prec = 2

        self.amount = a_amount
        self.currency_type = a_currency_code.upper()

        if self.currency_type == None:
            pass

    """Overriding the equality method to due a quick test on same currency type"""
    def __eq__(self, other):
        if self.currency_type == other.currency_type:
            if self.amount == other.amount:
                return True
            else:
                return False
        else:
            return False

    """Overriding the addition method to due a quick test on same currency type"""
    def __add__(self, other):
        if self.currency_type == other.currency_type:
            return Currency((Decimal(self.amount) + Decimal(other.amount)), self.currency_type)
        else:
            raise DifferentCurrencyCodeError('Currencies %s and %s were attempted to be added'
                                             % (self.currency_type, other.currency_type))

    """Overriding the subtraction method to due a quick test on same currency type"""
    def __sub__(self, other):
        if self.currency_type == other.currency_type:
            return Currency ((Decimal(self.amount) - Decimal(other.amount)), self.currency_type)
        else:
            raise DifferentCurrencyCodeError('Currencies %s and %s were attempted to be subtracted'
                                             % (self.currency_type, other.currency_type))

    """Overriding the multiplication method to due a quick test on same currency type"""
    def __mul__(self, other):
        if self.currency_type == other.currency_type:
            return Currency ((Decimal(self.amount) * Decimal(other.amount)), self.currency_type)
        else:
            raise DifferentCurrencyCodeError(str('Currencies %s and %s were attempted to be multiplied'
                                                 % (self.currency_type, other.currency_type)))

    """Print variables of a class"""
    def __str__(self):
        return str("This currency class contains %s %s" %(self.currency_type, str(self.amount)))

"""Is raised when two objects of varying currencies are attempted to be added"""
class DifferentCurrencyCodeError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


if __name__ == '__main__':
    f = Currency(5.00004, 'USD')
    d = Currency(9.9, 'USD')
    s = Currency(3, 'GBP')
    print("Result of Add instance f & d")
    print(f + d)
    print("F instance")
    print(f)
    print("D instance")
    print(d)

    print(f == d)
    print(d*f)
    #print(d+s)
    #print(d*s)
