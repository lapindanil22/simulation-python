import pygame
import actions
from map import Map


class Simulation:
    cell_size_px = 10

    def __init__(self, size) -> None:
        self.__cells = Map(size)
        self.__screen = pygame.display.set_mode((self.get_cells().size[0] * self.cell_size_px,
                                                 self.get_cells().size[1] * self.cell_size_px))

    def get_cells(self):
        return self.__cells

    def render(self):
        pygame.draw.rect(self.__screen, "black",
                         (0, 0, self.get_cells().size[0] * self.cell_size_px,
                          self.get_cells().size[1] * self.cell_size_px))
        for coords, entity in self.get_cells().as_dict().items():
            pygame.draw.rect(self.__screen, entity.color, (coords[0] * self.cell_size_px,
                                                           coords[1] * self.cell_size_px,
                                                           self.cell_size_px,
                                                           self.cell_size_px))
        pygame.display.update()

    def next_turn(self):
        actions.move_all_entities(self.get_cells())
        self.render()

    def start(self):
        actions.place_entities(self.get_cells())
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.next_turn()
            pygame.time.Clock().tick(15)
