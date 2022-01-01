SUBLIST = "Sublist"
SUPERLIST = "Superlist"
EQUAL = "Equal"
UNEQUAL = "Unequal"

def sublist(list_one, list_two):
        for index_x, x in enumerate(list_one):
            for index_y, y in enumerate(list_two):
                if x == y and list_one[index_x+1] == list_two[index_y+1]:
                    hook = [index_x, index_y]
        if len(list_one) > len(list_two):
            for i in range(hook[0], (hook[0] + len(list_two))):
                print(i)









sublist([1, 2, 3, 4, 5, 6], [3, 4, 5])