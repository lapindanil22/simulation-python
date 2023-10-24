from entity.creature import Creature


class Predator(Creature):
    color = "red"

    def make_move(self, current_coords, cells):
        cells.move_entity(current_coords, (current_coords[0] + 1, current_coords[1] + 2))

    def do_attack(self):
        ...
