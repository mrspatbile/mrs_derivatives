import unittest
from datetime import datetime as dt
from src.mrs_derivatives.options import OptionData  

class TestOptionData(unittest.TestCase):

    def test_default_values(self):
        expiration = dt(2025, 1, 30)
        option = OptionData(strike=50, expiration=expiration)
        
        # Test default values
        self.assertEqual(option.strike, 50)
        self.assertEqual(option.expiration, expiration)
        self.assertEqual(option.what, 'call')  # Default 'what' should be 'call'
        self.assertEqual(option.multiplier, 100)  # Default multiplier should be 100

    def test_custom_values(self):
        expiration = dt(2025, 1, 30)
        option = OptionData(strike=50, expiration=expiration, what='put', multiplier=200)
        
        # Test custom values
        self.assertEqual(option.strike, 50)
        self.assertEqual(option.expiration, expiration)
        self.assertEqual(option.what, 'put')  # Custom 'what' should be 'put'
        self.assertEqual(option.multiplier, 200)  # Custom multiplier should be 200

if __name__ == '__main__':
    unittest.main()