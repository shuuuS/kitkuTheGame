import json

from characters.tofik import Tofik
from characters.kropcia import Kropcia

class Game():
    main_character = Tofik()
    
    def __init__(self):
        pass
    def move(self):
        self.main_character.movement()

    def usingSpell(self):
        self.main_character.abilites()

    def checkBackpack(self):
        pass

    def HUD(self):
        self.main_character.showStats()
    
if __name__ == "__main__":
    Game()

while True:
        action = input("What do you want do?\n 1)Activitis \n 2)Options \n 3)Exit\n")
        if action == "1":
            options = input("\n1)Move\n2)Meow\n")
            if options == "1":
                Game().main_character.movement()
            if options == "2":
                Game().main_character.abilites()
            if options == "3":
                Game().main_character.rest()
        if action == "2":
            options = input("\n1)Check stats\n2) Check Backpack\n")
            if options == "1":
                Game().HUD()
            if options == "2":
                Game().checkBackpack()
        
        if action == "3":
            break




        
        


    



