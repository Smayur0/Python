# ==========================================
# PYTHON VARIABLES, CONSTANTS & MEMORY (id)
# ==========================================


# -------------------------------
# 1️⃣ VARIABLE ASSIGNMENT
# -------------------------------
# SUGAR_AMT is a variable.
# In Python, a variable is just a reference (label) 
# that points to an object stored in memory.

SUGAR_AMT = 2   # Assignment statement
# Here:
# - 2 is an integer object
# - SUGAR_AMT is a reference name
# - '=' is the assignment operator
# Python creates integer object 2 in memory
# and SUGAR_AMT points to that object

print(f"sugar is {SUGAR_AMT} grams")
# f-string → formatted string literal
# It allows embedding variables inside string using {}


# -------------------------------
# 2️⃣ REASSIGNMENT
# -------------------------------
# Now we are changing the value

SUGAR_AMT = 12
# This does NOT change 2 into 12.
# Instead:
# - A new integer object 12 is created (if not already present)
# - SUGAR_AMT now points to 12
# - It stops pointing to 2

print(f"Second sugar is {SUGAR_AMT} grams")


# -------------------------------
# 3️⃣ MEMORY ADDRESS (id function)
# -------------------------------
# id() returns the identity of an object.
# It is usually the memory address where the object is stored.

print(f"ID of 2 is {id(2)}")
print(f"ID of 12 is {id(12)}")

# Important Concept:
# Python integers are immutable.
# Immutable means:
# Once created, their value cannot be changed.
#
# So when we wrote:
# SUGAR_AMT = 12
#
# Python did NOT modify 2.
# Instead, it made SUGAR_AMT point to a new object 12.


# -------------------------------
# 🧠 KEY TERMINOLOGY
# -------------------------------
#
# Variable        → A name that references an object
# Object          → Data stored in memory (like 2, 12, "chai")
# Assignment      → Binding a variable name to an object
# Immutable       → Cannot be changed after creation
# id()            → Returns unique identity of object
# f-string        → Modern way to format strings
#
# In Python:
# Everything is an object.
# Variables don't store values directly.
# They store references to objects.
