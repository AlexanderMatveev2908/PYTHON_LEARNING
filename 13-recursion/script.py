from typing import cast, TypeVar
import json

T = TypeVar('T')


def add(arg: int) -> int:
    if arg < 5:
        return add(arg + 1)
    return arg


a = add(0)
print(a)


def cpy_obj(arg: T) -> T:
    if isinstance(arg, dict):
        return cast(T, {k: cpy_obj(v) for k, v in arg.items()})
    elif isinstance(arg, list):
        return cast(T, [cpy_obj(item) for item in arg])
    elif isinstance(arg, tuple):
        return cast(T, tuple(cpy_obj(item) for item in arg))
    elif isinstance(arg, set):
        return cast(T, {cpy_obj(item) for item in arg})
    else:
        return arg


sample = {
    'numbers': [1, 2, 3],
    'info': {'name': 'alex', 'tags': ('dev', 'zsh')},
    'flags': {True, False}
}

wrong = sample
good = cpy_obj(sample)


print(wrong is sample)
print(good is sample)
print(sample)


dummy = {
    "name": "Alex",
    "age": 28,
    "active": True,
    "score": 99.5,
    "languages": ["Python", "JavaScript", "Zsh"],
    "details": {
        "country": "Romania",
        "projects": 42,
        "meta": None
    }
}


also_good_cpy = json.loads(json.dumps(dummy, indent=2))
print(also_good_cpy is dummy)
print(json.dumps(dummy, indent=2, sort_keys=True))
