#python -m unittest test_options_data.py


import unittest
from datetime import date
from src.mrs_derivatives.options_data import InstrumentData, MarketData
class TestInstrumentData(unittest.TestCase):

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

class TestMarketData(unittest.TestCase):

    def test_default_values(self):
        # Create an instance of MarketData with div using the default value (0)
        market_data = MarketData(spot=100, rate=0.05, vol=0.2)
        
        # Test the values
        self.assertEqual(market_data.spot, 100)
        self.assertEqual(market_data.rate, 0.05)
        self.assertEqual(market_data.vol, 0.2)
        self.assertEqual(market_data.div, 0)  # Default div should be 0


    def test_invalid_param(self):
        invalid_param = {
            "spot": -100,  # Negative value for the 'spot' parameter
            "rate": 0.05,
            "vol": 0.2
        }

        with self.assertRaises(ValueError) as context:
            # Create MarketData with the invalid 'spot' value
            MarketData(**invalid_param)

        # Check if the error message contains the expected part
        self.assertTrue("Spot cannot be negative." in str(context.exception))


    def test_custom_values(self):
        # Create an instance with custom values, including a custom div value
        market_data = MarketData(spot=120, rate=0.03, vol=0.25, div=0.02)
        
        # Test that the values were set correctly
        self.assertEqual(market_data.spot, 120)
        self.assertEqual(market_data.rate, 0.03)
        self.assertEqual(market_data.vol, 0.25)
        self.assertEqual(market_data.div, 0.02) 


if __name__ == '__main__':
    unittest.main()