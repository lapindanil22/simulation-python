class Map:
    def __init__(self, size) -> None:
        self.size = size
        self.map = {}

    def clear_cell(self, coords):
        self.map.pop(coords, None)

    def set_entity(self, coords, entity):  # TODO boundary check
        self.map[coords] = entity

    def move_entity(self, coords_from, coords_to):
        self.set_entity(coords_to, self.map[coords_from])
        self.clear_cell(coords_from)

    def as_dict(self):
        return self.map
