from entity.creature import Creature


class Predator(Creature):
    color = "red"

    def make_move(self):
        ...

    def do_attack(self):
        ...
