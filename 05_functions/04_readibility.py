def calculate_bill(cups, price_per_cup):
    total_cost = cups * price_per_cup
    return total_cost

my_bill = calculate_bill(3, 15)
print(f"Total bill: ${my_bill}")