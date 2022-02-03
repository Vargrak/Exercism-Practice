def append(list1, list2):
    """Adds two lists together by adding each of the lists together"""
    appended_list = list1 + list2
    return appended_list

def concat(lists):
    """Flattens one layer in a list of lists down. For every item in the list it takes everything one layer down and adds it into a new list."""
    concat_list = []
    for list_ in lists:
        for x in list_:
            concat_list += [x]
    return concat_list

def filter(function, list_):
    """Function inserted is a lambda that returns a bool. It compares against each item in the input list to determine if it is added to the output list."""
    filtered_list = []
    for x in list_:
        if function(x) == True:
            filtered_list += [x]
    return filtered_list

def length(list_):
    """Simply cycles through every item and increments count. Result should be length of the list."""
    count = 0
    for item in list_:
        count += 1
    return count

def map(function, list_):
    """Applies a lambda function to each item in the list provided and outputs the results in a new list."""
    mapped_list = []
    for x in list_:
        mapped_list += [function(x)]
    return mapped_list

def foldl(function, list_, initial):
    """For every item in a list, take an initial value and apply a lambda function to that item. Result is the new value of 'initial'"""
    for x in list_:
       initial = function(initial, x)
    return initial
        
def foldr(function, list_, initial):
    """Same as foldl but reversed."""
    for x in list_[::-1]:
        initial = function(x, initial)
    return initial

def reverse(list_):
    """Takes a list and parses it in reverse to append it to a new, reversed list."""
    reversed_list = []
    for item in list_[::-1]:
       reversed_list += [item]
    return reversed_list