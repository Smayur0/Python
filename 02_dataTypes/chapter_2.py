# ==========================================
# PYTHON SETS, MUTABILITY & MEMORY (id)
# ==========================================


# -------------------------------
# 1️⃣ CREATING A SET
# -------------------------------

amt = set()
# set() → creates an empty set object
#
# Set is:
# - A built-in data type
# - Unordered
# - Mutable
# - Stores unique elements (no duplicates)
#
# amt is a variable (reference)
# It points to a set object stored in memory

print(f"amt is {amt}")
print(f"ID of amt is {id(amt)}")
# id(amt) → returns the memory identity of the set object


# -------------------------------
# 2️⃣ ADDING ELEMENTS TO SET
# -------------------------------

amt.add(2)
amt.add(22)

# .add() is a method of set object.
#
# Important concept:
# Sets are MUTABLE.
# That means:
# The object itself can change without creating a new object.
#
# When we call amt.add(2):
# - Python modifies the existing set object
# - It does NOT create a new set
# - The memory address remains the same

print(f"amt is {amt}")
print(f"ID of amt is {id(amt)}")


# -------------------------------
# 🧠 KEY CONCEPTS YOU LEARNED
# -------------------------------
#
# Variable → Reference to an object
# Object → Data stored in memory
# Mutable → Can change after creation (set, list, dict)
# Immutable → Cannot change (int, float, str, tuple)
#
# Very Important Difference:
#
# Earlier (with integers):
# SUGAR_AMT = 2
# SUGAR_AMT = 12
# → Memory reference changed (new object)
#
# Here (with set):
# amt.add(2)
# → Memory reference stays same
# → Object content changes
#
# That is the core difference between:
# 🔹 Mutable objects
# 🔹 Immutable objects


# -------------------------------
# 🔥 Interview-Level Insight
# -------------------------------
#
# id(amt) before and after add()
# stays the SAME because set is mutable.
#
# If it was immutable (like int),
# the id would change after reassignment.
#
# Python stores objects in heap memory,
# and variables are just labels pointing to them.

# ========================================== Chapter - 9  Detailed description of Python Sets ==========================================