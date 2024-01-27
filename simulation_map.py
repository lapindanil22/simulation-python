from entities import Entity


class SimulationMap:
    def __init__(self, size: tuple[int, int]):
        self.size = size
        self.cells = dict()

    def clear_cell(self, coord):
        self.cells.pop(coord, None)

    def set_cell(self,
                 coord: tuple[int, int],
                 entity_type: Entity):
        self.cells[(coord[0] % self.size[0], coord[1] % self.size[1])] = entity_type()

    def move_entity(self, coord_from, coord_to):
        if coord_from != coord_to:
            self.set_cell(coord_to, type(self.cells[coord_from]))
            self.clear_cell(coord_from)

    def to_dict(self):
        return self.cells.items()
