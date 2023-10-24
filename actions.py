import random
from copy import deepcopy

from entity import Predator, Herbivore, Tree, Grass, Rock, Creature


def move_all_entities(cells):
    temp_cells = deepcopy(cells)
    for coords, entity in temp_cells.as_dict().items():
        if isinstance(entity, Creature):
            entity.make_move(coords, cells)


def place_entities(cells):
    for i in range(100):
        cells.set_entity((random.randint(0, 1000), random.randint(0, 1000)),
                         random.choice((Predator(), Herbivore(), Tree(), Grass(), Rock())))
