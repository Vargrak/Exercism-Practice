class Alien:
    total_aliens_created = 0

    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health = self.health - 1
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other_object):
        pass

def new_aliens_collection(coord_list):
    aliens = [Alien(coordinates[0], coordinates[1]) for  coordinates in coord_list]
    return aliens