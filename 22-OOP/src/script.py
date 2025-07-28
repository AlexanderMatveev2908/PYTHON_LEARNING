from datetime import datetime
import locale
from typing import Optional
import attr


def gen_fancy_money(v: float) -> str:
    locale.setlocale(locale.LC_ALL, "en_US")
    return locale.currency(v, grouping=True)


@attr.s(auto_attribs=True)
class Bank_account:
    name: str
    age: int
    job: str
    _amount: float = attr.ib(repr=False, default=0.0)
    email: Optional[str] = None

    def get_blc(self) -> float:
        print(self._amount)
        return self._amount

    def put(self, v: float) -> float:
        self._amount += v
        print(self._amount)
        return self._amount

    def get(self, v: float) -> float:
        self._amount -= v
        print(self._amount)
        return self._amount


amber = Bank_account(
    name="Amber",
    age=24,
    job="nurse",
)

amber.get_blc()


print(gen_fancy_money(34.9666))

# print(f"${343838465.9666:_.2f}")


now = datetime.now()

formatted = now.strftime("%a, %d %b, %Y %H:%M")
print(formatted)
