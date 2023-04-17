
class Tofik():
    def __init__(self, hp, energy):
        self.hp = hp
        self.energy = energy
        
    def showStats(self):
        print(f"\nTofik\nHP:{self.hp}\nEnergy:{self.energy}\n")
        
    def movement(self):
        while True:
            try:
                numSteps = int(input("How much steps do you want me to make? Meow\n"))
            except ValueError:
                print("Input must be integer")
                continue
            else:
                print(f"Tofik did {numSteps} steps forward")
                break
    
    def abilites(self):
        pass

    def backpack(self, inventorySlots, weight):
        inventorySlots = 20
        for slot in inventorySlots:
            pass