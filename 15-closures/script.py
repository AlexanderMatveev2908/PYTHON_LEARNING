from typing import Any, Callable, Optional

# __ like HOF in JS


def fn_outer(msg: Optional[Any] = None) -> Callable[..., None]:
    def fn_inner(arg: Optional[Any] = None) -> None:
        print(msg)

    return fn_inner


greet = fn_outer("message...")
greet()


def fn_outer_1(name: str) -> Callable[..., None]:
    coins = 5

    def fn_inner_1(arg: Optional[Any] = None) -> None:
        nonlocal coins

        if not coins:
            return

        coins -= 1

        print(f"{name} has {coins} coins {'✅' if coins else '❌'}")

    return fn_inner_1


jane = fn_outer_1("jane")
amber = fn_outer_1("amber")

jane()
amber()
amber()
amber()
amber()
jane()
amber()
amber()
amber()
amber()
amber()
