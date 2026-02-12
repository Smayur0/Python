# ==========================================
# PYTHON NUMBERS & ARITHMETIC OPERATORS
# ==========================================

# In Python:
# - int → Whole numbers (immutable)
# - float → Decimal numbers (immutable)
# - Arithmetic operations create NEW objects


# -------------------------------
# 1️⃣ ADDITION (+)
# -------------------------------

black_tea = 14      # integer object
ginger_tea = 4      # integer object

total_tea = black_tea + ginger_tea
# + operator performs addition
# 14 + 4 = 18
# Python creates a NEW integer object (18)
# total_tea now references that object

print(f"Total tea is {total_tea} grams")


# -------------------------------
# 2️⃣ SUBTRACTION (-)
# -------------------------------

remaining_tea = black_tea - ginger_tea
# - operator performs subtraction
# 14 - 4 = 10
# Again, a new integer object is created

print(f"Remaining tea is {remaining_tea} grams")


# -------------------------------
# 3️⃣ DIVISION (/)
# -------------------------------

milk_liter = 5
servings = 2

milk_per_serving = milk_liter / servings
# / operator performs TRUE division
# IMPORTANT: Always returns a float
# 5 / 2 = 2.5 (float)

print(f"Milk per serving is {milk_per_serving} liters")


# -------------------------------
# 4️⃣ FLOOR DIVISION (//)
# -------------------------------

total_tea_bags = 5
pots = 2

bags_per_pot = total_tea_bags // pots
# // operator performs floor division
# It removes the decimal part
# 5 // 2 = 2 (not 2.5)

print(f"Bags per pot is {bags_per_pot}")


# -------------------------------
# 5️⃣ MODULUS (%)
# -------------------------------

total_cadmon_pods = 10
pods_per_tea = 3

leftover_pods = total_cadmon_pods % pods_per_tea
# % operator returns remainder after division
# 10 % 3 = 1
# (Because 10 = 3*3 + 1)

print(f"Leftover pods are {leftover_pods}")


# -------------------------------
# 6️⃣ EXPONENT (**)
# -------------------------------

base_flavor = 2
scale_factor = 3

scaled_flavor = base_flavor ** scale_factor
# ** operator means "power"
# 2 ** 3 = 2 * 2 * 2 = 8

print(f"Scaled flavor is {scaled_flavor}")


# -------------------------------
# 7️⃣ UNDERSCORE IN NUMBERS
# -------------------------------

total_leaves = 1_000_000
# Underscores improve readability
# Python ignores underscores in numbers
# 1_000_000 == 1000000

print(f"Total leaves is {total_leaves}")


# ==========================================
# 🧠 IMPORTANT CONCEPTS
# ==========================================

# 1. Integers and floats are IMMUTABLE
#    → Operations create new objects.

# 2. /  always returns float
# 3. // returns floor (integer result if both are int)
# 4. %  gives remainder
# 5. ** means power

# Python integers:
# - Have unlimited precision
# - Automatically expand for large numbers
