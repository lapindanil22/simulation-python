import pygame
import actions

entity_size = 10


def pause_simulation():
    pygame.quit()
    quit()


class Simulation:

    def __init__(self, cells) -> None:
        self.epochs_counter = 0
        self.__cells = cells
        pygame.init()
        self.screen = pygame.display.set_mode((self.get_cells().size[0] * entity_size,
                                               self.get_cells().size[1] * entity_size))

    def get_cells(self):
        return self.__cells

    def render(self):
        pygame.draw.rect(self.screen, "black",
                         (0, 0, self.get_cells().size[0] * entity_size, self.get_cells().size[1] * entity_size))
        for coords, entity in self.get_cells().as_dict().items():
            pygame.draw.rect(self.screen, entity.color, (coords[0] * entity_size,
                                                         coords[1] * entity_size,
                                                         entity_size,
                                                         entity_size))

        pygame.display.update()

    def next_turn(self):
        actions.move_all_entities(self.get_cells())
        self.render()

    def start_simulation(self):

        actions.place_entities(self.get_cells())

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause_simulation()

            self.next_turn()
            pygame.time.delay(1000)
