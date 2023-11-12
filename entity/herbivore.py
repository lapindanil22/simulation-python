from entity.grass import Grass
from entity.creature import Creature
from ulils import sign
from actions import find_nearest_entity


class Herbivore(Creature):
    color = "white"
    visibility_dist = 10

    def do_move(self, current_coord, cells):
        target_coord = find_nearest_entity(Grass, self.visibility_dist, current_coord, cells)
        target_coord = (current_coord[0] + sign(target_coord[0] - current_coord[0]),
                        current_coord[1] + sign(target_coord[1] - current_coord[1]))
        cells.move_entity(current_coord, target_coord)
