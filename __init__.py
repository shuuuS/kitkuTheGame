from characters.tofik import Tofik
from characters.kropcia import Kropcia

from possibleLoot.petfood import PetFood
from possibleLoot.drinks import Drinks

class Game():
    def __init__(self):
        self.main_character = Tofik(20, 15)

        self.final_character = Kropcia(self, self)
        

        self.whiskas = PetFood("Whiskas", 3, 7)
        self.milk = Drinks("Giga milk", 2)

    def checkBackpack(self):
        self.main_character.backpack("Green", 3, (self.whiskas.name, self.milk.name))

    def HUD(self):
        self.main_character.showStats()

    def move(self):
        self.main_character.movement()

    def useItem(self):
        self.whiskas.effect(self.main_character.hp)
        
    def usingSpell(self):
        self.main_character.abilites(self.main_character.energy, 7)
        print(f"Now Tofik has {self.main_character.energy}")
        

    
if __name__ == "__main__":
    Game()

while True:
        action = input("What do you want do? (move, meow, use item, check backpack)\n")
        if action == "move":
            Game().move()
            
        if action == "check stats":
            Game().HUD()
        
        if action == "meow":
            Game().usingSpell()

        if action == "check backpack":
            Game().checkBackpack()

        if action == "use item":
            if Game().main_character.hp >= 20:
                print("Cant do that, i will be too fat")   
            else: 
                Game().useItem()
        
        if action == "exit":
            break




        
        


    



