# pricing.py

import math
from scipy.stats import norm  # type: ignore
from datetime import date
from numbers import Number
from typing import Optional, Literal, Tuple
from options_data import OptionData
from options_market import OptionMarket


def get_dte(
    dte: int = None, 
    expiration: date = None, 
    ref_date: date = date.today()
    ) -> float:
    """
    Calculate or validate days to expiration as a fraction of a year.

    Parameters:
        dte (float): Time to expiration in years (optional).
        expiration (date): Expiration date (optional, used if dte is not provided).
        ref_date (date): Reference date for dte calculation (default is today).

    Returns:
        float: Time to expiration in years.
    """

    if dte and expiration: # type: ignore
       print("Both dte and expiration where given."
        "Using dte value."
        "If expiration is to be used, pls remove dte param from call.")
    if dte is not None:
        return float(dte)
    elif expiration is None:
        raise ValueError("Either dte or expiration must be provided.")
    return (expiration - ref_date).days / 365


def get_dte_d1_d2(
    expiration: date, 
    spot: Number, 
    strike: Number, 
    rate: float, 
    vol: float, 
    div: Number = 0, 
    dte: Optional[float] = None,
    ref_date: date = date.today()
    ) -> Tuple[float, float, float]:
    """
    Calculate the time to expiration (dte), d1, and d2 values for the Black-Scholes model.

    Parameters:
        expiration (date): Expiration date of the option.
        spot (Number): Current price of the underlying asset.
        strike (Number): Strike price of the option.
        rate (float): Risk-free interest rate (annualized).
        vol (float): Volatility of the underlying asset (annualized).
        div (Number, optional): Dividend yield of the underlying asset (default is 0).
        dte (Optional[float], optional): Time to expiration in years (default is None, will be calculated if not provided).
        ref_date (date, optional): Reference date for dte calculation (default is today).

    Returns:
        tuple: A tuple containing the following values:
        - dte (float): Time to expiration in years.
        - d1 (float): d1 value for the Black-Scholes model.
        - d2 (float): d2 value for the Black-Scholes model.
    """

    # Compute dte
    dte = get_dte(dte, expiration, ref_date)

    # Compute d1 and d2 using the pre-calculated dte
    d1 = (math.log(spot / strike) + 
        (rate - div + 0.5 * vol ** 2) * dte) / (vol * math.sqrt(dte))
    
    d2 = d1 - vol * math.sqrt(dte)

    return dte, d1, d2

class OptionPricing:
    def __init__(self, 
                 option_data: OptionData, 
                 market_data: OptionMarket, 
                 ):

        self.opt = option_data
        self.mkt = market_data

    
    def __post_init__(self):
        self.dte, self.d1, self.d2 = get_dte_d1_d2(
            expiration=self.opt.expiration,
            spot=self.mkt.spot,
            strike=self.opt.strike,
            rate=self.mkt.rate,
            vol=self.mkt.vol,
            div=self.opt.div, 
        )
   
    @property
    def get_black_scholes(self):
        return  black_scholes(
                spot=self.mkt.spot,
                strike=self.opt.strike,
                div=self.mkt.div,
                rate=self.mkt.rate,
                option_type=self.mkt.what,
                dte=self.dte,
                d1=self.d1,
                d2=self.d2,
        )


def black_scholes(  
    spot: Number, 
    strike: Number, 
    rate: Number,
    dte: Number,  
    d1: float,
    d2: float,
    div: Number = 0, 
    option_type: Literal['call', 'put'] = 'call', 
    ) -> float:
    """
    Calculate the Black-Scholes price for a European option.
    
    Parameters:
        spot (float): Current stock price.
        strike (float): Strike price of the option.
        rate (float): Risk-free interest rate.
        vol (float): Volatility (standard deviation of returns).
        div (float): Dividend yield (default is 0).
        option_type (Literal['call', 'put']): 'call' or 'put' (default is 'call').
        dte (float): Time to expiration in years (default is 1.0).
    
    Returns:
        float: Option price.
    """
    # Calculate the option price based on d1 and d2
    if option_type == 'call':
        price = (spot * math.exp(-div * dte) * norm.cdf(d1) -
                 strike * math.exp(-rate * dte) * norm.cdf(d2))
    elif option_type == 'put':
        price = (-spot * math.exp(-div * dte) * norm.cdf(-d1) +
                 strike * math.exp(-rate * dte) * norm.cdf(-d2))
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return price