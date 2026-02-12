seat_type = input("Enter ticket type (sleeper/AC/general/luxury): ").lower()
# normalize input for consistent pattern matching

match seat_type:
    case "sleeper":
        print("Sleeper ticket")

    case "ac":
        print("AC ticket")

    case "general":
        print("General ticket")

    case "luxury":
        print("Luxury ticket")

    case _:
        # wildcard (default case)
        print("Invalid ticket type")
