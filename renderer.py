import pygame


class Renderer:
    def __init__(self, map_size: tuple[int, int], cell_size_px: int):
        self.__cell_size_px = cell_size_px
        self.__screen = pygame.display.set_mode((map_size[0] * cell_size_px,
                                                 map_size[1] * cell_size_px))

    def render(self, cells):
        pygame.draw.rect(self.__screen, "black",
                         (0, 0, cells.size[0] * self.__cell_size_px,
                          cells.size[1] * self.__cell_size_px))
        for coord, entity in cells.to_dict():
            pygame.draw.rect(self.__screen, entity.color, (coord[0] * self.__cell_size_px,
                                                           coord[1] * self.__cell_size_px,
                                                           self.__cell_size_px,
                                                           self.__cell_size_px))
        pygame.display.update()
