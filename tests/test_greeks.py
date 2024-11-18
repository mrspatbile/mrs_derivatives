import unittest
from math import isclose
from src.mrs_derivatives.greeks import delta, gamma, theta, vega, rho, get_greeks

class TestGreeksFunctions(unittest.TestCase):
    def setUp(self):
        self.spot = 100
        self.strike = 100
        self.rate = 0.05
        self.vol = 0.2
        self.dte = 30 / 365  # Time to expiration in years
        self.option_type = 'call'
        self.d1 = 0.5  # Example values for d1 and d2
        self.d2 = 0.3
        self.div = 0.02  # Dividend yield

    def test_delta_call(self):
        result = delta(self.spot, self.strike, self.rate, self.vol, self.option_type, self.dte, self.d1, self.div)
        expected = 0.6903267443744298  
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_delta_put(self):
        result = delta(self.spot, self.strike, self.rate, self.vol, 'put', self.dte, self.d1, self.div)
        expected = -0.3080307703668755  
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_gamma(self):
        result = gamma(self.spot, self.strike, self.rate, self.vol, self.dte, self.d1, self.div)
        expected = 0.06130066079457635
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_theta_call(self):
        result = theta(self.spot, self.strike, self.rate, self.vol, self.option_type, self.dte, self.d1, self.d2, self.div)
        expected = -0.028942189844193878
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_theta_put(self):
        result = theta(self.spot, self.strike, self.rate, self.vol, 'put', self.dte, self.d1, self.d2, self.div)
        expected = -0.03711418762320322
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_vega(self):
        result = vega(self.spot, self.strike, self.rate, self.vol, self.dte, self.d1, self.div)
        expected = 0.100768209525331
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_rho_call(self):
        result = rho(self.spot, self.strike, self.rate, self.vol, self.option_type, self.dte, self.d2, self.div)
        expected = 0.050578953773151206
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_rho_put(self):
        result = rho(self.spot, self.strike, self.rate, self.vol, 'put', self.dte, self.d2, self.div)
        expected = -0.03127574571431764
        self.assertTrue(isclose(result, expected, rel_tol=1e-5))

    def test_get_greeks(self):
        greeks = get_greeks(self.spot, self.strike, self.rate, self.vol, self.option_type, self.dte, self.d1, self.d2, self.div)
        self.assertTrue(isclose(greeks['delta'], 0.6903267443744298, rel_tol=1e-5))  # Update with actual expected values
        self.assertTrue(isclose(greeks['gamma'], 0.06130066079457635, rel_tol=1e-5))
        self.assertTrue(isclose(greeks['theta'], -0.028942189844193878, rel_tol=1e-5))
        self.assertTrue(isclose(greeks['vega'], 0.100768209525331, rel_tol=1e-5))
        self.assertTrue(isclose(greeks['rho'], 0.050578953773151206, rel_tol=1e-5))

if __name__ == '__main__':
    unittest.main()