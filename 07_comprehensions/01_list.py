# List Comprehensions
# List comprehensions are a concise way to create lists. 
# They consist of brackets containing an expression followed 
# by a for clause, then zero or more for or if clauses. The 
# expressions can be anything, meaning you can put in all 
# kinds of objects in lists.


menu = [
    "masala chai",
    "ginger chai",
    "cardamom chai",
    "Ice tea",

]
#1. Using list comprehension, create a list of all the teas 
# in the menu that contain the word "iced".
iced_tea = [tea for tea in menu if "iced" in tea]
print(iced_tea)

#2.
Chai = [tea for tea in menu if "chai" in tea]
print(Chai)

#3.
iced_tea = [tea for tea in menu if len(tea) > 10]
print(iced_tea)