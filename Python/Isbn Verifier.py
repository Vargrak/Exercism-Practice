def is_valid(isbn):
    sum = 0
    isbn_list = [number for number in isbn if number != "-"]
    isbn_list.reverse()
    for index, value in enumerate(isbn_list):
        if index == 0 and value == "X":
            value = 10
        elif value.isdigit() == False:
            return False
        sum += (index+1) * int(value)


    if sum % 11 == 0 and len(isbn_list) == 10:
        return True
    return False