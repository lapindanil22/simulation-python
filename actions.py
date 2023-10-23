from copy import deepcopy

from entity import Predator, Herbivore, Tree, Grass, Rock


def move_all_entities(cells):
    temp_cells = deepcopy(cells)
    for coords, entity in temp_cells.as_dict().items():
        cells.move_entity(coords, (coords[0] + 1, coords[1]))


def place_entities(cells):
    cells.set_entity((14, 34), Predator())
    cells.set_entity((15, 35), Herbivore())
    cells.set_entity((23, 35), Tree())
    cells.set_entity((24, 36), Grass())
    cells.set_entity((25, 37), Rock())
    # simulation.get_map().clear_cell((23, 36))
    # cells.move_entity((14, 34), (20, 34))
