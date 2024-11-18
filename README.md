[![CircleCI](https://circleci.com/gh/google/pybadges.svg?style=svg)](https://circleci.com/gh/google/pybadges)
![pypi](https://img.shields.io/pypi/v/pybadges.svg)
![mrs](https://img.shields.io/badge/https%3A%2F%2Fwww.mrspatbile.com-blue)
![Static Badge](https://img.shields.io/badge/python-3.13-blue)



# mrs_derivatives

Create objects and conveniently get valuation, implicit volatility, risk measures, visualize payoffs and value variation for various inputs.

## Installation

You can install this package using pip:

```bash
pip install  mrs_derivatives
```

---

### **Usage Examples**

There are two basic classes to hold data: `InstrumentData` (with immutable attributes corresponding to the instrument as strike, option price and expuration date) and `MarketData` (hold values that are bound to change as underlying spot price, interest rates and volatility).   


```python
from mrs_derivatives.options_data import InstrumentData, MarketData
from datetime import date

# arguments for the working example
strike = 50
expiration = date(2025, 1, 30)
what = 'put'
multiplier = 1000

# instantiate an object with immutable option characteristics
option = option = InstrumentData(strike, expiration, what, multiplier)
print(option)
# InstrumentData(strike=50, expiration=datetime.date(2025, 1, 30), what='put', multiplier=1000, underlying=None)
```

The default for option is a `what=call` and `multiplier=100`. Thus a call can be instatiated by passing only 2 arguments:

```python
call = InstrumentData(strike, expiration)
print(call)
# output: InstrumentData(strike=50, expiration=datetime.date(2025, 1, 30), what='call', multiplier=100, underlying=None)
```

The object for market data contains the additional market information (on tip of teh instrument's info) for computing price and risk.
```python
vol = .25
rate=.02
spot=52

mkt = MarketData(vol, rate, spot)
print(mkt)
#output: MarketData(vol=0.25, rate=0.02, spot=52, div=0)
```
---
The `OptionPricing` class takes two inputs: one object `InstrumentData` and another `MarketData`. Upon instantiation, it calculates and stores $dte$ (time to expiry), $d_1$, and $d_2$ as attributes for efficient reuse in pricing, Greeks, and sensitivities.

```python
pricing = OptionPricing(call, mkt)
print(pricing.d1, pricing.d12, pricing.dte)
# (0.44072697364909796, 0.328160402782289, 0.20273972602739726)
```



get_black_scholes

## Features

> 🛡️ Create **call** or **put** instances with embedded functionalities: methods for pricing, greeks, and visualizations.

> 🏛️ Compute **greeks** (delta, gamma, theta, vega, rho) and **visualize partial effects** of interest rate, time to expiration, and underlying value.

> 💵 Get option valuation using different techniques (Black-Scholes, binomial, Monte Carlo).

> 🎲 Compute **implied volatility** for the underlying given option's market price.

## Contributing

Do not be shy! Please contribute to this project by either openning an issue or submitting a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
