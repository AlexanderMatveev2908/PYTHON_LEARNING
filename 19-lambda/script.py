from functools import reduce


mgk = lambda msg: f"🧙‍♂️ {msg}"  # noqa: E731

parsed = mgk("a slime appeared")
print(parsed)


arg = [x for x in range(10)]
print(arg)

arg_map = list(map(lambda x: x * 2, arg))
print(arg_map)

arg_filter = list(filter(lambda x: not x % 2, arg))
print(arg_filter)

arg_tot = reduce(lambda acc, curr: acc + curr, arg, 0)
print(arg_tot)
