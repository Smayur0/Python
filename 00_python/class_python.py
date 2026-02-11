class Chai:

    def __init__(self,sweetness,milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("sipping the chai")
    
    def add_sugar(self,):
        print("adding sugar to the chai")

my_chai = Chai(sweetness=5,milk_level=3)

my_chai.add_sugar()
my_chai.sip()