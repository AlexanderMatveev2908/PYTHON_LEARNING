import traceback
from typing import Any, Callable, Dict, Optional


class Err(Exception):
    def __init__(self, msg: str, *, code: int = 500) -> None:
        super().__init__(f"😡 {msg}")

        self.code = code


d = {
    "name": "john",
    "address": {
        "street": {
            "code": 34,
            "road": {
                "pre_renovation": "old old name",
                "modern": "new fancy name ",
            },
        }
    },
}


def dtr(d: Dict[str, Any], k: str) -> Any | None:

    if k in d:
        return d[k]

    for v in d.values():
        if not isinstance(v, dict):
            continue

        found = dtr(v, k)
        if found is not None:
            return found


v = dtr(d, "pre_renovation")
print(v)


def tc(cb: Callable[..., Optional[Any]]):
    try:
        try:
            cb()
        except Exception as err:
            raise Err(str(err)) from err
    except Err as err:
        print(traceback.print_exc())
        print(err)


# def b() -> None:
#     4 + "h"


# tc(b)
