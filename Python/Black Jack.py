def value_of_card(card):
    return int(card_dictionary(card))
    
def higher_card(card_one, card_two):
    int_hand = hand_to_int(card_one, card_two)
    if int(int_hand[0]) > int(int_hand[1]):
        return card_one
    elif int(int_hand[0]) < int(int_hand[1]):
        return card_two
    else:
        return (card_one, card_two)

def value_of_ace(card_one, card_two):
    int_hand = hand_to_int(card_one, card_two)
    if sum(int_hand) >= 11:
        return 1
    elif sum(int_hand) < 11:
        return 11

def is_blackjack(card_one, card_two):
    hand = [card_one, card_two]
    if "A" in hand:
        if "K" in hand or "Q" in hand or "J" in hand or "10" in hand:
            return True
        else:
            return False
    return False

def can_split_pairs(card_one, card_two):
    int_hand = hand_to_int(card_one, card_two)
    if int_hand[0] == int_hand[1]:
        return True
    return False

def can_double_down(card_one, card_two):
    total = sum(hand_to_int(card_one, card_two))
    if total == 11 or total == 10 or total == 9:
        return True
    return False

def card_dictionary(card):
    cards = { "A":"1",
              "K":"10",
              "Q":"10",
              "J":"10"  }
    if card in cards:
        return cards.get(card)
    else:
        return card

def hand_to_int(card_one, card_two):
    hand, int_hand = [card_one, card_two], []
    for card in hand:
        card = int(card_dictionary(card))
        int_hand.append(card)
    return int_hand