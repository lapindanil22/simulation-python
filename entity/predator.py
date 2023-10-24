import random

from entity.creature import Creature


class Predator(Creature):
    color = "red"

    def make_move(self, current_coords, cells):
        cells.move_entity(current_coords, (current_coords[0] + random.randint(-1, 1), current_coords[1] + random.randint(-1, 1)))

    def do_attack(self):
        ...
