import math as mt


T = int | float | str

v: T = -5.754

print(abs(v))

print(round(v))

print(round(v, 1))

print(mt.floor(v))
print(mt.ceil(v))

print(mt.pi)

print(mt.sqrt(9))

v = '1954'
print(isinstance(v, str))
v = int(v)
print(isinstance(v, int))
