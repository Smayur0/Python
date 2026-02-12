# -----------------------------------------
# PYTHON SETS - DETAILED CONCEPT NOTES
# -----------------------------------------

"""
1️⃣ What is a Set?

A Set is:
- Unordered collection (no indexing)
- Contains only UNIQUE elements
- Mutable (can add/remove elements)
- Uses hashing internally
- Very fast lookup (O(1) average time)

Internally:
A set is implemented using a hash table.
It stores elements based on their hash value.
"""

# Creating sets
essential_spices = {"cardamom", "cinnamon", "ginger", "clove"}
optional_spices = {"ginger", "nutmeg"}

"""
Important:
- Duplicate values are automatically removed.
- Order is NOT guaranteed.
- Elements must be hashable (immutable types only).
  Example:
  Allowed → int, str, tuple (if immutable elements)
  Not allowed → list, dict, set
"""


# -----------------------------------------
# 1️⃣ UNION ( | )
# -----------------------------------------

"""
Union combines elements from both sets.
Duplicates automatically removed.

Time Complexity: O(len(s1) + len(s2))
"""

all_spices = essential_spices | optional_spices
print(f"All spices (Union): {all_spices}")


# -----------------------------------------
# 2️⃣ INTERSECTION ( & )
# -----------------------------------------

"""
Intersection returns elements common in both sets.

Time Complexity: O(min(len(s1), len(s2)))
"""

common_spices = essential_spices & optional_spices
print(f"Common spices (Intersection): {common_spices}")


# -----------------------------------------
# 3️⃣ DIFFERENCE ( - )
# -----------------------------------------

"""
Difference returns elements present in first set
but NOT in second set.

Order does not matter.
"""

only_in_essential = essential_spices - optional_spices
print(f"Only essential spices (Difference): {only_in_essential}")


# -----------------------------------------
# 4️⃣ MEMBERSHIP TESTING (in)
# -----------------------------------------

"""
Membership check in set is VERY FAST.

Why?
Because sets use hashing.

Hashing process:
1. Python computes hash value of element.
2. Uses that hash to directly locate position.
3. Checks equality only if needed.

Average Time Complexity: O(1)
Worst case (rare collisions): O(n)
"""

print(f"Is 'clove' an essential spice? {'clove' in essential_spices}")


# -----------------------------------------
# 🧠 IMPORTANT INTERNAL CONCEPTS
# -----------------------------------------

"""
1️⃣ Set is mutable, but elements must be immutable.

2️⃣ No indexing:
   You cannot do essential_spices[0]

3️⃣ Order is not guaranteed.
   Printing may show different order.

4️⃣ Sets are optimized for:
   - Membership testing
   - Removing duplicates
   - Mathematical set operations

5️⃣ Behind the scenes:
   Set uses hash table (same concept as dictionary keys).
"""
