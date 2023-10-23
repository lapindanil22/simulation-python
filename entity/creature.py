from abc import abstractmethod, ABC

from entity.entity import Entity


class Creature(Entity):  # TODO inherit from ABC also
    @abstractmethod
    def make_move(self):
        pass
