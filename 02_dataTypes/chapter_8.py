# -----------------------------------------
# PYTHON LISTS (Dynamic Arrays) - DETAILED NOTES
# -----------------------------------------

"""
1️⃣ What is a List?

A List is:
- Ordered collection (index-based access)
- Mutable (can change after creation)
- Allows duplicate values
- Dynamic in size (can grow/shrink)
- Can store heterogeneous data types

Internally:
Python list is implemented as a dynamic array.
It stores references to objects (not actual objects).
"""

# Creating a list
ingredients = ["water", "milk", "black tea"]
# List object created in memory
# ingredients variable references that list


# -----------------------------------------
# LIST METHODS (Mutating Operations)
# -----------------------------------------

# 1️⃣ append() → Adds element at end
ingredients.append("sugar")
# Time Complexity: Amortized O(1)
# Adds new element at the end

print(f"Ingredients after append: {ingredients}")


# 2️⃣ remove() → Removes first matching value
ingredients.remove("milk")
# Time Complexity: O(n)
# Searches for value and removes it

print(f"After removing milk: {ingredients}")


# 3️⃣ extend() → Adds multiple elements
spices_options = ["cinnamon", "cardamom"]
ingredients.extend(spices_options)
# Time Complexity: O(k)
# Adds each element from iterable

print(f"After extend: {ingredients}")


# 4️⃣ insert(index, value) → Insert at specific position
ingredients.insert(2, "ginger")
# Time Complexity: O(n)
# Elements after index shift right

print(f"After insert: {ingredients}")


# 5️⃣ pop() → Removes and returns element
last_added = ingredients.pop()
# Default: removes last element (O(1))
# pop(index) → O(n)

print(f"Last added ingredient removed: {last_added}")
print(f"After pop: {ingredients}")


# 6️⃣ reverse() → Reverse list in-place
ingredients.reverse()
# Time Complexity: O(n)
# Modifies same list object

print(f"After reverse: {ingredients}")


# 7️⃣ sort() → Sort list in ascending order
ingredients.sort()
# Time Complexity: O(n log n)
# Uses Timsort (hybrid sorting algorithm)
# Modifies list in-place

print(f"After sort: {ingredients}")


# -----------------------------------------
# BUILT-IN FUNCTIONS (Non-mutating)
# -----------------------------------------

sugar_levels = [1, 2, 3, 4, 5]

print(f"Sugar levels: {sugar_levels}")

print(f"Max sugar level: {max(sugar_levels)}")
# max() → returns largest element

print(f"Min sugar level: {min(sugar_levels)}")
# min() → returns smallest element


# -----------------------------------------
# OPERATOR OVERLOADING
# -----------------------------------------

base_liquid = ["water", "milk"]
extra_flavors = ["ginger"]

# + → Concatenation
liquid_mix = base_liquid + extra_flavors
# Creates NEW list
# Does NOT modify original lists

print(f"Liquid mix: {liquid_mix}")

# * → Repetition
strong_brew = base_liquid * 2
# Repeats elements
# Creates NEW list

print(f"Strong brew: {strong_brew}")


# -----------------------------------------
# BYTEARRAY (Mutable Binary Data)
# -----------------------------------------

"""
bytearray:
- Mutable sequence of bytes
- Used for binary data manipulation
- Similar to list of integers (0–255)
"""

raw_spice_data = bytearray(b"CINNAMON")

# Replace bytes
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
# replace() returns new bytearray

print(f"Raw spice data: {raw_spice_data}")


# -----------------------------------------
# 🧠 IMPORTANT CONCEPT SUMMARY
# -----------------------------------------

"""
1️⃣ List is mutable and dynamic.
2️⃣ Stores references to objects.
3️⃣ append() → O(1)
4️⃣ remove(), insert() → O(n)
5️⃣ sort() → O(n log n)
6️⃣ + and * create new lists.
7️⃣ reverse() and sort() modify in-place.
8️⃣ bytearray is mutable binary container.
"""
