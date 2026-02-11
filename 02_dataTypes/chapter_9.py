# -------------------------------
# Python Sets 
# -------------------------------

"""
1. A Set is an unordered collection of unique elements.
2. Duplicates are automatically removed.
3. Sets are mutable (we can add/remove elements).
4. Lookup in sets is very fast (O(1) average time).
"""

# Creating sets
essential_spices = {"cardamom", "cinnamon", "ginger", "clove"}
optional_spices = {"ginger", "nutmeg"}

# 1️⃣ Union ( | )
# Combines both sets and removes duplicates
all_spices = essential_spices | optional_spices
print(f"All spices (Union): {all_spices}")

# 2️⃣ Intersection ( & )
# Returns common elements in both sets
common_spices = essential_spices & optional_spices
print(f"Common spices (Intersection): {common_spices}")

# 3️⃣ Difference ( - )
# Elements present in first set but not in second
only_in_essential = essential_spices - optional_spices
print(f"Only essential spices (Difference): {only_in_essential}")

# 4️⃣ Membership Testing (in)
# Very fast lookup (Hashing concept internally)
print(f"Is 'clove' an essential spice? {'clove' in essential_spices}")
