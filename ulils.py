import random


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def find_nearest_entity(entity_type, visibility_dist, current_coord, cells):
    nearest_entity_coord = (current_coord[0] + random.randint(-1, 1),
                            current_coord[1] + random.randint(-1, 1))
    nearest_dist = 10 ** 6
    for coord, entity in cells.to_dict():
        if isinstance(entity, entity_type):
            dist = max(abs(current_coord[0] - coord[0]),
                       abs(current_coord[1] - coord[1]))
            if dist < visibility_dist and dist < nearest_dist:
                nearest_entity_coord = coord
                nearest_dist = dist
    return nearest_entity_coord
# return (current_coord[0] + random.randint(-1, 1),
#         current_coord[1] + random.randint(-1, 1))  # TODO solve cell conflict
