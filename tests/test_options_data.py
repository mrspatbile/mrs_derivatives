import unittest
from datetime import date
from src.mrs_derivatives.options_data import InstrumentData, MarketData

class TestOptionData(unittest.TestCase):

    def test_default_values(self):
        expiration = date(2025, 1, 30)
        option = InstrumentData(strike=50, expiration=expiration)
        
        # Test default values
        self.assertEqual(option.strike, 50)
        self.assertEqual(option.expiration, expiration)
        self.assertEqual(option.what, 'call')  # Default 'what' should be 'call'
        self.assertEqual(option.multiplier, 100)  # Default multiplier should be 100

    def test_custom_values(self):
        expiration = date(2025, 1, 30)
        option = InstrumentData(strike=50, expiration=expiration, what='put', multiplier=200)
        
        # Test custom values
        self.assertEqual(option.strike, 50)
        self.assertEqual(option.expiration, expiration)
        self.assertEqual(option.what, 'put')  # Custom 'what' should be 'put'
        self.assertEqual(option.multiplier, 200)  # Custom multiplier should be 200

    
    def test_invalid_what(self):
        # Test invalid 'what' value
        with self.assertRaises(ValueError) as context:
            InstrumentData(strike=50, expiration=date(2025, 1, 30), what='invalid')
        
        self.assertTrue(
            "Invalid value for 'what': invalid. Must be 'call' or 'put'." in str(context.exception)
        )


if __name__ == '__main__':
    unittest.main()