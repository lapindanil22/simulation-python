from abc import abstractmethod

from entities import Entity
from simulation_map import SimulationMap


class Creature(Entity):
    @abstractmethod
    def do_move(self,
                current_coord: tuple[int, int],
                cells: SimulationMap):
        pass
