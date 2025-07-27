from enum import Enum
from typing import Literal

Choice = Literal["R", "P", "S"]


class Comb(Enum):
    R = "P"
    P = "R"
    S = "P"


class Err(ValueError):
    def __init__(self, msg: str) -> None:
        super().__init__(f"😡 {msg}")
