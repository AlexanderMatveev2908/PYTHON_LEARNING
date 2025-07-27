a = [x for x in range(10)]

print(a)
print(a[-3:-1])

a.append(10)
a.insert(0, -1)

print(a)

a += [11]
a.extend([12, 13])
print(a)
a.remove(-1)
print(a)

b = a.pop()
c = a.pop(0)
print(b)
print(c)
print(a)


cpy = [*a]
cpy = a[:]        # slicing
cpy = list(a)     # constructor
cpy = a.copy()    # method
