class Map:
    def __init__(self, size) -> None:
        self.size = size
        self.cells = {}

    def clear_cell(self, coords):
        self.cells.pop(coords, None)

    def set_entity(self, coords, entity):
        self.cells[(coords[0] % self.size[0], coords[1] % self.size[1])] = entity

    def move_entity(self, coords_from, coords_to):
        self.set_entity(coords_to, self.cells[coords_from])
        self.clear_cell(coords_from)

    def as_dict(self):
        return self.cells
