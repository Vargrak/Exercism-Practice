

def color_code(color, lookup=1):
    dict = colors(lookup)
    return dict[color.capitalize()]


def colors(lookup=0):
    dict = { "Black":0,
             "Brown":1,
             "Red":2,
             "Orange":3,
             "Yellow":4,
             "Green":5,
             "Blue":6,
             "Violet":7,
             "Grey":8,
             "White":9 }
    if lookup == 0: return list(dict.keys())
    else: return dict

print(color_code("orange"))