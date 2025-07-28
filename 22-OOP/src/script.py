from datetime import datetime
import locale
from typing import Any, Literal, Optional
import attr
from threading import Timer


def gen_fancy_money(v: float) -> str:
    locale.setlocale(locale.LC_ALL, "en_US")
    return locale.currency(v, grouping=True)


def show_famcy_money(v: float) -> float:
    v_parsed = gen_fancy_money(v)
    print(v_parsed)
    return v


def show_fancy_time(v: datetime) -> str:
    parsed = v.strftime("%a, %d %b, %Y %H:%M %S")
    return parsed


OpT = Literal["+", "-", ""]


def balance_handler(inst: Any, *, v: float = 0.0, op: OpT = "") -> float:
    inst.updated_at = datetime.now()
    print(show_fancy_time(inst.updated_at))

    if not op:
        return show_famcy_money(inst._amount)
    else:

        inst._amount += v if op == "+" else -v
        return show_famcy_money(inst._amount)


@attr.s(auto_attribs=True)
class Bank_account:
    name: str
    age: int
    job: str
    _amount: float = attr.ib(repr=False, default=0.0)
    email: Optional[str] = None
    created_at: datetime = attr.ib(factory=datetime.now)
    updated_at: datetime = attr.ib(factory=datetime.now)

    def __attrs_post_init__(self):
        print(
            f"🏦 New bank account opened for {self.name}"
            " "
            f"at {show_fancy_time(self.created_at)}"
        )

    def get_blc(self) -> float:
        return balance_handler(
            self,
        )

    def put(self, v: float) -> float:
        return balance_handler(self, v=v, op="+")

    def get(self, v: float) -> float:
        return balance_handler(self, v=v, op="-")

    def get_created_at(self) -> str:
        return show_fancy_time(self.created_at)


amber = Bank_account(
    name="Amber",
    age=24,
    job="nurse",
)


timeout = Timer(3.0, amber.get_blc)
timeout.start()
# amber.get_blc()
# amber.get_created_at()
# amber.put(55)
# amber.get(23)

# print(gen_fancy_money(34.9666))

# print(f"${343838465.9666:_.2f}")


# now = datetime.now()

# formatted = now.strftime("%a, %d %b, %Y %H:%M")
# print(formatted)
