from reg import REG_INT, REG_FLOAT


class Err(Exception):
    def __init__(self, msg: str):
        super().__init__(f"🔥 {msg}")


T = int | float | None


def get_v(v: str) -> T:
    try:
        if REG_INT.fullmatch(v):
            return int(v)
        elif REG_FLOAT.fullmatch(v):
            return float(v)
        raise Err('Invalid val')
    except (ValueError, Err) as err:
        print(err)
        return None


v = get_v(input('Write an int\n '))

if isinstance(v, int):
    print(f"{v} is an int")
elif isinstance(v, float):
    print(f"{v} is a float")
else:
    print("Not a valid number.")


print('not crashed 😎')
