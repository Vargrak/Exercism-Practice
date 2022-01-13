def score(dice, category):
    return category(dice)

def ones(dice):
    return dice.count(1) * 1

def twos(dice):
    return dice.count(2) * 2

def threes(dice):
    return dice.count(3) * 3

def fours(dice):
    return dice.count(4) * 4

def fives(dice):
    return dice.count(5) * 5

def sixes(dice):
    return dice.count(6) * 6

def full_house(dice):
    die_types = set(dice)
    if len(die_types) == 2:
        for die in die_types:
            if dice.count(die) == 3:
                return sum(dice)
    return 0

def four_of_a_kind(dice):
    for die in dice:
        if dice.count(die) >= 4:
            return die * 4
    return 0

def little_straight(dice):
    dice = sorted(dice)
    if dice == [1, 2, 3, 4, 5]:
        return 30
    return 0

def big_straight(dice):
    dice = sorted(dice)
    if dice == [2, 3, 4, 5, 6]:
        return 30
    return 0

def choice(dice):
    return sum(dice)

def yacht(dice):
    for die in dice:
        if dice.count(die) == 5:
            return 50
    return 0

YACHT = yacht
ONES = ones
TWOS = twos
THREES = threes
FOURS = fours
FIVES = fives
SIXES = sixes
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = choice