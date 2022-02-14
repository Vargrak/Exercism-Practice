from itertools import zip_longest

def transpose(lines):
    lines = lines.replace(" ", "_")
    tupled_list = list(zip_longest(*lines.split("\n"), fillvalue=" "))
    detupled_list = [''.join(item).rstrip() for item in tupled_list]
    transposed = '\n'.join(detupled_list).replace("_", " ")
    return transposed