import random as rdm
import math as mt
from enum import Enum
from typing import Literal


class WinMap(Enum):
    R = 'P'
    P = 'R'
    S = 'P'


Args = Literal['R', 'P', 'S']
args: tuple[Args, Args, Args] = ('R', 'P', 'S')


def min_max(min: int, max: int) -> int:
    return mt.floor(rdm.random() * (max - min + 1)) + min


while 1:
    user_chc: str | int = input('''
Enter...
1 -> Rock
2 -> Paper
3 -> Scissors
q -> Quit

''')

    if user_chc.lower() == 'q':
        print("👋 Bye!")
        break

    try:
        user_chc = int(user_chc)
        if user_chc not in [1, 2, 3]:
            raise ValueError("Invalid choice (must be 1–3)")
    except ValueError as err:
        print(f"❌ Error: {err}")
        continue

    user_val = args[user_chc - 1]
    cpu_val = args[min_max(0, 2)]

    print(f"\n🧠 CPU: {cpu_val}")
    print(f"🙋 You: {user_val}")

    if cpu_val == user_val:
        print("🤝 Tie!")
    elif WinMap[user_val].value == cpu_val:
        print("🎉 You win!")
    else:
        print("💀 You lose!")

    print("\n➖➖➖➖➖\n")
