from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass(frozen=True)
class OptionData:
    strike: float
    expiration: date
    what: Literal['call', 'put'] = 'call'
    multiplier: int = 100

    def __post_init__(self):
        if self.what not in ('call', 'put'):
            raise ValueError(f"Invalid value for 'what': {self.what}."
                             " Must be 'call' or 'put'.")