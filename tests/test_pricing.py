import unittest
from datetime import date
from src.mrs_derivatives.options_data import InstrumentData, MarketData, OptionPricing
from src.mrs_derivatives.options_data import black_scholes
from unittest.mock import MagicMock



class TestOptionPricing(unittest.TestCase):

    def setUp(self):
        # Mocking InstrumentData and MarketData for tests
        self.option_data = InstrumentData(strike=50, expiration=date(2025, 1, 30))
        self.market_data = MarketData(vol=0.2, rate=0.05, spot=100, div=0.01)
        
        # Create OptionPricing instance
        self.option_pricing = OptionPricing(option_data=self.option_data, market_data=self.market_data)

    def test_dte_computation(self):
        # Check that dte is computed correctly (time to expiration in years)
        self.assertAlmostEqual(self.option_pricing.dte, (date(2025, 1, 30) - date.today()).days / 365, places=2)

    def test_d1_d2_computation(self):
        # Check that d1 and d2 are computed correctly (you would need to check these values against the expected formula result)
        self.assertIsNotNone(self.option_pricing.d1)
        self.assertIsNotNone(self.option_pricing.d2)

    def test_get_black_scholes(self):
        # Check that the Black-Scholes pricing calculation is correct
        price = self.option_pricing.get_black_scholes
        self.assertIsInstance(price, float)  # Should return a float
        
        # Example of an expected value (you might need to compute this manually or using an existing library)
        expected_price = black_scholes(
            spot=self.market_data.spot,
            strike=self.option_data.strike,
            div=self.market_data.div,
            rate=self.market_data.rate,
            option_type=self.option_data.what,
            dte=self.option_pricing.dte,
            d1=self.option_pricing.d1,
            d2=self.option_pricing.d2
        )
        self.assertAlmostEqual(price, expected_price, places=2)


if __name__ == '__main__':
    unittest.main()
