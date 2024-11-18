from dataclasses import dataclass
from datetime import date
from typing import Literal
from numbers import Number

@dataclass(frozen=True)
class InstrumentData:
    strike: Number
    expiration: date
    what: Literal['call', 'put'] = 'call'
    multiplier: int = 100
    underlying: str = None

    def __post_init__(self):
        if self.what not in ('call', 'put'):
            raise ValueError(f"Invalid value for 'what': {self.what}."
                             " Must be 'call' or 'put'.")
        

class MarketData:
    def __init__(self, 
            spot: Number, 
            rate: float, 
            vol: float, 
            div: float = 0
            ):
        # List of parameters to validate
        params = [("spot", spot), 
                  ("rate", rate), 
                  ("vol", vol), 
                  ("div", div)]
        
        # Check that all values are non-negative
        for param_name, value in params:
            if value < 0:
                raise ValueError(f"{param_name.capitalize()} cannot be negative.")

        # Assign values if no error was raised
        self.spot = spot
        self.rate = rate
        self.vol = vol
        self.div = div

    def __str__(self):
        return (f"MarketData("
            f"spot={self.spot:.2f}, "
            f"rate={self.rate:.4f}, "
            f"vol={self.vol:.4f}, "
            f"div={self.div:.4f}"
            f")")