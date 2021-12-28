def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost is True:
        return True
    else:
        return False

def score(touching_power_pellet, touching_dot):
    if touching_power_pellet or touching_dot is True:
        return True
    else:
        return False

def lose(power_pellet_active, touching_ghost):
    if power_pellet_active is False and touching_ghost is True:
        return True
    else:
        return False

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if lose(power_pellet_active, touching_ghost) is True:
        return False
    elif has_eaten_all_dots is True:
        return True
    else:
        return False