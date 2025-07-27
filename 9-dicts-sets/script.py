user = {
    'name': 'john',
    'job': 'rocker',
    'fav_film': 'fight club'
}

print(user['name'])

# name, job = (user[k] for k in ('name', 'job'))
# name = user['name']
# job = user['job']
name = user.get('name', None)
job = user.get('job', None)
income = user.get('income', 0.0)

print(name, job, income)

for k in user.keys():
    user[k] = user[k].title()
    print(k)

for v in user.values():
    print(v)

for k, v in user.items():
    print(k, v, sep=' -> ', end=' | \n')

print(len(user.keys()))


user['car'] = 'volvo'.title()
print('car' in user)


print(user.pop('name'))

user['fav_book'] = 'Sun rise again'

tpl = user.popitem()

print(tpl)

print(user)
del user['fav_film']

print(user)

# user.clear()

print(user)

cpy = {**user}
# cpy = user.copy()
wrong_cpy = cpy


print(cpy is wrong_cpy)
print(cpy is user)
print(cpy)
