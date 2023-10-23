class Map:
    def __init__(self, size) -> None:
        self.size = size
        self.map = {}

    def set_entity(self, coords, entity):  # TODO boundary check
        self.map[coords] = entity

    def as_dict(self):
        return self.map
