class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergens = {128:"cats", 64:"pollen", 32:"chocolate", 16:"tomatoes", 8:"strawberries", 4:"shellfish", 2:"peanuts", 1:"eggs"}

    def allergic_to(self, item):
        if item in self.lst:
            return True
        return False

    @property
    def lst(self):
        return [self.allergens[key] for key in self.allergens if key & self.score]