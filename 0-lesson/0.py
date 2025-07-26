# ------------------ STRINGS ------------------

s = " Hello Buddy "

print("Original:", repr(s))
print("strip():", s.strip())  # Remove surrounding spaces
print("lower():", s.lower())  # Lowercase
print("upper():", s.upper())  # Uppercase
print("replace():", s.replace("Buddy", "World"))  # Replace
print("startswith(' '):", s.startswith(" "))  # True
print("endswith(' '):", s.endswith(" "))  # True
print("split():", s.split())  # Split into list
print("find('Buddy'):", s.find("Buddy"))  # Index of "Buddy"
print("'yo' in s:", "yo" in s)  # Check if "yo" in string
print("s * 3:", s * 3)  # Repeat string

# ------------------ LISTS ------------------

nums = [1, 2, 3]
print("\nOriginal nums:", nums)
nums.append(4)
print("append(4):", nums)
nums.insert(0, 0)
print("insert(0, 0):", nums)
nums.pop()
print("pop():", nums)
nums.remove(2)
print("remove(2):", nums)
nums.sort()
print("sort():", nums)
nums.reverse()
print("reverse():", nums)
print("nums * 2:", nums * 2)
print("[1, 2] + [3, 4]:", [1, 2] + [3, 4])

# ------------------ DICTIONARIES ------------------

person = {"name": "Alex", "age": 30}
print("\nOriginal dict:", person)
print("person['age']:", person["age"])
print("person.get('email'):", person.get("email"))
person["job"] = "dev"
print("Added job:", person)
print("keys():", list(person.keys()))
print("values():", list(person.values()))
print("items():", list(person.items()))

# ------------------ TUPLES ------------------

coords = (10, 20)
x, y = coords
print("\nTuple coords:", coords)
print("Unpacked:", x, y)

# ------------------ SETS ------------------

a = {1, 2, 3}
b = {3, 4, 5}
print("\nSet a:", a)
print("Set b:", b)
print("union():", a.union(b))
print("intersection():", a.intersection(b))
print("difference():", a.difference(b))
print("a | b:", a | b)
print("a & b:", a & b)
print("a - b:", a - b)

# ------------------ NUMBERS ------------------

print("\nMath with ints and floats")
print("10 / 3:", 10 / 3)  # Float division
print("10 // 3:", 10 // 3)  # Floor division
print("10 % 3:", 10 % 3)  # Modulo
print("2 ** 3:", 2**3)  # Power

# ------------------ TYPE CONVERSION ------------------

print("\nType conversions:")
print("str(123):", str(123))
print("int('42'):", int("42"))
print("float('3.14'):", float("3.14"))
print("list('abc'):", list("abc"))

# ------------------ TYPE CHECK ------------------

print("\nType checks:")
print("type('hi'):", type("hi"))
print("type(123):", type(123))
print("type(3.14):", type(3.14))
print("type([]):", type([]))
print("type({}):", type({}))
print("type(()):", type(()))
print("type(set()):", type(set()))
