#WIP
from itertools import zip_longest

def transpose(lines):
    rows = lines.split("\n")
    tupled_list = list(zip_longest(*rows, fillvalue=" "))
    detupled_list = [''.join(item) for item in tupled_list]
    return '\n'.join(detupled_list)


print(transpose("\n".join(lines)))