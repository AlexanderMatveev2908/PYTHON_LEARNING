from typing import Literal, Tuple
from enum import Enum


class Role(Enum):
    CONSUMER = 0
    EMPLOYEE = 1
    MANAGER = 2
    OWNER = 3


StageT = Literal['pending', 'in_progress', 'completed', 'cancelled']
StagesListT = Tuple[StageT, ...]

stages_loading: StagesListT = ('pending', 'in_progress')


if not stages_loading:
    raise ValueError('miss stages_loading')

# print('values present')

print('pending' in stages_loading)
