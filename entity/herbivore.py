import random

from entity.grass import Grass
from entity.creature import Creature
from ulils import sign


class Herbivore(Creature):
    color = "green"
    visibility_dist = 10

    def do_move(self, current_coord, cells):
        target_coords = self.find_nearest_grass(current_coord, cells)

        target_coords = (current_coord[0] + sign(target_coords[0] - current_coord[0]),
                         current_coord[1] + sign(target_coords[1] - current_coord[1]))

        cells.move_entity(current_coord, target_coords)

    @classmethod
    def find_nearest_grass(cls, current_coords, cells):
        nearest_grass_coords = (current_coords[0] + random.randint(-1, 1),
                                current_coords[1] + random.randint(-1, 1))
        nearest_dist = 10 ** 6

        for coords, entity in cells.as_dict().items():
            if isinstance(entity, Grass):
                dist = max(abs(current_coords[0] - coords[0]),
                           abs(current_coords[1] - coords[1]))
                if dist < cls.visibility_dist and dist < nearest_dist:
                    nearest_grass_coords = coords
                    nearest_dist = dist

        return nearest_grass_coords

        # return (current_coords[0] + random.randint(-1, 1),
        #         current_coords[1] + random.randint(-1, 1))  # TODO solve cell conflict
