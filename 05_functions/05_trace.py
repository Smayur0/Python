def add_vat(price, vat_rate):
   return price *(100+ vat_rate) / 100

orders = [100, 200, 300]
for price in orders:
    final = add_vat(price, 20)
    print(f"Final price for order ${price}: ${final}")