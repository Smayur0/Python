# ==========================================
# PYTHON BOOLEANS & LOGICAL OPERATORS
# ==========================================

# In Python:
# bool is a data type.
# It has only two values: True and False.
# IMPORTANT: bool is a subclass of int.
# True  = 1
# False = 0


# -------------------------------
# 1️⃣ Boolean + Integer (Type Behavior)
# -------------------------------

is_boiling = True        # Boolean value (internally equals 1)
string_count = 4         # Integer

total_actions = string_count + is_boiling
# Since bool is a subclass of int:
# True behaves like 1
# False behaves like 0
#
# So:
# 4 + True  → 4 + 1 → 5
# This is not exactly "upcasting"
# It works because bool inherits from int.

print(f"Total actions is {total_actions}")


# -------------------------------
# 2️⃣ Truthy and Falsy Values
# -------------------------------

miik_present = "jelkwsnd"
# Non-empty string → Truthy
# In Python:
# False values are:
#   0
#   0.0
#   None
#   ""
#   []
#   {}
#   set()
# Everything else is True (Truthy)

print(f"is there milk? {bool(miik_present)}")
# bool() converts a value to True or False


# -------------------------------
# 3️⃣ LOGICAL OPERATORS
# -------------------------------

is_morning = True
is_Evening = False


# 🔹 OR Operator
# Returns True if at least one condition is True

what_is_time = is_morning or is_Evening
# True or False → True

print(f"is it morning or evening? {what_is_time}")


# 🔹 AND Operator
# Returns True only if BOTH conditions are True

what_is_time = is_morning and is_Evening
# True and False → False

print(f"is it morning and evening? {what_is_time}")


# 🔹 NOT Operator
# Reverses the boolean value

what_is_time = not is_Evening
# not False → True

print(f"NOT evening? {what_is_time}")


# ==========================================
# 🧠 IMPORTANT CONCEPTS
# ==========================================

# 1️⃣ bool is subclass of int
#     True  = 1
#     False = 0

# 2️⃣ Logical Operators:
#     and  → both must be True
#     or   → at least one True
#     not  → reverses value

# 3️⃣ Short-Circuiting:
#     True or X  → stops at True
#     False and X → stops at False
# Python does not evaluate second condition if result is already known.

# 4️⃣ Truthy & Falsy:
#     Empty values → False
#     Non-empty values → True
