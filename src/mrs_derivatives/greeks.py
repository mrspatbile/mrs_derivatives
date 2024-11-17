# greeks.py

import math
from scipy.stats import norm
from datetime import date
from pricing import dte, d1, d2


def delta(spot, strike, rate, vol, dte, option_type, div=0):
    d1_val = d1(spot, strike, rate, vol, dte, div)
    if option_type == 'call':
        return math.exp(-div * dte) * norm.cdf(d1_val)
    else:
        return -math.exp(-div * dte) * norm.cdf(-d1_val)

def gamma(spot, strike, rate, vol, dte, div=0):
    d1_val = d1(spot, strike, rate, vol, dte, div)
    return norm.pdf(d1_val) * math.exp(-div * dte) / (spot * vol * math.sqrt(dte))

def theta(spot, strike, rate, vol, dte, option_type, div=0):
    d1_val = d1(spot, strike, rate, vol, dte, div)
    d2_val = d2(spot, strike, rate, vol, dte, div)
    first_term = -(spot * vol * norm.pdf(d1_val) * math.exp(-div * dte)) / (2 * math.sqrt(dte))
    if option_type == 'call':
        second_term = rate * strike * math.exp(-rate * dte) * norm.cdf(d2_val)
        third_term = -div * spot * math.exp(-div * dte) * norm.cdf(d1_val)
    else:
        second_term = -rate * strike * math.exp(-rate * dte) * norm.cdf(-d2_val)
        third_term = div * spot * math.exp(-div * dte) * norm.cdf(-d1_val)
    return (first_term + second_term + third_term) / 365

def vega(spot, strike, rate, vol, dte, div=0):
    d1_val = d1(spot, strike, rate, vol, dte, div)
    return spot * norm.pdf(d1_val) * math.exp(-div * dte) * math.sqrt(dte) / 100

def rho(spot, strike, rate, vol, dte, option_type, div=0):
    d2_val = d2(spot, strike, rate, vol, dte, div)
    if option_type == 'call':
        return strike * dte * math.exp(-rate * dte) * norm.cdf(d2_val) / 100
    else:
        return -strike * dte * math.exp(-rate * dte) * norm.cdf(-d2_val) / 100

### Greeks Summary

def greeks(spot, strike, rate, vol, dte, option_type, div=0):
    greeks_dict = {
        'delta': delta(spot, strike, rate, vol, dte, option_type, div),
        'gamma': gamma(spot, strike, rate, vol, dte, div),
        'theta': theta(spot, strike, rate, vol, dte, option_type, div),
        'vega': vega(spot, strike, rate, vol, dte, div),
        'rho': rho(spot, strike, rate, vol, dte, option_type, div),
    }
    
    class GreeksDict:
        def __init__(self, greeks_dict):
            self.greeks_dict = greeks_dict

        def __getitem__(self, key):
            return self.greeks_dict[key]

        def items(self):
            return self.greeks_dict.items()

        def __str__(self):
            return "\n".join(f"{key:>8}: {value:>7.4f}" for key, value in self.greeks_dict.items())
    
    return GreeksDict(greeks_dict)