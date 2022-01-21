def is_paired(input_string):
    bracket_list = []
    bracket_dict = {"[":"]", "{":"}", "(":")"}

    for char in input_string:
        if char in bracket_dict.keys():
            bracket_list.append(char)

        if char in bracket_dict.values():
            if len(bracket_list) < 1:
                return False
            test_key = ''.join([key for key, value in bracket_dict.items() if char == value])
            if test_key == bracket_list[-1]:
                bracket_list.pop(-1)
            else:
                return False
    if len(bracket_list) == 0:
        return True
    return False