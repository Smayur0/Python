# ==========================================
# PYTHON FLOATING POINT PRECISION
# ==========================================

import sys
from fractions import Fraction
from decimal import Decimal as D

# ------------------------------------------
# 1️⃣ FLOAT NUMBERS (Floating Point)
# ------------------------------------------

ideal_temp = 95.5
current_temp = 95.99

# These are float objects.
# In Python, float is implemented using
# IEEE 754 double-precision (64-bit).

# Important Concept:
# Floats are stored in binary format.
# Some decimal numbers cannot be represented
# exactly in binary.
# This causes small precision errors.

print(f"Current temperature is {current_temp}")
print(f"Ideal temperature is {ideal_temp}")

# Subtracting floats can show precision issues
print(f"Difference is {ideal_temp - current_temp}")

# You might see something like:
# -0.4899999999999949 instead of -0.49
#
# This is NOT a bug.
# It happens because 95.99 cannot be represented
# exactly in binary floating-point form.


# ------------------------------------------
# 2️⃣ FLOAT INTERNAL DETAILS
# ------------------------------------------

print(sys.float_info)

# sys.float_info gives:
# - max value a float can hold
# - min value
# - epsilon (smallest difference between 1.0 and next float)
# - precision details
#
# epsilon (~2.22e-16) tells us how accurate floats are.


# ------------------------------------------
# 3️⃣ DECIMAL (High Precision Arithmetic)
# ------------------------------------------

# Decimal stores numbers in base-10 (decimal)
# Useful for financial calculations

a = D("95.5")
b = D("95.99")

print("Decimal Difference:", a - b)

# IMPORTANT:
# Always pass string to Decimal
# If you pass float, precision issue already exists.


# ------------------------------------------
# 4️⃣ FRACTION (Rational Numbers)
# ------------------------------------------

# Fraction stores numbers as numerator/denominator
# Exact rational arithmetic

f1 = Fraction(955, 10)
f2 = Fraction(9599, 100)

print("Fraction Difference:", f1 - f2)

# Fraction keeps exact precision
# No floating-point rounding error.


# ==========================================
# 🧠 IMPORTANT CONCEPTS
# ==========================================

# 1️⃣ Float uses binary representation (IEEE 754)
# 2️⃣ Some decimal values cannot be stored exactly
# 3️⃣ Small rounding errors are normal
# 4️⃣ Use Decimal for financial calculations
# 5️⃣ Use Fraction for exact rational math
# 6️⃣ sys.float_info shows float limits & precision
