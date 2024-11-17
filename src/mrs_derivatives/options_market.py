from dataclasses import dataclass

@dataclass
class OptionMarket:
    vol: float
    rate: float
    spot: float
    div: float