class Map:
    def __init__(self, size) -> None:
        self.size = size
        self.__cells = {}

    def clear_cell(self, coord):
        self.__cells.pop(coord, None)

    def set_cell(self, coord, entity_type):
        self.__cells[(coord[0] % self.size[0], coord[1] % self.size[1])] = entity_type()

    def move_entity(self, coord_from, coord_to):
        if coord_from != coord_to:
            self.set_cell(coord_to, type(self.__cells[coord_from]))
            self.clear_cell(coord_from)

    def to_dict(self):
        return self.__cells.items()
