SUBLIST = "Sublist"
SUPERLIST = "Superlist"
EQUAL = "Equal"
UNEQUAL = "Unequal"

def sublist(list_one, list_two):
    if len(list_one) > len(list_two):
        if list_two == []:
            return SUPERLIST
        for index in range(0, len(list_one) - len(list_two) + 1):
            if list_one[index:(index+len(list_two))] == list_two:
                return SUPERLIST
        return UNEQUAL

    if len(list_two) > len(list_one):
        if list_one == []:
            return SUBLIST
        for index in range(0, len(list_two) - len(list_one) + 1):
            if list_two[index:(index+len(list_one))] == list_one:
                return SUBLIST
        return UNEQUAL

    if list_one == list_two:
        return EQUAL
    return UNEQUAL