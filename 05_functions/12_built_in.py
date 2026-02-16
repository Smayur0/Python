

def chai_flavor(flavor="masala"):
    """Return the flavor of chai.""" #it should be the first line of the function body and it should be a string that describes the function's purpose.
    chai = "ginger"
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)
 
# The `help()` function is a built-in function in Python that 
# provides a convenient way to access the documentation of modules, 
# classes, functions, and other objects. It can be used to get 
# information about how to use a particular object, including 
# its methods, attributes, and usage examples.

#  help(len)

def generate_bill(chai = 0, samosa=0):
    """Calculate the total bill for chai and samosa.
    :param chai: number of cups of chai
    :param samosa: number of samosas
    return:(total amount, thank you message as string)"""
    chai_price = 20 
    samosa_price = 30   
    
    total = chai * chai_price + samosa * samosa_price
    return total, f"Thank you for your order! Your total is ₹{total}."