from abc import abstractmethod

from entity.entity import Entity


class Creature(Entity):
    @abstractmethod
    def make_move(self, current_coords, cells):
        pass
