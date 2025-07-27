from t import Choice, Comb, Err


def parse_val(v: Choice) -> Choice | None:
    try:
        if v not in Comb.__members__:
            raise Err("Invalid key")
        parsed = Comb[v].value
        return parsed
    except (ValueError, Err) as err:
        print(err)
