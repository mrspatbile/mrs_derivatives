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
        


@dataclass
class MarketData:
    vol: Number
    rate: float
    spot: Number
    div: Number = 0
    