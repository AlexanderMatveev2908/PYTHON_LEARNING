from typing import Any, Dict


class Err(ValueError):
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


def dest(d: Dict[str, Any], k: str) -> Any | None:

    if k in d:
        return d[k]

    for v in d.values():
        if not isinstance(v, dict):
            continue

        found = dest(v, k)
        if found is not None:
            return found


v = dest(d, "pre_renovation")
print(v)
