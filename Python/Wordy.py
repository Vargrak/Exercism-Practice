operator_dict = { "plus" : "+",
                  "minus" : "-",
                  "divided" : "//",
                  "multiplied" : "*",
                  "raised" : "**"}

operator_list = {"+", "-", "*", "/", "//"}
test_list = {"+", "*", "/", "//"}

def answer(question):
    should_have_op = 0
    list_question = question.split(" ")
    list_question = [question for question in list_question if not ""]
    if len(list_question) < 3:
        raise ValueError("syntax error")
    elif len(list_question) >= 4:
        should_have_op = 1

    for key, value in operator_dict.items():
        question = question.replace(key, value)
    check_str = ''.join(char for char in question if char.isdigit() or char in operator_list or char.isspace())
    check_str = check_str.strip(" ")
    check_str = ''.join(sequence_check(check_str, should_have_op))
    return eval(check_str)
    
def sequence_check(check_str, should_have_op):
    check_list = check_str.split(" ")
    for var in check_list:
        if var == "":
            check_list.remove("")
    op_count, num_count = 0, 0

    for index, var in enumerate(check_list):
        if index % 2 != 0 and var not in operator_list:
            raise ValueError("syntax error")
        elif index % 2 == 0 and var in test_list:
            raise ValueError("syntax error")
        if var in operator_list:
            op_count += 1
        else:
            num_count += 1
        if op_count == 2:
            insert_idx = index

    if num_count != 1 and op_count == 0 or op_count == 0 and should_have_op == 1:
        raise ValueError("unknown operation")
    elif num_count == 1 and op_count == 1:
        raise ValueError("syntax error")
    if op_count >= 2:
        check_list.insert(0, "(")
        check_list.insert(insert_idx, ")")
    return check_list