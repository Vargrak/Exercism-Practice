def append(list1, list2):
    appended_list = []
    for item in list1:
        appended_list.append(item)
    for item in list2:
        appended_list.append(item)
    return appended_list

def concat(lists):
    concat_list = []
    for list_ in lists:
        for item in list_:
            concat_list.append(item)
    return concat_list

def filter(function, list):
    filtered_list = []
    for item in list:
        x = item
        if function == True:
            filtered_list.append(item)
    return filtered_list

def length(list):
    count = 0
    for item in list:
        count += 1
    return count

def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
