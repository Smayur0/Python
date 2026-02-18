# =========================================
# BASIC DECORATOR + functools.wraps
# =========================================

"""
What is a Decorator?

A decorator is a function that:
✔ Takes another function as input
✔ Adds extra behavior
✔ Returns a modified function

It works because:
- Functions are first-class objects in Python
"""


# -----------------------------------------
# Basic Decorator Example
# -----------------------------------------

from functools import wraps

def my_decorator(func):

    @wraps(func)   # Preserves original function metadata
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


@my_decorator
def greet():
    print("Hello from decorator class")


greet()
print(greet.__name__)
