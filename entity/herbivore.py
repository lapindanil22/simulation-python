import random

from entity.grass import Grass
from entity.creature import Creature


def find_nearest_grass(current_coords, cells):
    nearest_grass_coords = (current_coords[0] + random.randint(-1, 1),
                            current_coords[1] + random.randint(-1, 1))
    nearest_dist = 10 ** 6

    for coords, entity in cells.as_dict().items():
        if isinstance(entity, Grass):
            dist = max(abs(current_coords[0] - coords[0]),
                       abs(current_coords[1] - coords[1]))
            if dist < nearest_dist:
                nearest_grass_coords = coords
                nearest_dist = dist

    return nearest_grass_coords

    # return (current_coords[0] + random.randint(-1, 1),
    #         current_coords[1] + random.randint(-1, 1))  # TODO solve cell conflict


def sign(number):
    if number > 0:
        return 1
    if number < 0:
        return -1
    else:
        return 0


class Herbivore(Creature):
    color = "green"

    def do_move(self, current_coords, cells):
        target_coords = find_nearest_grass(current_coords, cells)

        target_coords = (current_coords[0] + sign(target_coords[0] - current_coords[0]),
                         current_coords[1] + sign(target_coords[1] - current_coords[1]))

        cells.move_entity(current_coords, target_coords)
