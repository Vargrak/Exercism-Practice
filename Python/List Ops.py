def append(list1, list2):
    appended_list = []
    for item in list1:
        appended_list += [item]
    for item in list2:
        appended_list += [item]
    return appended_list

def concat(lists):
    concat_list = []
    for list_ in lists:
        for x in list_:
            concat_list += [x]
    return concat_list

def filter(function, list_):
    filtered_list = []
    for x in list_:
        if function(x) == True:
            filtered_list += [x]
    return filtered_list

def length(list_):
    count = 0
    for item in list_:
        count += 1
    return count

def map(function, list_):
    mapped_list = []
    for x in list_:
        mapped_list += [function(x)]
    return mapped_list

def foldl(function, list_, initial):
    for x in list_:
       initial = function(initial, x)
    return initial
        
def foldr(function, list_, initial):
    for x in list_[::-1]:
        initial = function(x, initial)
    return initial

def reverse(list_):
    reversed_list = []
    for item in list_[::-1]:
       reversed_list += [item]
    return reversed_list