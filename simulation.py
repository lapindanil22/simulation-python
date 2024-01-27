import pygame
import actions
from renderer import Renderer
from simulation_map import SimulationMap


class Simulation:
    def __init__(self, map_size: tuple[int, int], cell_size_px: int):
        self.cells = SimulationMap(map_size)
        self.renderer = Renderer(map_size, cell_size_px)

    def next_turn(self):
        actions.move_all_entities(self.cells)

    def start(self, population: dict, fps_limit: int):
        actions.init_place_entities(self.cells, population)
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.next_turn()
            self.renderer.render(self.cells)
            clock.tick(fps_limit)
