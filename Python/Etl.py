def transform(legacy_data):
    transformed_dict = {}
    for key, letter_list in legacy_data.items():
        for letter in letter_list:
            transformed_dict.update({letter.lower():key})
    return transformed_dict