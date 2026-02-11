# -------------------------------
# Tuples in Python - Chapter 7
# -------------------------------

"""
1. A Tuple is an ordered, immutable collection.
2. Defined using parentheses ().
3. Allows duplicate values.
4. Faster than lists (slightly) because immutable.
5. Used when data should NOT change.
"""

masla_spices = ("cumin", "coriander", "turmeric", "cardamom", "cloves")


# -------------------------------
# Tuple Unpacking
# -------------------------------

"""
Tuple unpacking:
We can assign tuple elements to variables directly.
Number of variables must match number of elements.
"""

(first, second, third, fourth, fifth) = masla_spices

print(f"First spice: {first}, second spice: {second}, third spice: {third}, fourth spice: {fourth}, fifth spice: {fifth}")


# -------------------------------
# Multiple Assignment
# -------------------------------

"""
Python allows assigning multiple variables in one line.
This is called multiple assignment.
"""

ginger_ratio, cadramom_ratio = 2, 1

print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cadramom_ratio}")


# -------------------------------
# Swapping Variables
# -------------------------------

"""
Python allows swapping without temporary variable.
Internally it creates a temporary tuple.
"""

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio

print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cadramom_ratio}")


# -------------------------------
# Membership Testing
# -------------------------------

"""
We can check if an element exists in a tuple using 'in'.
Time Complexity: O(n)
"""

print("cumin" in masla_spices)
print("pepper" in masla_spices)
