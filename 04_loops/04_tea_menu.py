menu = ["Green", "Lemon", "Spiced", "Mint"]
# ordered list of items

# enumerate(iterable, start)
# returns (index, value) pairs while iterating
# avoids manual counter management

for idx, item in enumerate(menu, start=1):
    # start=1 → indexing begins from 1 instead of default 0
    print(f"{idx} : {item} chai")
