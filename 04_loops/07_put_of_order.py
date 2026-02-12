falvours = ["Green", "Lemon", "Spiced", "Out of stock", "Discontinued", "Mint"]

for flavour in falvours:

    if flavour == "Out of stock":
        # skip this iteration and move to next item
        continue

    if flavour == "Discontinued":
        # terminate loop completely
        print(f"{flavour} is no longer available")
        break

    print(f"{flavour} item found")

print("End of menu")
