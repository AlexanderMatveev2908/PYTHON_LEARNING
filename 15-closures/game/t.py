from enum import Enum
from typing import Dict, Literal

Choice = Literal["R", "P", "S"]
ChoicesList: tuple[Choice, ...] = ("R", "P", "S")
Emoji = Literal["✊🏼", "✋🏼", "✌🏼"]


class Comb(Enum):
    R = "P"
    P = "R"
    S = "P"


FancyChoice: Dict[Choice, Emoji] = {"R": "✊🏼", "P": "✋🏼", "S": "✌🏼"}


class Err(ValueError):
    def __init__(self, msg: str) -> None:
        super().__init__(f"😡 {msg}")
