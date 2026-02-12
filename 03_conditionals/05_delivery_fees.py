order_amt = int(input("Enter the order amt:"))
# input() → returns string
# int() → explicit type casting (raises ValueError if input is not numeric)

print(f"Order amt is {order_amt}")

# Ternary (conditional expression)
# Syntax: value_if_true if condition else value_if_false
# Expression-based (returns a value), unlike normal if-statement
delivery_fee = 0 if order_amt > 300 else 30

print(f"Delivery fee is {delivery_fee}")
