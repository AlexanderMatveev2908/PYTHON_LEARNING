import random
from typing import Any, Optional

from lib import parse_val
from t import ChoicesList, Comb, FancyChoice


def game(arg: Optional[Any] = None) -> None:
    cpu_wins = 0
    us_wins = 0
    play_again = True

    while play_again:
        input_val = input("Enter...\n1 => R\n2 => P\n3 => S\nQ => Quit\n-> ")
        if input_val.strip().lower() == "q":
            play_again = False
            print("By ✌🏼")
            break

        us_choice = parse_val(input_val)
        if not us_choice:
            print("Try again")
            continue

        print(f"You Chose: {FancyChoice[us_choice]}")

        cpu_choice = random.choice(ChoicesList)
        print(f"cpu chose {FancyChoice[cpu_choice]}")

        if us_choice == cpu_choice:
            print("tie 🤝")
        elif Comb[us_choice].value == cpu_choice:
            print("u win ✅")
            us_wins += 1
        else:
            print("u lose ❌")
            cpu_wins += 1

        feed = input(
            f"🧙‍♂️ us_wins => {us_wins}\n"
            f"cpu_wins => {cpu_wins}\n\n"
            "Play again?\n"
            "y => yes\n"
            "n => no\n"
            "-> "
        )
        if feed.strip().lower() != "y":
            play_again = False
            print("By ✌🏼")
            break


game()

print("Exit")
