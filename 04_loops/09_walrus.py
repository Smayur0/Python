# -----------------------------------------
# Walrus Operator (:=) — Deep Explanation
# -----------------------------------------

"""
Walrus operator (Assignment Expression)
Introduced in Python 3.8

Syntax:
    variable := expression

It does TWO things:
1. Assigns value to variable
2. Returns that value

So it can be used inside conditions, loops, etc.
"""


# -------------------------------------------------
# 1️⃣ Modulus Example
# -------------------------------------------------

value = 13

if (reminder := value % 5):
    # Step 1: value % 5 → 13 % 5 → 3
    # Step 2: reminder = 3
    # Step 3: if 3 → True (non-zero is truthy)
    print(f"Not divisible, reminder is {reminder}")

"""
Key Concept:
- 0 → False
- Non-zero numbers → True
- So this pattern checks divisibility AND stores remainder.

Equivalent without walrus:

reminder = value % 5
if reminder:
"""


# -------------------------------------------------
# 2️⃣ Assignment inside membership check
# -------------------------------------------------

available_sizes = ["medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    # Execution order:
    # 1. input() runs
    # 2. requested_size gets assigned
    # 3. membership check happens
    print(f"Serving {requested_size} chai")
else:
    print(f"{requested_size} is not available")

"""
Benefit:
- Avoids repeating input()
- Keeps assignment close to usage
- Cleaner than assigning above the if
"""


# -------------------------------------------------
# 3️⃣ While loop with walrus
# -------------------------------------------------

flavors = ["vanilla", "chocolate", "strawberry"]
print("Available flavors:", flavors)

while (flavor := input("choose your flavor: ")) not in flavors:
    # Each iteration:
    # 1. input() executes
    # 2. flavor gets assigned
    # 3. condition checked
    print(f"sorry, {flavor} is not available")

print(f"you choose {flavor} Chai")

"""
Why this is powerful:

Without walrus, you'd need:

flavor = input(...)
while flavor not in flavors:
    print(...)
    flavor = input(...)

Walrus removes duplication and keeps logic compact.
"""


# -------------------------------------------------
# Important Notes
# -------------------------------------------------

"""
✔ Useful when:
- You need the computed value inside condition
- Avoiding duplicate expensive calls
- Cleaner loop patterns

❌ Avoid when:
- Condition becomes hard to read
- Too many nested assignments
- Reduces clarity

Rule of thumb:
If it improves readability → use it.
If it makes code dense → avoid it.
"""
