# ------------------ PYTHON SYNTAX SHORTCUTS & ONE-LINERS ------------------

# ---------- TERNARY (if-else in one line) ----------
age = 18
status = "adult" if age >= 18 else "minor"
print("Ternary:", status)

# ---------- NULLISH COALESCING / DEFAULT FALLBACK ----------
name = None
display = name or "Anonymous"
print("Fallback (or):", display)

# ---------- SHORT-CIRCUIT EVALUATION ----------
x = True and "Yes"
y = False or "Default"
print("Short-circuit AND:", x)
print("Short-circuit OR:", y)

# ---------- WALRUS OPERATOR (:=) ----------
if (n := len("hello")) > 3:
    print("Walrus operator captured length:", n)

# ---------- LIST COMPREHENSION ----------
squares = [x * x for x in range(5)]
print("Squares:", squares)

# ---------- SET COMPREHENSION ----------
evens = {x for x in range(10) if x % 2 == 0}
print("Even set:", evens)

# ---------- DICT COMPREHENSION ----------
mapping = {str(i): i * i for i in range(3)}
print("Dict:", mapping)

# ---------- DESTRUCTURING / UNPACKING ----------
a, b = [1, 2]
print("Unpacked:", a, b)

# ---------- SWAPPING VALUES ----------
a, b = b, a
print("Swapped:", a, b)

# ---------- SLICE SHORTCUTS ----------
s = "abcdef"
print("Last char:", s[-1])
print("Reverse string:", s[::-1])
print("Middle slice:", s[1:4])

# ---------- LAMBDA ONE-LINER FUNCTION ----------
double = lambda x: x * 2
print("Lambda result:", double(4))

# ---------- ANY / ALL ----------
nums = [1, 0, 3]
print("Any true?", any(nums))
print("All true?", all(nums))

# ---------- ZIP / ENUMERATE ----------
for i, val in enumerate(["a", "b"]):
    print(f"Index {i}: {val}")

for x, y in zip([1, 2], ["a", "b"]):
    print(f"Zip: {x} -> {y}")

# ---------- F-STRINGS ----------
name = "Buddy"
age = 99
print(f"My name is {name}, I'm {age} years old.")


# ---------- ARGS / KWARGS ----------
def show(*args, **kwargs):
    print("ARGS:", args)
    print("KWARGS:", kwargs)


show(1, 2, 3, name="Alex", lang="Python")

# ---------- FOR-ELSE / WHILE-ELSE ----------
for i in range(3):
    print("Trying:", i)
else:
    print("Completed without break")

x = 0
while x < 2:
    print("Counting:", x)
    x += 1
else:
    print("While ended normally")

# ---------- WITH CONTEXT ----------
with open("example.txt", "w") as f:
    f.write("Hello from with statement!")
