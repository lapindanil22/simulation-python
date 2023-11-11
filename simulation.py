import pygame
import actions
from renderer import Renderer
from simulation_map import SimulationMap


class Simulation:
    cell_size_px = 10

    def __init__(self, map_size) -> None:
        self.__cells = SimulationMap(map_size)
        self.renderer = Renderer(map_size, self.cell_size_px)

    def next_turn(self):
        actions.move_all_entities(self.__cells)

    def start(self, population):
        actions.place_entities(self.__cells, population)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.next_turn()
            self.renderer.render(self.__cells)
            pygame.time.Clock().tick(15)
