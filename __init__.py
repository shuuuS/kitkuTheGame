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

    def HUD(self):
        self.main_character.showStats()

    def move(self):
        self.main_character.movement()

    def useItem(self):
        self.whiskas.effect(self.main_character.hp)
        print(f"Tofik ate {self.whiskas.name} and got {self.whiskas.value} missing HP. Now has {self.main_character.hp}")
        

    
if __name__ == "__main__":
    Game()

while True:
        Game().HUD()
        action = input("What do you want do? (move, meow, use item)\n")
        if action == "move":
            steps = Game().move()
        if action == "meow":
            print("Meow Meow! o.o")
        if action == "use item":
            Game().useItem()
        




        
        


    



