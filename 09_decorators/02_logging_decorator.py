# ==================================================
# DECORATORS WITH ARGUMENTS — COMPLETE SUMMARY
# ==================================================

"""
Problem:
Earlier decorator only worked for functions with NO parameters.

Solution:
Use *args and **kwargs inside wrapper
so it works for ANY function signature.
"""


# --------------------------------------------------
# Decorator Supporting Any Arguments
# --------------------------------------------------

from functools import wraps

def log_activity(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Before function execution
        print(f"Calling: {func.__name__}")

        # Execute original function
        result = func(*args, **kwargs)

        # After function execution
        print(f"Finished: {func.__name__}")

        return result   # Always return original result

    return wrapper


@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and {milk} milk")


brew_chai("Masala")
