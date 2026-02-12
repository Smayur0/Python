cup = input("Choose your cup size (small, medium, large): ").lower()
# input() → always returns string
# .lower() → normalizes user input (avoids case mismatch issues)

if cup == "small":
    print("price is 10 rs")

elif cup == "medium":
    print("price is 20 rs")

elif cup == "large":
    print("price is 30 rs")

else:
    print("invalid cup size")
    # executes only if none of the above conditions match
