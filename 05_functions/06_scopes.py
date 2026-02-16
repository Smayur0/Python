# Scope of variables in Python

# LOCAL SCOPE: Variables defined inside a function are local
#  to that function and cannot be accessed outside of it.
def serve_chai():
    chai = "Green tea chai"
    print(f"Inside function: {chai}")

chai = "masala chai"
serve_chai()
print(f"Outside function: {chai}")



# ENCLOSING SCOPE: If a function is defined inside another 
# function, the inner function can access variables of the 
# outer function.

# GLOBAL SCOPE: Variables defined at the top level of a script
# or module are in the global scope and can be accessed from 
# anywhere in the code.

def chai_counter():
    chai_order = "lemon"  # Enclosing scope

    def print_order():
        chai_order = "ginger"  # Local scope
        print(f" inner : {chai_order}")
    print_order()
    print(f" outer : {chai_order}")

chai_order = "masala"  # Global scope
chai_counter()
print(f"Global: {chai_order}")