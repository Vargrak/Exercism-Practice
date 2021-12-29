def get_rounds(round_number):
    rounds = [round_number, round_number + 1, round_number + 2]
    return rounds

def concatenate_rounds(round_1, round_2):
    return round_1 + round_2

def list_contains_round(rounds, round_number):
    return round_number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    return ((hand[0] + hand[-1]) / 2) == card_average(hand) or card_average(hand) == hand[(len(hand)//2)]

def average_even_is_average_odd(hand):
    return  (sum(hand[::2]) / len(hand[::2])) == card_average(hand) or card_average(hand) == (sum(hand[1::2]) / len(hand[1::2]))
    

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
