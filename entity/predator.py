import random

from entity.herbivore import Herbivore
from entity.creature import Creature
from ulils import sign


class Predator(Creature):
    color = "red"
    visibility_dist = 5

    def do_move(self, current_coord, cells):
        target_coords = self.find_nearest_herbivore(current_coord, cells)
        target_coords = (current_coord[0] + sign(target_coords[0] - current_coord[0]),
                         current_coord[1] + sign(target_coords[1] - current_coord[1]))
        cells.move_entity(current_coord, target_coords)

    @classmethod
    def find_nearest_herbivore(cls, current_coord, cells):
        nearest_herbivore_coord = (current_coord[0] + random.randint(-1, 1),
                                   current_coord[1] + random.randint(-1, 1))
        nearest_dist = 10 ** 6

        for coords, entity in cells.as_dict().items():
            if isinstance(entity, Herbivore):
                dist = max(abs(current_coord[0] - coords[0]),
                           abs(current_coord[1] - coords[1]))
                if dist < cls.visibility_dist and dist < nearest_dist:
                    nearest_herbivore_coord = coords
                    nearest_dist = dist

        return nearest_herbivore_coord
