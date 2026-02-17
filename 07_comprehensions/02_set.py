# set compressions
# Set comprehensions are similar to list comprehensions,
# but they create sets instead of lists.

chais = ["masala chai", "ginger chai", "cardamom chai", 
         "Ice tea", "lemon tea", "Green tea",
        "black tea", "herbal tea","Ice tea","Ice tea"
         ]


unique_chais = {tea for tea in chais}
# print(unique_chais)


recipes = {
    "masala chai": ["ginger","clove"],
    "ginger chai": ["clove", "cardamom", "ginger"],
    "cardamom chai": ["black peppre", "cardamom"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)    