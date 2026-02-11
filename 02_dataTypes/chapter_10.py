# -------------------------------
# Dictionaries in Python - Chapter 10
# -------------------------------

"""
1. Dictionary is a collection of key-value pairs.
2. Keys must be unique and immutable (string, int, tuple).
3. Values can be of any data type.
4. Dictionaries are mutable.
5. Internally implemented using Hash Table.
"""

# Creating dictionary using dict()
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")


# Creating empty dictionary
chai_recipe = {}

# Adding key-value pairs
chai_recipe["water"] = "200ml"
chai_recipe["milk"] = "100ml"

print(f"Chai recipe: {chai_recipe}")
print(f"Water quantity: {chai_recipe['water']}")


# Deleting a key-value pair
del chai_recipe["milk"]
print(f"Chai recipe after deletion: {chai_recipe}")


# -------------------------------
# Membership Testing
# -------------------------------

"""
'in' checks only keys (NOT values).
Time Complexity: O(1) average
"""

print(f"Is 'sugar' in chai_order? {'sugar' in chai_order}")
print(f"Is 'water' in chai_recipe? {'water' in chai_recipe}")


# New dictionary
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

print(f"Keys: {chai_order.keys()}")
print(f"Values: {chai_order.values()}")
print(f"Items (key-value pairs): {chai_order.items()}")


# popitem() → removes last inserted key-value pair (Python 3.7+ preserves order)
last_item = chai_order.popitem()
print(f"Last item removed: {last_item}")
print(f"Chai order after popitem: {chai_order}")


# update() → merges dictionaries
extra_spices = {"cardamom": "1 tsp", "cinnamon": "1/2 tsp"}
chai_recipe.update(extra_spices)
print(f"Chai recipe after update: {chai_recipe}")


# -------------------------------
# Safe Access
# -------------------------------

"""
Accessing a non-existing key using [] raises KeyError.
"""

# customer_note = chai_order["bear"]  ❌ KeyError

# Use .get() to avoid error
customer_note = chai_order.get("size", "No note")
print(f"Customer note: {customer_note}")
