# greeks.py
import math
from scipy.stats import norm # type: ignore
from typing import Optional, Dict
from numbers import Number

def delta(
    spot: float, 
    strike: float, 
    rate: float, 
    vol: float, 
    option_type: str, 
    dte: float, 
    d1: float, 
    div: float = 0
) -> float:
    if option_type == 'call':
        return math.exp(-div * dte) * norm.cdf(d1)
    return -math.exp(-div * dte) * norm.cdf(-d1)

def gamma(
    spot: float, 
    strike: float, 
    rate: float, 
    vol: float, 
    dte: float, 
    d1: float, 
    div: Number = 0
) -> float:
    if vol == 0:
        return float('inf')
    return norm.pdf(d1) * math.exp(-div * dte) / (spot * vol * math.sqrt(dte))

def theta(
    spot: float, 
    strike: float, 
    rate: float, 
    vol: float, 
    option_type: str, 
    dte: float, 
    d1: float, 
    d2: float, 
    div: Number = 0
) -> float:
    first_term = -(spot * vol * norm.pdf(d1) * math.exp(-div * dte)) / (2 * math.sqrt(dte))
    if option_type == 'call':
        second_term = rate * strike * math.exp(-rate * dte) * norm.cdf(d2)
        third_term = -div * spot * math.exp(-div * dte) * norm.cdf(d1)
    else:
        second_term = -rate * strike * math.exp(-rate * dte) * norm.cdf(-d2)
        third_term = div * spot * math.exp(-div * dte) * norm.cdf(-d1)
    return (first_term + second_term + third_term) / 365

def vega(
    spot: float, 
    strike: float, 
    rate: float, 
    vol: float, 
    dte: float, 
    d1: float, 
    div: Number = 0
) -> float:
    return spot * norm.pdf(d1) * math.exp(-div * dte) * math.sqrt(dte) / 100

def rho(
    spot: float, 
    strike: float, 
    rate: float, 
    vol: float,
    option_type: str, 
    dte: float, 
    d2: float, 
    div: Number = 0
) -> float:
    if option_type == 'call':
        return strike * dte * math.exp(-rate * dte) * norm.cdf(d2) / 100
    return -strike * dte * math.exp(-rate * dte) * norm.cdf(-d2) / 100

def get_greeks(
    spot: float, 
    strike: float, 
    rate: float, 
    vol: float, 
    dte: float, 
    d1: float, 
    d2: float, 
    option_type: str, 
    div: Number = 0,
) -> Dict[str, float]:
    
    greeks_dict = {
    'delta': delta(spot, strike, rate, vol,  option_type, dte, d1,  div),
    'gamma': gamma(spot, strike, rate, vol,  dte, d1, div),
    'theta': theta(spot, strike, rate, vol,  option_type, dte, d1, d2, div),
    'vega': vega(spot, strike, rate, vol, dte, d1, div),
    'rho': rho(spot, strike, rate, vol,  option_type, dte, d2, div),
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