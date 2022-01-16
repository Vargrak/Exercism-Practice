scrabble = {("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1,
            ("D", "G") : 2,
            ("B", "C", "M", "P") : 3,
            ("F", "H", "V", "W", "Y") : 4,
            ("K") : 5,
            ("J", "X") : 8,
            ("Q", "Z") : 10}

def score(word):
    points = 0 
    for char in word:
        char = char.upper()
        for key in scrabble:
            if char in key:
                points += scrabble[key]
                break
    return points