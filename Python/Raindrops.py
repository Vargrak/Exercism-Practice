def convert(number):
    string = ""
    modulo = [3, 5, 7]
    rain = ["Pling", "Plang", "Plong"]

    for index, mod in enumerate(modulo):
        if number % mod == 0:
            string += rain[index]

    return string or str(number)