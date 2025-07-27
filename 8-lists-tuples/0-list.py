from types import GeneratorType


users = ['dave', 'john', 'jane']

for i in range(len(users)):
    users[i] = users[i].title()

print(users)

# print(users.index('Dave'))
# thing_u_return for thing_u_iterate in iterable if cond
found_el = next((u for u in users if u.startswith('J')), None)

# idx_u_return for ids_u_iterate in iterable
found_idx = next((i for i, u in enumerate(users) if u.startswith('X')), -1)

print(found_el)
print(found_idx)

gn_lazy = (x for x in range(10))
gn = [x + 1 for x in range(10)]

print(type(gn_lazy))
print(isinstance(gn_lazy, GeneratorType))
print(list(gn_lazy))
print(list(gn_lazy))
print(gn)
