# ------------------ FOR LOOPS ------------------

print("\n--- FOR loop over list ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

print("\n--- FOR loop over string ---")
for char in "hello":
    print("Char:", char)

print("\n--- FOR loop over range ---")
for i in range(3):
    print("Index:", i)

print("\n--- FOR loop with range(start, stop, step) ---")
for i in range(1, 10, 2):
    print("Odd number:", i)

print("\n--- FOR loop with enumerate (index + value) ---")
for i, fruit in enumerate(fruits):
    print(f"Index {i} -> {fruit}")

print("\n--- FOR loop with zip (parallel iteration) ---")
prices = [0.5, 0.75, 1.2]
for fruit, price in zip(fruits, prices):
    print(f"{fruit} costs {price}€")

# ------------------ DICTIONARY LOOPS ------------------

person = {"name": "Alex", "age": 30, "job": "dev"}

print("\n--- FOR loop over dict keys ---")
for key in person:
    print("Key:", key)

print("\n--- FOR loop over dict keys (explicit) ---")
for key in person.keys():
    print(f"{key} -> {person[key]}")

print("\n--- FOR loop over dict values ---")
for val in person.values():
    print("Value:", val)

print("\n--- FOR loop over dict items (key, value) ---")
for key, val in person.items():
    print(f"{key} = {val}")

# ------------------ WHILE LOOPS ------------------

print("\n--- WHILE loop example ---")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# ------------------ BREAK / CONTINUE ------------------

print("\n--- BREAK example ---")
for fruit in fruits:
    if fruit == "banana":
        print("Found banana, stopping")
        break
    print("Checking:", fruit)

print("\n--- CONTINUE example ---")
for fruit in fruits:
    if fruit == "banana":
        print("Skipping banana")
        continue
    print("Processing:", fruit)

# ------------------ FOR-ELSE / WHILE-ELSE ------------------

print("\n--- FOR-ELSE example ---")
for i in range(3):
    print("Trying", i)
else:
    print("Loop finished without break")

print("\n--- WHILE-ELSE example ---")
count = 0
while count < 3:
    print("While running", count)
    count += 1
else:
    print("While finished")

# ------------------ LIST COMPREHENSIONS (1-liner loops) ------------------

print("\n--- List comprehension ---")
squares = [x**2 for x in range(5)]
print("Squares:", squares)

print("\n--- List comprehension with condition ---")
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)
