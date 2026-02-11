import sys
from fractions import Fraction
from decimal import Decimal as D

ideal_temp = 95.5
current_temp = 95.99

print(f"Current temperature is {current_temp}") # False due to precision issues
print(f"ideal temp is {ideal_temp}") # False due to precision issues
print(f"Difference is {ideal_temp - current_temp}") # False due to precision issues

print(sys.float_info) # details of float precision and limits