import random
from copy import deepcopy

from entity import Predator, Herbivore, Tree, Grass, Rock, Creature


def move_all_entities(cells):
    temp_cells = deepcopy(cells)
    for coord, entity in temp_cells.to_dict():
        if isinstance(entity, Creature):
            entity.do_move(coord, cells)


def place_entities(cells):
    for i in range(200):
        cells.set_cell((random.randint(0, 1000), random.randint(0, 1000)), Grass)  # random.choice((Tree(), Rock())))

    for i in range(20):
        cells.set_cell((random.randint(0, 1000), random.randint(0, 1000)), Herbivore)

    for i in range(3):
        cells.set_cell((random.randint(0, 1000), random.randint(0, 1000)), Predator)
