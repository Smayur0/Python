# pure fucntions are functions that always return the same 
# output for the same input and have no side effects 
# (they do not modify any external state).

def pure_function(cups):
    return cups * 2

total_chai = 0

# impure functions are functions that may return different 
# outputs for the same input
def impure_function(cups):
    global total_chai
    total_chai += cups
    return total_chai

# recursive function is a function that calls itself in 
# order to solve a problem.
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured!"
    return pour_chai(n - 1)

print(pour_chai(5))  # Output: 15 (5 + 4 + 3 + 2 + 1 + 0)


# lambda function is a small anonymous function that can 
# take any number of arguments,

chai_types = ["Masala Chai", "Green Chai", "Lemon Chai"]

strong_chai = list(filter(lambda chai: "Masala" in chai, chai_types))
print(strong_chai)  # Output: ['Masala Chai']