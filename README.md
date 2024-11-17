# mrs_derivatives

Create objects and conveniently get valuation, implicit volatility, risk measures, visualize payoffs and value variation for various inputs.

## Installation

You can install this package using pip:

```bash
pip install  mrs_derivatives
```

---

### **Usage Examples**

There are two basic classes taht holds data: `OptionData` (with attibutes corresponding to the instrument) and `MarketData` (hold values that are bound to change as underlying spot price, interest rates and volatility).   


```python
from mrs_derivatives.options_data import OptionData
from datetime import date

# arguments for the working example
strike = 50
expiration = date(2025, 1, 30)
what = 'put'
multiplier = 1000

# instantiate an object with immutable option characteristics
option = OptionData(strike, expiration, what, multiplier)

print(option)
# output: OptionData(strike=50, expiration=datetime.date(2025, 1, 30), what='put', multiplier=1000, inderlying=None)
```

The default for option is a `what=call` and `multiplier=100`. Thus a call can be instatiated by passing only 2 arguments:

```python
call_1 = OptionData(strike, expiration)
print(call_1)
# output: OptionData(strike=50, expiration=datetime.date(2025, 1, 30), what='call', multiplier=100, underlying=None)
```

```python
from mrs_derivatives.options_market import OptionMarket
from datetime import date
vol = .25
rate = .02
spot = 100

OptionMarket(vol, rate, spot)
#output: OptionMarket(vol=0.25, rate=0.02, spot=100, div=0)
```
---

## Features

> 🛡️ Create **call** or **put** instances with embedded functionalities: methods for pricing, greeks, and visualizations.

> 🏛️ Compute **greeks** (delta, gamma, theta, vega, rho) and **visualize partial effects** of interest rate, time to expiration, and underlying value.

> 💵 Get option valuation using different techniques (Black-Scholes, binomial, Monte Carlo).

> 🎲 Compute **implied volatility** for the underlying given option's market price.

## Contributing

Do not be shy! Please contribute to this project by either openning an issue or submitting a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
