import random

class Character:
    def __init__(self):
        self.LOWER = 3
        self.UPPER = 18
        self.generator()

    def generator(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = (10+modifier(self.constitution))
    
    def ability(self):
        rolls = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        rolls = sorted(rolls)
        return sum(rolls[1:])

def modifier(ability_score):
        return (ability_score-10)//2