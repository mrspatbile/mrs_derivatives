from src.mrs_derivatives.pricing import black_scholes
from src.mrs_derivatives.greeks import get_greeks

# Example input parameters
spot = 100          # Current stock price
strike = 105        # Strike price
rate = 0.05         # Risk-free interest rate
vol = 0.2           # Volatility (20%)
dte = 30 / 365      # Time to expiration in years
option_type = 'call'  # Call or Put
div = 0.02          # Dividend yield

# Calculate the option price using Black-Scholes
price = black_scholes(spot, strike, rate, vol, dte, option_type, div)
print(f"The Black-Scholes {option_type} option price is: {price:.4f}")

# Calculate the Greeks
greeks = get_greeks(spot, strike, rate, vol, option_type, dte, d1, d2, div)
print("\nOption Greeks:")
for greek, value in greeks.items():
    print(f"{greek.capitalize()}: {value:.4f}")
