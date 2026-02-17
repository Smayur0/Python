# Dictionary Comprehensions
# Dictionary comprehensions are a concise way to create dictionaries.
# They consist of curly braces containing an expression followed 
# by a for clause, then zero or more for or if clauses. The 
# expressions can be anything, meaning you can put in all kinds of objects in dictionaries.


tea_prices_inr = {
    "masala tea": 40,
    "ginger chai": 50,
    "lemon chai": 200,
}


tea_prices_usd = { tea:price / 80 for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)