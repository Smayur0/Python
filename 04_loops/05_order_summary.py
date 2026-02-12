names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
bills  = [50, 100, 200, 400, 0]

# zip(iterable1, iterable2)
# pairs elements by position → returns tuples
# iteration stops at the shortest iterable

for name, bill in zip(names, bills):
    print(f"{name} paid {bill} rupees")
