def find(search_list, value):
    if len(search_list) == 1:
        return search_list

    half = len(search_list)//2
    if value > half:
        if value in search_list[half:]:
            return value
    elif value <= half:
        if value in search_list[:half]:
            return value
    raise ValueError("value not in array")