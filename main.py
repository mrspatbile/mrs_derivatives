from datetime import date, timedelta

from src.mrs_derivatives.pricing import black_scholes, get_dte_d1_d2, OptionPricing
from src.mrs_derivatives.greeks import get_greeks
from src.mrs_derivatives.options_data import MarketData, InstrumentData

# for tests
# python -m unittest discover -s tests


# # Example input parameters
# spot = 100          # Current stock price
# strike = 105        # Strike price
# rate = 0.05         # Risk-free interest rate
# vol = 0.2           # Volatility (20%)
# option_type = 'call'  # Call or Put
# div = 0.02          # Dividend yield

# dte, d1, d2 = get_dte_d1_d2(
#     expiration=date.today() + timedelta(days=30),
#     spot=spot,
#     strike=strike,
#     rate=rate,
#     vol=vol,
#     div=div,
# )

# # Calculate the option price using Black-Scholes
# price = black_scholes(spot, strike, rate, dte, d1, d2, div, option_type)
# print(f"The Black-Scholes {option_type} option price is: {price:.4f}")

# # Calculate the Greeks
# greeks = get_greeks(spot, strike, rate, vol, option_type, dte, d1, d2, div)
# print("\nOption Greeks:")
# for greek, value in greeks.items():
#     print(f"{greek.capitalize()}: {value:.4f}")


# working example: instrument
strike = 50
expiration = date(2025, 1, 30)
inst =  InstrumentData(strike, expiration)
print('Instrument object holds immutable data')
print(inst)
print()

# working example: market
vol = .25
rate = .02
spot = 52
mkt = MarketData(spot, rate, vol)

print('Market object holds data bound to change')
print(mkt)
print()

# compute Black and Scholes
pricing = OptionPricing(inst, mkt)
bs = pricing.get_black_scholes
print(f"Pricing (BSL model): {bs}")
print()

# get greeks
greeks = pricing.greek_dict()
print("greeks computed easily, from the object")
print(greeks)
print()

# get greek using key value
print(f"Delta: {greeks['delta']}.")
print()