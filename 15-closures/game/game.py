from typing import Any, Optional, cast

from lib import parse_val
from t import Choice


def game(arg: Optional[Any] = None) -> None:
    cpu_wins = 0
    us_wins = 0
    play_again = True

    while play_again:
        input_val = input("Enter...\n1 => R\n2 => P\n3 => S\nQ => Quit\n-> ")
        if input_val == "Q":
            play_again = False
            print("By ✌🏼")
            break

        us_choice = parse_val(cast(Choice, input_val))
        if not us_choice:
            print("Try again")
            continue


game()

print("Exit")
