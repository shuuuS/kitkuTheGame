from characters.tofik import Tofik

class PetFood():
    def __init__(self, name, requiredSpace, value):
        self.name = name
        self.requiredSpace = requiredSpace
        self.value = value

    def informationAboutObject(self):
        print(f"It's {self.name} and need {self.requiredSpace} spaces")

    def effect(self, target):
        target = Tofik(self, self)
        target.hp += self.value

    
        