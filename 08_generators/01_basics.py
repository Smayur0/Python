# -----------------------------------------
# Generator Concept in Python
# -----------------------------------------

"""
Generator = function that produces values lazily using `yield`.

Key idea:
- Normal function → computes everything and returns once.
- Generator → pauses execution and resumes from last state.

Useful when:
- Working with large datasets
- Streaming data
- Memory efficiency is important
"""


# ------------------ Generator Function ------------------

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

# Calling generator does NOT execute function body immediately
chai = serve_chai()   # returns a generator object

# Iteration triggers execution
# for tea in chai:
#     print(tea)

"""
How it works internally:
- Each `yield` pauses the function.
- State (local variables + instruction pointer) is preserved.
- Next call resumes from where it stopped.
"""


# ------------------ Normal Function ------------------

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

"""
Normal function:
- Executes completely
- Allocates full list in memory
- Returns once
"""


# ------------------ Another Generator ------------------

def get_chai_gen():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

gen_chai = get_chai_gen()

print(next(gen_chai))   # resumes → first yield
print(next(gen_chai))   # resumes → second yield
print(next(gen_chai))   # resumes → third yield
# print(next(gen_chai))  # StopIteration (no more values)

"""
Important Concepts:

1️⃣ next(generator)
   - Advances generator to next yield
   - Raises StopIteration when exhausted

2️⃣ Memory Efficient
   - Values produced on demand
   - No full list stored in memory

3️⃣ Lazy Evaluation
   - Execution happens only when requested

4️⃣ One-time iterable
   - Once exhausted, cannot reuse (need new generator)

Time Complexity:
- Same O(n) overall iteration
- Space complexity: O(1) extra (vs O(n) for list)

Mental Model:
Generator = paused function + saved execution state
"""
