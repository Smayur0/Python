# -----------------------------------------
# TUPLES IN PYTHON - DETAILED CONCEPT NOTES
# -----------------------------------------

"""
1️⃣ What is a Tuple?

A tuple is:
- An ordered collection (index-based)
- Immutable (cannot change after creation)
- Allows duplicate values
- Heterogeneous (can store different data types)
- Defined using parentheses ()

Example:
("a", 10, True)

Internally:
Tuple is an object of class 'tuple'.
Like strings, tuples are immutable.
"""

masala_spices = ("cumin", "coriander", "turmeric", "cardamom", "cloves")

# Tuple elements are ordered.
# Indexing works same as strings and lists.
# masala_spices[0] → "cumin"


# -----------------------------------------
# IMMUTABILITY CONCEPT
# -----------------------------------------

"""
Tuple is immutable.

This means:
- You cannot add elements
- You cannot remove elements
- You cannot modify elements

Example (would raise error):
masala_spices[0] = "pepper"

Why immutable?
- Memory optimization
- Safe data storage
- Can be used as dictionary keys (if elements are immutable)
"""


# -----------------------------------------
# TUPLE UNPACKING
# -----------------------------------------

"""
Tuple unpacking:
Assign tuple elements directly into variables.

Rule:
Number of variables must match number of elements.
"""

(first, second, third, fourth, fifth) = masala_spices

print(f"First spice: {first}")
print(f"Second spice: {second}")
print(f"Third spice: {third}")
print(f"Fourth spice: {fourth}")
print(f"Fifth spice: {fifth}")

"""
Internally:
Python assigns values positionally:
first  → index 0
second → index 1
...
"""


# -----------------------------------------
# MULTIPLE ASSIGNMENT
# -----------------------------------------

"""
Multiple assignment:
Assign multiple variables in a single line.

This actually creates a tuple on the right side.
"""

ginger_ratio, cardamom_ratio = 2, 1

# Internally this is:
# (ginger_ratio, cardamom_ratio) = (2, 1)

print(f"Ginger ratio: {ginger_ratio}")
print(f"Cardamom ratio: {cardamom_ratio}")


# -----------------------------------------
# SWAPPING VARIABLES
# -----------------------------------------

"""
Python allows swapping without temp variable.

Behind the scenes:
Python creates a temporary tuple.

Example:
a, b = b, a

Internally:
(a, b) = (b, a)
"""

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"After swapping:")
print(f"Ginger ratio: {ginger_ratio}")
print(f"Cardamom ratio: {cardamom_ratio}")


# -----------------------------------------
# MEMBERSHIP TESTING
# -----------------------------------------

"""
'in' operator checks whether element exists.

Time Complexity:
O(n) → Linear search
Because tuple does not use hashing like set.
"""

print("cumin" in masala_spices)    # True
print("pepper" in masala_spices)   # False


# -----------------------------------------
# 🧠 IMPORTANT CONCEPT SUMMARY
# -----------------------------------------

"""
1️⃣ Tuple is ordered & immutable.
2️⃣ Supports indexing and slicing.
3️⃣ Allows duplicate values.
4️⃣ Faster than list (slightly) because immutable.
5️⃣ Can be used as dictionary keys (if contents immutable).
6️⃣ Unpacking assigns elements positionally.
7️⃣ Swapping uses tuple packing/unpacking internally.
8️⃣ Membership testing is O(n).
"""
