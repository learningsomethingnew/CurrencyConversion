import unittest
from CurrencyClasses.Currency import Currency


class TestWordFrequency(unittest.TestCase):

    def __init__(self):
        self.currency1 = Currency(5, 'USD')
        self.currency2 = Currency(9, 'USD')
        self.currency3 = Currency(5, 'USD')
        self.currency4 = Currency(20, 'GBP')

    def test_assert_true(self):
        self.assertEqual((self.currency1+self.currency2), 14)

    def test_assert_false(self):
        self.assertFalse(my_module.is_false())

    def test_assert_equal(self):
        self.assertEqual(my_module.get_one(), 1)

    def test_assert_not_equal(self):
        self.assertNotEqual(my_module.get_one(), 0)


if __name__ == '__main__':
    unittest.main()