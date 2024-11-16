# mrs_derivatives

Create objects and conveniently get valuation, implicit volatility, risk measures, visualize payoffs and value variation for various inputs.

## Installation

You can install this package using pip:

```bash
pip install  mrs_derivatives
```

---

### **Usage Examples**

The basic class is `Option`, which is instantiated with 4 attributes:  `what`, `multiplier`, `expiration`, `strike`.

```python
from mrs_derivatives import Options
from datetime import date

# arguments for the working example
strike = 50
expiration = date(2025, 1, 30)
what = 'put'
multiplier = 1000

# instantiate the option
option = Options(strike, expiration, what, multiplier)

print(option)
# output: OptionData(strike=50, expiration=date(2025, 1, 30), what='put', multiplier=1000)
```

The default for option is a `what=call` and `multiplier=100`. Thus a call can be instatiated by passing only 2 arguments:

```python
call_1 = Options(strike, expiration)
print(call_1)
```
---

## Features

> 🛡️ Create Call or Put Instances with Embedded Functionalities: methods for pricing, Greeks, and visualizations.

> 🏛️ Compute Greeks (Delta, Gamma, Theta, Vega, Rho) and Visualize Partial Effects of interest rate, time to expiration, and underlying value.

> 💵 Get option valuation usign different techniques (Black-Scholes, binomial, Monte Carlo).

> 🎲 Compute Underlying Implied Volatility from Options Prices from option's market price.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
