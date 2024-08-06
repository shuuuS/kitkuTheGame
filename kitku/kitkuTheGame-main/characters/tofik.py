
class Tofik():
    def __init__(self, hp=20, energy=15):
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
                self.energy -= numSteps
 
                if self.energy <= 0:
                    print(f"Tofik must take break, it has {self.energy} energy")
                else:
                    print(f"Tofik did {numSteps} steps forward")
                
                return numSteps
        
    def abilites(self, lostEnergyValue=7):
        if self.energy > 0 and self.energy >= lostEnergyValue:
            self.energy -= lostEnergyValue
            print(f"Tofik tried taunt enemy and lost {lostEnergyValue} energy. Now he has {self.energy} energy")
        else:
            print(f"Tofik needs rest...he has only {self.energy} energy")
    
    def rest(self):
        self.energy += 5
        print(f"Tofik did quick break and he has {self.energy} energy now :D ")
    def backpack(self, color, backpackSlots, backpackItems):
        self.color = color
        self.backpackSlots = backpackSlots
        self.backpackItems = backpackItems
        if self.color == "Green":
            print(f"Your backpack has {self.backpackSlots} slots and items: {self.backpackItems}")
        if self.color == "Red":
            print(f"Your backpack has {self.backpackSlots} slots and items: {self.backpackItems}")
        

        