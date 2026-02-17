# Generator Comprehensions
# Generator are memory efficient iterators that generate items in memory.

daily_sales = [100, 200, 300, 400, 500]


total_sale = (sale for sale in daily_sales)
print(total_sale)

total_sales = [sale for sale in daily_sales]
print(total_sales)