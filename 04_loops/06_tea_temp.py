temp = 5
# initial state

while temp < 100:
    # condition checked before every iteration (pre-check loop)
    # loop continues while condition is True

    temp += 15
    # increment step (prevents infinite loop)
    # equivalent to: temp = temp + 15

    print(f"current temperature is {temp}")

print("Tea is ready to boil")
