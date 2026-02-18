# -----------------------------------------
# Generator with send() – Two-Way Communication
# -----------------------------------------

def chai_customer():
    print("Welcome ! What chai would you like ?")

    order = yield
    # First yield pauses the generator.
    # It waits to RECEIVE a value from outside.
    # That received value gets assigned to `order`.

    while True:
        print(f"Preparing: {order}")

        order = yield
        # After preparing, generator pauses again.
        # Next .send(value) will resume execution
        # and assign the new value to `order`.


# Create generator instance (does NOT run body fully)
stall = chai_customer()

next(stall)
# Prime the generator.
# Execution runs until first `yield`.
# Now generator is paused and ready to receive data.

stall.send("Masala chai")
# "Masala chai" gets assigned to `order`
# Loop prints → Preparing: Masala chai
# Pauses again at next yield

stall.send("Ginger chai")
# Same flow repeats with new value
