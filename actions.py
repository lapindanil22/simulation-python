import random
from copy import deepcopy
from entities import Entity

from simulation_map import SimulationMap


def move_all_entities(cells: SimulationMap):
    from entities import Creature
    temp_cells = deepcopy(cells)
    for coord, entity in temp_cells.to_dict():
        if isinstance(entity, Creature):
            entity.do_move(coord, cells)


def init_place_entities(cells: SimulationMap,
                        population: dict):
    for entity_type, quantity in population.items():
        for _ in range(quantity):
            cells.set_cell((random.randint(0, cells.size[0]), random.randint(0, cells.size[1])), entity_type)


def find_nearest_entity(entity_type: Entity,
                        visibility_dist: int,
                        current_coord: tuple[int, int],
                        cells: SimulationMap) -> tuple[int, int]:
    nearest_entity_coord = None
    nearest_dist = 10 ** 6
    for coord, entity in cells.to_dict():
        if isinstance(entity, entity_type):
            dist = max(abs(current_coord[0] - coord[0]),
                       abs(current_coord[1] - coord[1]))  # TODO find entity through map edge
            if dist < visibility_dist and dist < nearest_dist:
                nearest_entity_coord = coord
                nearest_dist = dist
    return nearest_entity_coord
