import pygame
import actions
from renderer import Renderer
from simulation_map import SimulationMap


class Simulation:
    def __init__(self, map_size, cell_size_px):
        self.__cells = SimulationMap(map_size)
        self.renderer = Renderer(map_size, cell_size_px)

    def next_turn(self):
        actions.move_all_entities(self.__cells)

    def start(self, population, fps_limit):
        actions.place_entities(self.__cells, population)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.next_turn()
            self.renderer.render(self.__cells)
            pygame.time.Clock().tick(fps_limit)
