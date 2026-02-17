# All imports  
import recipes.flavours

print(recipes.flavours.ginger_chai())


#named imports
from recipes.flavours import elachai_chai, ginger_chai

print(elachai_chai())
print(ginger_chai())


# relative imports
from .recipes.flavours import elachai_chai
print(elachai_chai())