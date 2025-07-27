from typing import Literal, Tuple


Char = Literal['A', 'B', 'C', 'D']

ArgT = Tuple[Char, ...]

arg: ArgT = ('A', 'B')

print(len(arg))
print(arg[0])
print(arg[0] == 'A')
