def color_code(color, lookup=1):
    dict = colors(lookup)
    return dict[color]


def colors(lookup=0):
    dict = { "black":0,
             "brown":1,
             "red":2,
             "orange":3,
             "yellow":4,
             "green":5,
             "blue":6,
             "violet":7,
             "grey":8,
             "white":9 }
    if lookup == 0: return list(dict.keys())
    else: return dict