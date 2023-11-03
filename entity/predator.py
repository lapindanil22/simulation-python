import random

from entity.herbivore import Herbivore
from entity.creature import Creature


def find_nearest_herbivore(current_coords, cells):
    nearest_herbivore_coords = (current_coords[0] + random.randint(-1, 1),
                            current_coords[1] + random.randint(-1, 1))
    nearest_dist = 10 ** 6

    for coords, entity in cells.as_dict().items():
        if isinstance(entity, Herbivore):
            dist = max(abs(current_coords[0] - coords[0]),
                       abs(current_coords[1] - coords[1]))
            if dist < 10 and dist < nearest_dist:  # 10 is visibility distance
                nearest_herbivore_coords = coords
                nearest_dist = dist

    return nearest_herbivore_coords


def sign(number):
    if number > 0:
        return 1
    if number < 0:
        return -1
    else:
        return 0


class Predator(Creature):
    color = "red"

    def do_move(self, current_coords, cells):
        target_coords = find_nearest_herbivore(current_coords, cells)

        target_coords = (current_coords[0] + sign(target_coords[0] - current_coords[0]),
                         current_coords[1] + sign(target_coords[1] - current_coords[1]))

        cells.move_entity(current_coords, target_coords)
