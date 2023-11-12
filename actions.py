import random
from copy import deepcopy

# from entities import Creature


def move_all_entities(cells):
    from entity import Creature
    temp_cells = deepcopy(cells)
    for coord, entity in temp_cells.to_dict():
        if isinstance(entity, Creature):
            entity.do_move(coord, cells)


def place_entities(cells, population):
    for entity_type, quantity in population.items():
        for _ in range(quantity):
            cells.set_cell((random.randint(0, cells.size[0]), random.randint(0, cells.size[1])), entity_type)


def find_nearest_entity(entity_type, visibility_dist, current_coord, cells):
    nearest_entity_coord = (current_coord[0] + random.randint(-1, 1),
                            current_coord[1] + random.randint(-1, 1))
    nearest_dist = 10 ** 6
    for coord, entity in cells.to_dict():
        if isinstance(entity, entity_type):
            dist = max(abs(current_coord[0] - coord[0]),
                       abs(current_coord[1] - coord[1]))  # TODO find entity through map edge
            if dist < visibility_dist and dist < nearest_dist:
                nearest_entity_coord = coord
                nearest_dist = dist
    return nearest_entity_coord
