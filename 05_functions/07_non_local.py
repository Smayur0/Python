
#NON-LOCAL VARIABLES: Variables that are not local to the current function but are defined in an enclosing scope. 
# The nonlocal keyword allows us to modify variables in the enclosing scope from within a nested function.
chai_type = "milk wala chai"
def update_order():
    chai_type = "lemon"  # This variable is local to update_order

    def kitchen():
        #Global -  will look in global scope and update the global variable, 
        #Nonlocal -  will look in the enclosing scope (update_order) and update that variable.
        # This allows us to modify the enclosing variable
        nonlocal chai_type  # global chai_type  
        chai_type = "ginger"  # Modifying the enclosing variable

    # print(f"Order before kitchen update: {chai_type}")
    kitchen()
    print(f"Order after kitchen update: {chai_type}")

update_order()
print(f"Global chai type: {chai_type}")