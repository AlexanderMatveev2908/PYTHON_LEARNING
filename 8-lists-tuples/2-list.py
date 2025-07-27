from functools import reduce


arg = [x for x in range(10)]

print(arg)
print(arg[1:-1])

my_str = '-'.join([str(x) for x in range(10)])

my_str = ', '.join(my_str.split('-'))

print(my_str)

# lazy evaluation
parsed = list(map(int, my_str.split(',')))
print(parsed)

cond_0 = all(isinstance(x, int) for x in parsed)
print(cond_0)

cond_1 = any(not x % 2 for x in parsed)
print(cond_1)

# parsed_2 = [str(x) + '...' for x in parsed]
parsed_2 = list(map(lambda x: str(x) + '...', parsed))
print(parsed_2)

# filtered = [x for x in parsed if not x % 2]
filtered = list(filter(lambda x: not x % 2, parsed))
print(filtered)

pairs = [
    ['name', 'john'],
    ['job', 'doctor']
]

d = reduce(lambda acc, curr: {**acc, curr[0]: curr[1]}, pairs, {})
print(d)

prices = [9.99, 14.99, 3.50]
tot = reduce(lambda acc, curr: acc + curr, prices, 0)
print(tot)
