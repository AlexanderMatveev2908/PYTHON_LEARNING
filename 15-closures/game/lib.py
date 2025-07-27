from t import Choice, ChoicesList, Err


def parse_val(v: str) -> Choice | None:
    try:
        # if v not in Comb.__members__:
        #     raise Err("Invalid key")
        if v not in [str(x + 1) for x in range(3)]:
            raise Err("Invalid key")
        # parsed = Comb[v].value
        parsed = ChoicesList[int(v) - 1]
        return parsed
    except (ValueError, Err) as err:
        print(err)
