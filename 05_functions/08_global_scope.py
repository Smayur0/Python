chai_type = "plain"

def front_desk():
    print(f"Front desk order: {chai_type}")

    def kitchen():
        global chai_type  # This allows us to modify the global variable
        chai_type = "Irani"  # Modifying the global variable
        print(f"Kitchen received order: {chai_type}")
    kitchen()

front_desk()
print(f"Global chai type after kitchen modification: {chai_type}")