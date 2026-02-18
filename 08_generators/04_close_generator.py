# -----------------------------------------
# yield from → Generator Delegation
# -----------------------------------------

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    # `yield from` delegates iteration to another generator
    # Equivalent to:
    # for item in local_chai():
    #     yield item
    yield from local_chai()
    yield from imported_chai()

# Iterates seamlessly over both generators
for chai in full_menu():
    print(chai)

"""
Key Concept: yield from

✔ Flattens nested generators
✔ Passes through values directly
✔ Cleaner than manual for-loop delegation
✔ Also forwards send(), throw(), close() to sub-generator

Mental model:
full_menu() becomes a pipeline combining multiple generators.
"""


# -----------------------------------------
# Generator close() and exception handling
# -----------------------------------------

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order!"
            # Generator yields a message
            # Then pauses waiting for next interaction

    except:
        # When close() is called,
        # Python raises GeneratorExit inside the generator
        print("Stall closed, No more chai")


stall = chai_stall()

print(next(stall))
# Starts generator
# Runs until first yield
# Prints: "Waiting for chai order!"

stall.close()
# close() raises GeneratorExit inside generator
# Execution jumps to except block
# Cleanup message printed


"""
Deep Concepts:

1️⃣ yield from
   - Delegates control to sub-generator
   - Handles iteration automatically
   - Propagates values + exceptions

2️⃣ close()
   - Raises GeneratorExit inside generator
   - Allows cleanup logic
   - After close(), generator cannot resume

3️⃣ Generator lifecycle:
   - Created
   - Running
   - Paused (at yield)
   - Closed (via exhaustion or close())

4️⃣ Important:
   Never suppress GeneratorExit silently.
   Proper generators either:
   - Let it propagate
   - Or clean up resources properly

Use cases:
- Streaming pipelines
- Delegation chains
- Resource management
"""
