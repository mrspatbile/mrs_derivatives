# mrs_derivatives

Create objects and conveniently get valuation, implicit volatility, risk measures, visualize payoffs and value variation for various inputs.

## Installation

You can install this package using pip:

```bash
pip install  mrs_derivatives
```

---

### **Usage Examples**


```python
from mrs_derivatives import Options

call1 = Options(data)
print(call1)
```

---

## Features

📞 Create Call or Put Instances with Embedded Functionalities: methods for pricing, Greeks, and visualizations.

📊 Compute Greeks (Delta, Gamma, Theta, Vega, Rho) and Visualize Partial Effects of interest rate, time to expiration, and underlying value.

💵 Get option valuation usign different techniques (Black-Scholes, binomial, Monte Carlo).

🔍 Compute Underlying Implied Volatility from Options Prices from option's market price.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
