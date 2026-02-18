# -----------------------------------------
# Infinite Generator Example
# -----------------------------------------

def infinite_chai():
    count = 1

    while True:
        # infinite loop (runs forever unless externally stopped)
        yield f"Refill #{count}"
        # execution pauses here and state is preserved

        count += 1
        # when resumed, continues from here


# Each function call creates a NEW generator instance
refill = infinite_chai()
refill_user2 = infinite_chai()

"""
Important:
- Generators maintain their own internal state.
- refill and refill_user2 are completely independent.
- Each has its own `count` variable.
"""


# Consume first generator (3 values)
for _ in range(3):
    print(next(refill))
    # next() resumes execution until next yield


# Consume second generator (5 values)
for _ in range(5):
    print(next(refill_user2))


"""
Deep Concepts:

1️⃣ Infinite Generator
   - while True makes it unbounded.
   - Must control consumption externally.
   - Useful for streams, polling, event loops.

2️⃣ Lazy Evaluation
   - No memory growth.
   - Only one value exists at a time.

3️⃣ Independent State
   - Each generator call has its own frame + local variables.
   - Equivalent to separate paused function executions.

4️⃣ StopIteration?
   - Won’t occur here naturally (infinite loop).
   - Only stops if externally broken.

Time Complexity:
- O(k) where k = number of times next() is called.
Space Complexity:
- O(1) constant memory.
"""
