from typing import Any, Optional


name = "Jordan"


def fn(arg: Any = None) -> None:
    global name
    name = "Michael"


fn()
print(name)


def fn_2(arg: str | None = None) -> None:
    name = "Mark"

    def fn_inner(arg: Optional[Any] = None) -> None:
        nonlocal name
        name = "Mary"

    fn_inner()
    print(name)


fn_2()
