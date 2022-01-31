def flatten(iterable):
    flattened_list = []
    for item in iterable:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        elif item != None:
            flattened_list.append(item)
    return flattened_list