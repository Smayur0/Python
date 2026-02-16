# A function can return a value using the return statement.
def make_chai():
    return "Here is your masala chai!"

# 1.`make_chai()` calls the function and returns the string "Here is your masala chai!".
print(make_chai())  

# 2. The return value of the function is stored in the variable return_value.
return_value = make_chai() 
print(return_value)

# If a function does not have a return statement, 
# it will return None by default.
def idle_chaiWala():
    pass
print(idle_chaiWala())


#return one value from a function and use it in an expression.
def sold_cups():
    return 5

total_cups = sold_cups()
print(total_cups)

#return a value based on a condition.

def chai_status(cups_left):
    if cups_left > 0:
        return "Chai is available!"
    else:
        return "Sorry, we're out of chai."
    
print(chai_status(3))  # Output: Chai is available!
print(chai_status(0))  # Output: Sorry, we're out of chai.
    

# return multiple values from a function using a tuple.
def chai_details():
    name = "Masala Chai"
    price = 50
    description = "A flavorful blend of tea, spices, and milk."
    return name, price , description

chai_name, chai_price , _ = chai_details()
print(f"Chai Name: {chai_name}, Price: {chai_price}, {_}")


# _ means that we are ignoring the description value returned by the function.