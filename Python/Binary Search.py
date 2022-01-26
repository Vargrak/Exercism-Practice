def find(search_list, value):
    #check minimum length requirements
    if len(search_list) == 1:
        return 0
    if len(search_list) < 1:
        raise ValueError("value not in array")

    #find middle position and value
    half_index = len(search_list)//2
    half = search_list[half_index]
    
    #check upper-half or lower-half of the array 
    if value >= half:
        for index, list_value in enumerate(search_list[half_index:]):
            if list_value == value:
                return index+len(search_list)//2
    elif value < half:
        for index, list_value in enumerate(search_list[:half_index]):
            if list_value == value:
                return index
    raise ValueError("value not in array")