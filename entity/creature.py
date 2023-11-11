from abc import abstractmethod, ABC

from entity.entity import Entity


class Creature(Entity, ABC):
    @abstractmethod
    def do_move(self, current_coord, cells):
        pass
