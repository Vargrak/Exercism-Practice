def is_armstrong_number(number):
    total = 0
    number_list = [char for char in str(number)]
    for char in number_list:
       total += int(char) ** len(number_list)
    return total == number