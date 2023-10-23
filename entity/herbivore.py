from entity.creature import Creature


class Herbivore(Creature):
    color = "green"

    def make_move(self):
        ...

    def do_eat(self):
        ...
