class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self, card_listd = None):
        card_listd = []
        card_num = self.card_num
        card_spaceless = ''.join(char for char in card_num if char not in " ")
        if card_spaceless.isdigit():
            for i in range(-1, -len(card_spaceless)-1, -1):
                if i % -2 == 0:
                    product = int(card_spaceless[i]) * 2
                    if product > 9:
                        product = product - 9
                    card_listd.append(product)
                else:
                    card_listd.append(int(card_spaceless[i]))
            card_sum = sum(card_listd)
            if card_sum % 10 == 0 and len(card_listd) > 1:
                return True
            return False
        return False