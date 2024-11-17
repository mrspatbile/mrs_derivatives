# pricing.py

import math
from scipy.stats import norm
from datetime import date


nt("Both expiration and dte where provided." 
            "Assuming dte as parameter."
            "If you want otherwise, remove dte from parameters.")
    if dte isdef get_dte(dte=None, expiration=None, ref_date=date.today()):
    """
    Calculate or validate days to expiration as a fraction of a year.

    Parameters:
        dte (float): Time to expiration in years (optional).
        expiration (date): Expiration date (optional, used if dte is not provided).
        ref_date (date): Reference date for dte calculation (default is today).

    Returns:
        float: Time to expiration in years.
    """
    if dte and expiration:
      pri not None:
        return dte
    if expiration is None:
        raise ValueError("Either dte or expiration must be provided.")
    return (expiration - ref_date).days / 365

def get_dte_d1_d2(expiration, spot, strike, rate, vol, div=0, dte=None, ref_date=date.today()):
    """
    Compute dte, d1, and d2 values for the Black-Scholes model in a single function.
    
    Parameters:
        expiration (date): Expiration date of the option.
        spot (float): Current stock price.
        strike (float): Strike price of the option.
        rate (float): Risk-free interest rate.
        vol (float): Volatility (standard deviation of returns).
        div (float): Dividend yield (default is 0).
        ref_date (date): Reference date for dte calculation (default is today).
    
    Returns:
        tuple: (dte, d1, d2)
    """
    # Compute dte
    dte = get_dte_from_inputs(dte, expiration, ref_date)

    # Compute d1 and d2 using the pre-calculated dte
    d1_val = (math.log(spot / strike) + 
              (rate - div + 0.5 * vol ** 2) * dte) / (vol * math.sqrt(dte))
    
    d2_val = d1_val - vol * math.sqrt(dte)

    return dte, d1_val, d2_val


def black_scholes(spot, strike, rate, vol, dte=None, expiration=None, div=0, option_type='call', ref_date=date.today()):
    """
    Calculate the Black-Scholes price for a European option.
    
    Parameters:
        spot (float): Current stock price.
        strike (float): Strike price of the option.
        rate (float): Risk-free interest rate.
        vol (float): Volatility (standard deviation of returns).
        dte (float): Time to expiration in years (optional).
        expiration (date): Expiration date of the option (optional, used if dte is not provided).
        div (float): Dividend yield (default is 0).
        option_type (str): 'call' or 'put' (default is 'call').
        ref_date (date): Reference date for dte calculation (default is today).
    
    Returns:
        float: Option price.
    """
    # Compute dte, d1, and d2
    dte, d1_val, d2_val = compute_dte_d1_d2(spot=spot, strike=strike, rate=rate, vol=vol, div=div)

    # Calculate option price
    if option_type == 'call':
        price = (spot * math.exp(-div * dte) * norm.cdf(d1_val) -
                 strike * math.exp(-rate * dte) * norm.cdf(d2_val))
    elif option_type == 'put':
        price = (-spot * math.exp(-div * dte) * norm.cdf(-d1_val) +
                 strike * math.exp(-rate * dte) * norm.cdf(-d2_val))
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price


def implied_vol(quote, spot, strike, rate, div, dte, option_type='call', tolerance=1e-5, max_iterations=100):
    """
    Calculate the implied volatility using the Black-Scholes model.
    
    Parameters:
        quote (float): Observed market price of the option.
        spot (float): Current stock price.
        strike (float): Strike price of the option.
        rate (float): Risk-free interest rate.
        div (float): Dividend yield.
        dte (float): Time to expiration in years.
        option_type (str): 'call' or 'put' (default is 'call').
        tolerance (float): Tolerance for convergence (default is 1e-5).
        max_iterations (int): Maximum number of iterations (default is 100).
    
    Returns:
        float or str: Implied volatility or a message indicating failure.
    """
    low = 0.0
    high = 5.0

    for _ in range(max_iterations):
        vol = (low + high) / 2
        price = black_scholes(spot, strike, rate, vol, dte, div, option_type)

        if abs(price - quote) < tolerance:
            return vol
        elif price < quote:
            low = vol
        else:
            high = vol
    
    return "Implied volatility not found within the specified tolerance."