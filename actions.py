import random
from copy import deepcopy

from entity import Predator, Herbivore, Tree, Grass, Rock, Creature


def move_all_entities(cells):
    temp_cells = deepcopy(cells)
    for coords, entity in temp_cells.as_dict().items():
        if isinstance(entity, Creature):
            entity.do_move(coords, cells)


def place_entities(cells):
    for i in range(200):
        cells.set_entity((random.randint(0, 1000), random.randint(0, 1000)), Grass())  # random.choice((Tree(), Grass(), Rock())))

    for i in range(20):
        cells.set_entity((random.randint(0, 1000), random.randint(0, 1000)), Herbivore())

    for i in range(3):
        cells.set_entity((random.randint(0, 1000), random.randint(0, 1000)), Predator())
