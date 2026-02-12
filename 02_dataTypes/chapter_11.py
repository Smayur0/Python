# -----------------------------------------
# Working with Date & Time using Arrow
# -----------------------------------------

"""
Arrow is a third-party library (not built-in).
It makes working with datetime easier than Python's default datetime module.

Install using:
pip install arrow
"""

import arrow

"""
arrow.utcnow()

- Returns current time in UTC (Coordinated Universal Time).
- The object returned is an Arrow object (wrapper around datetime).
- It is timezone-aware.
"""

brew_time = arrow.utcnow()

"""
.to("Asia/Kolkata")

- Converts the timezone of the Arrow object.
- Important: .to() RETURNS A NEW OBJECT.
- It does NOT modify the original object (Arrow objects are immutable).
"""

brew_time = brew_time.to("Asia/Kolkata")

print(f"Current brew time in Kolkata: {brew_time}")

"""
Important Concept:
Arrow objects are IMMUTABLE.
So every transformation returns a new object.
This is similar to strings in Python.
"""


# -----------------------------------------
# namedtuple from collections
# -----------------------------------------

"""
namedtuple is a factory function that creates a subclass of tuple.

Why use it?

Normal tuple:
tea = ("Masala", "Large", 2)
Problem:
tea[0] → Not readable

namedtuple:
tea.type → More readable

It improves code readability while keeping tuple immutability.
"""

from collections import namedtuple

Tea = namedtuple("Tea", ["type", "size", "sugar"])

"""
Tea is now a class (tuple subclass).
Fields:
- type
- size
- sugar
"""

# Creating instance
my_tea = Tea("Masala", "Large", 2)

print(my_tea)
print(my_tea.type)
print(my_tea.size)
print(my_tea.sugar)

"""
Key Properties of namedtuple:

1️⃣ Immutable (like tuple)
   You cannot modify values after creation.

2️⃣ Memory efficient
   Uses less memory than normal class.

3️⃣ Access by name AND index
   my_tea[0] → "Masala"
   my_tea.type → "Masala"

4️⃣ Hashable (if elements are hashable)
   Can be used as dictionary keys.
"""


# -----------------------------------------
# Internal Understanding
# -----------------------------------------

"""
namedtuple internally:
- Creates a class dynamically
- Inherits from tuple
- Adds attribute access for fields
- Stores values in fixed positions

Equivalent conceptual structure:

class Tea(tuple):
    __slots__ = ()
    _fields = ("type", "size", "sugar")

But automatically generated.
"""
