staff = [("amit", 18), ("sara", 25), ("john", 30), ("lisa", 22)]
# list of tuples → unpacking inside loop

for name, age in staff:
    # tuple unpacking per iteration

    if age > 30:
        print(f"{name} is eligible for retirement")
        break   # exits loop immediately if condition met

else:
    # executes ONLY if loop completes normally
    # (i.e., no break was triggered)
    print("no one is eligible for retirement")
