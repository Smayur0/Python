# Arguments in python


chai = "Ginger chai"

def prepare_chai(order):
    print(f"Preparing {order}...")
    
prepare_chai(chai)
print(chai)

chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42
edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Ginger", "Yes", "high fat")
make_chai(tea="Cardamom", sugar="no", milk="Low")

def special_chai(*ingredients, **extras):
    print("Special chai with:", ingredients)
    print("Extras:", extras)

special_chai("Ginger", "Cardamom", milk="Yes", sugar="No")


# dont use mutable default arguments like lists or dictionaries in function definitions, as they can lead to unexpected behavior 
# due to shared state across function calls.
def chai_order(order=[]):
    order.append("Ginger")
    print(order)

def chai_order(order=[]):
    order.append("Ginger")
    print(order)

chai_order()
chai_order()

# To avoid this issue, use None as the default value and create a new list inside the function if needed.
def chai_order(order=None):
    if order is None:
        order = []  
    print(order)

chai_order()
