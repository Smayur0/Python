snack = input("Enter you favorite snack: ").lower()
# normalize input to avoid case mismatch

if snack == "cookies" or snack == "samosa":
    # logical OR → condition is True if any operand is True
    # evaluated left to right (short-circuiting applies)
    print(f"Great choice : {snack} ")
else:
    print("We only serve samosa and cookies")
