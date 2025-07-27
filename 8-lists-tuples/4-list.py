a = [5, 3, 2, 4, 1, 0]

print(a)

# key returns vals evaluated in comparison with other results to control order
a.sort(key=lambda x: x % 2)
print(a)

b = sorted(a, reverse=True)
print(b)
