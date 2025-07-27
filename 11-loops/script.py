i = 0

while i < 10:
    v = i + 1
    print(f'even {v}') if not v % 2 else print(f'odd {v}')
    i += 1


for x in ['A', 'B', 'C']:
    code = ord(x)
    char = chr(code)
    print(char)


for x in range(0, 10, 2):
    print(x)
