# -----------------------------------------
# DICTIONARIES IN PYTHON - DETAILED NOTES
# -----------------------------------------

"""
1️⃣ What is a Dictionary?

- Collection of key-value pairs.
- Keys must be:
    ✔ Unique
    ✔ Immutable
    ✔ Hashable
- Values can be ANY data type.
- Dictionary is MUTABLE.
- Implemented internally using a HASH TABLE.

Important:
Dictionary preserves insertion order (Python 3.7+ officially).
"""


# -----------------------------------------
# Creating dictionary using dict()
# -----------------------------------------

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}") #Chai order: {'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}

"""
Internally:
Python calculates hash(key) to determine where to store it.
Example:
hash("type") → some integer
That integer determines the storage bucket.
"""


# -----------------------------------------
# Creating empty dictionary
# -----------------------------------------

chai_recipe = {}

# Adding key-value pairs
chai_recipe["water"] = "200ml"
chai_recipe["milk"] = "100ml"

print(f"Chai recipe: {chai_recipe}")  #Chai recipe: {'water': '200ml', 'milk': '100ml'}
print(f"Water quantity: {chai_recipe['water']}") #Water quantity: 200ml

"""
Time Complexity:
Insertion → O(1) average
Lookup → O(1) average
Worst case (rare hash collisions) → O(n)
"""


# -----------------------------------------
# Deleting a key-value pair
# -----------------------------------------

del chai_recipe["milk"]
print(f"Chai recipe after deletion: {chai_recipe}") #Chai recipe after deletion: {'water': '200ml'}

"""
del removes key completely.
If key not found → KeyError.
"""


# -----------------------------------------
# MEMBERSHIP TESTING
# -----------------------------------------

"""
'in' checks ONLY keys.
It does NOT check values.

Because dictionary lookup is based on key hashing.
"""

print(f"Is 'sugar' in chai_order? {'sugar' in chai_order}") #Is 'sugar' in chai_order? True
print(f"Is 'water' in chai_recipe? {'water' in chai_recipe}") #Is 'water' in chai_recipe? True


# -----------------------------------------
# Accessing keys, values, items
# -----------------------------------------

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

print(f"Keys: {chai_order.keys()}")
print(f"Values: {chai_order.values()}")
print(f"Items (key-value pairs): {chai_order.items()}")

"""
keys(), values(), items() return VIEW objects.

They are dynamic.
If dictionary changes, these views reflect changes.
"""


# -----------------------------------------
# popitem()
# -----------------------------------------

"""
popitem() removes last inserted key-value pair.
(Works like stack - LIFO)
Python 3.7+ preserves insertion order.
"""

last_item = chai_order.popitem()
print(f"Last item removed: {last_item}") #Last item removed: ('sugar', 1)
print(f"Chai order after popitem: {chai_order}") # {'type': 'Ginger Chai', 'size': 'Medium'}


# -----------------------------------------
# update()
# -----------------------------------------

"""
update() merges another dictionary.
If key already exists → value gets overwritten.
"""

extra_spices = {"cardamom": "1 tsp", "cinnamon": "1/2 tsp"}
chai_recipe.update(extra_spices)

print(f"Chai recipe after update: {chai_recipe}") # {'water': '200ml', 'cardamom': '1 tsp', 'cinnamon': '1/2 tsp'}


# -----------------------------------------
# SAFE ACCESS
# -----------------------------------------

"""
Accessing non-existing key using [] raises KeyError.
"""

# customer_note = chai_order["bear"]  ❌ KeyError

"""
Use .get(key, default_value)
Returns default if key not found.
Does NOT raise error.
"""

customer_note = chai_order.get("size", "No note")
print(f"Customer note: {customer_note}")


# -----------------------------------------
# 🔥 IMPORTANT INTERNAL CONCEPTS
# -----------------------------------------

"""
1️⃣ Dictionary is mutable
   - You can change values
   - You can add/remove keys
   - Object reference remains same

2️⃣ Keys must be HASHABLE
   - Immutable objects
   - Must have __hash__() and __eq__()

3️⃣ Hash Collision Handling
   - If two keys produce same hash,
     Python checks equality to resolve collision.

4️⃣ Dictionary vs Set
   - Set = only keys (no values)
   - Dictionary = key + value

5️⃣ Time Complexity Summary
   - Insert → O(1) avg
   - Delete → O(1) avg
   - Lookup → O(1) avg
   - Worst case → O(n)
"""
