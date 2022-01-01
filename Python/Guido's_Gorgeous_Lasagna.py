EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calc how much time is left till done baking"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Total minutes for x number of layers"""
    return 2 * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Time since start of cooking (baking plus layering)"""
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)