from dataclasses import dataclass
from datetime import datetime as dt
from typing import Literal

@dataclass(frozen=True)
class OptionData:
    strike: float
    expiration: dt
    what: Literal['call', 'put'] = 'call'
    multiplier: int = 100