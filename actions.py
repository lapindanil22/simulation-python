from copy import deepcopy

from entity import Predator, Herbivore, Tree, Grass, Rock, Creature


def move_all_entities(cells):
    temp_cells = deepcopy(cells)
    for coords, entity in temp_cells.as_dict().items():
        if isinstance(entity, Creature):
            entity.make_move(coords, cells)


def place_entities(cells):
    cells.set_entity((14, 34), Predator())
    cells.set_entity((15, 35), Herbivore())
    cells.set_entity((23, 35), Tree())
    cells.set_entity((24, 36), Grass())
    cells.set_entity((25, 37), Rock())
