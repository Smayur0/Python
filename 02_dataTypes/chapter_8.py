# -------------------------------
# Python Lists (Arrays in Python)
# -------------------------------

"""
1. A List is an ordered, mutable collection.
2. Allows duplicate values.
3. Elements are indexed (index starts from 0).
4. Lists are dynamic in size.
"""

# Creating a list
ingredients = ["water", "milk", "black tea"]

# 1️⃣ append() → adds element at end
ingredients.append("sugar")
print(f"Ingredients after append: {ingredients}")

# 2️⃣ remove() → removes specific value
ingredients.remove("milk")
print(f"After removing milk: {ingredients}")

# 3️⃣ extend() → adds multiple elements
spices_options = ["cinnamon", "cardamom"]
ingredients.extend(spices_options)
print(f"After extend: {ingredients}")

# 4️⃣ insert(index, value) → insert at specific position
ingredients.insert(2, "ginger")
print(f"After insert: {ingredients}")

# 5️⃣ pop() → removes and returns last element
last_added = ingredients.pop()
print(f"Last added ingredient removed: {last_added}")
print(f"After pop: {ingredients}")

# 6️⃣ reverse() → reverse list order
ingredients.reverse()
print(f"After reverse: {ingredients}")

# 7️⃣ sort() → sorts list (ascending by default)
ingredients.sort()
print(f"After sort: {ingredients}")

# --------------------------------
# Built-in functions
# --------------------------------

sugar_levels = [1, 2, 3, 4, 5]
print(f"Sugar levels: {sugar_levels}")
print(f"Max sugar level: {max(sugar_levels)}")
print(f"Min sugar level: {min(sugar_levels)}")

# --------------------------------
# Operator Overloading in Lists
# --------------------------------

base_liquid = ["water", "milk"]
extra_flavors = ["ginger"]

# + → Concatenation
liquid_mix = base_liquid + extra_flavors
print(f"Liquid mix: {liquid_mix}")

# * → Repetition
strong_brew = base_liquid * 2
print(f"Strong brew: {strong_brew}")

# --------------------------------
# Bytearray (Mutable Binary Data)
# --------------------------------

raw_spice_data = bytearray(b"CINNAMON")

# Replace bytes
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Raw spice data: {raw_spice_data}")
