def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    return convert_coordinate(azara_record[1]) == rui_record[1]

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"

def clean_up(combined_record_group):
    report = ""
    for subtuple in combined_record_group:
        temp = list(subtuple)
        del temp[1]

        new_tuple = tuple(temp)
        report = report + str(new_tuple) + "\n"
    return report